import os
import cv2
import tkinter as tk
from tkinter import filedialog
import customtkinter
import cv2
from PIL import Image, ImageTk
from ocr_model import *
from pygame import mixer
import tensorflow as tf
import flet as ft

def main(page: ft.Page):
    page.title = "Soundify"
    page.icon = "assets/icon.ico"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    dark_theme = True
    link = " "
    sound = True
    arabic_text = " "
    model = keras.models.load_model(os.path.join("model", "arabic-OCR.h5"))

    

    def theme_switch(e):
        nonlocal dark_theme
        if dark_theme:
            page.theme = "light"
            dark_theme = False
        else:
            page.theme = "dark"
            dark_theme = True

    def from_file(e):
        nonlocal link
        link = filedialog.askopenfilename()
        my_img = Image.open(link)
        resized_img = my_img.resize((200, 200))
        new_img = ImageTk.PhotoImage(resized_img)
        text_display.value = ""
        text_display.update()
        text_to_sound(link)

    def text_to_sound(link):
        nonlocal arabic_text
        arabic_text = pred_one_img(model, link)
        with open('output2.txt', 'w', encoding='utf-8') as file:
            file.write(arabic_text)
        text_to_speech(arabic_text)

    def play_audio(e):
        nonlocal sound
        if sound:
            mixer.init()
            mixer.music.load('test.mp3')
            mixer.music.play()
            sound = False
        else:
            mixer.music.stop()
            sound = True

    def set_text():
        text_display.value = arabic_text
        text_display.update()
        
    theme_switcher = ft.ElevatedButton(text="Theme", on_click=theme_switch)
    select_file = ft.ElevatedButton(text="Browse", on_click=from_file)
    text_display = ft.Text(value="", width=40, height=10)
    play_audio = ft.ElevatedButton(text="Play", on_click=play_audio)

    row1 = ft.Row(controls=[theme_switcher, select_file])
    row2 = ft.Row(controls=[text_display])
    row3 = ft.Row(controls=[play_audio])

    page.add(row1)
    page.add(row2)
    page.add(row3)

if __name__ == "__main__":
    ft.app(target=main)