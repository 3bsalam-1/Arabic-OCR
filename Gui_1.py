# Import Needed Packages
import warnings
warnings.filterwarnings('ignore')
import os
from tkinter import *
from tkinter.filedialog import askopenfilename
import customtkinter
import cv2
from PIL import Image, ImageTk
from ocr_model import *
from pygame import mixer

# Initialize Gui Window
root = customtkinter.CTk()
root.geometry("820x370")
root.resizable(True, True)
root.title('Soundify')
root.iconbitmap(os.path.join('assets', "icon.ico"))
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
dark_theme = True  # Helpful In Themes Switcher
cam = True  # Helpful In Camera Status Switcher
link = " "
sound = True
arabic_text=" "
opencv_image = None
captured_image = None
# Define a video capture object
vid = cv2.VideoCapture(0)
# Declare the width and height in variables
width, height = 200, 200
# Set the width and height
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
# Theme Switcher Button Icons Initialization
img_light = PhotoImage(file=os.path.join('assets', 'light.png'))
img_dark = PhotoImage(file=os.path.join('assets', "dark.png"))
# Camera Button Icon
cam_img = customtkinter.CTkImage(light_image=Image.open(os.path.join('assets', "camera_light.png")),
                                 dark_image=Image.open(os.path.join('assets', "camera_dark.png")))

text_img = customtkinter.CTkImage(light_image=Image.open(os.path.join('assets', "text-light.ico")),
                                  dark_image=Image.open(os.path.join('assets', "text-dark.ico")))

sound_img = customtkinter.CTkImage(light_image=Image.open(os.path.join('assets', "speaking-light.ico")),
                                   dark_image=Image.open(os.path.join('assets', "speaking-dark.ico")))

# Function To Set Dark Theme
def dark():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    theme.configure(image=img_dark, bg="#242424")
    select_label.configure(bg="#242424", fg='#ebebeb')
    img_capture.configure(hover_color="#242424")


# Function To Set light Theme
def light():
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("blue")
    theme.configure(image=img_light, bg='#ebebeb', activebackground='#ebebeb')
    select_label.configure(bg='#ebebeb', fg="#242424")
    img_capture.configure(hover_color="#ebebeb")


# Theme Switcher Function
def theme_switch():
    global dark_theme

    if dark_theme:
        light()
        dark_theme = False
    else:
        dark()
        dark_theme = True

def play_audio():
    global sound

    if sound:
        mixer.init() #Initialzing pyamge mixer
        mixer.music.load('test.mp3') #Loading Music File
        mixer.music.play() #Playing Music with Pygame
        sound = False
    else:
        mixer.music.stop()
        sound = True
# Open Camera Session Function
def open_camera():
    global opencv_image
    global captured_image

    # Capture the video frame by frame
    _, frame = vid.read()
    # Convert image from one color space to other
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Capture the latest frame and transform to image
    captured_image = Image.fromarray(opencv_image)
    # Resize the captured image
    captured_image = captured_image.resize((200, 200))
    # Convert captured image to photo-image
    photo_image = ImageTk.PhotoImage(image=captured_image)

    # Displaying photo-image in the label
    select_label.photo_image = photo_image

    # Configure image in the label
    select_label.configure(image=photo_image)

    # Repeat the same process after every 1 seconds
    select_label.after(1, open_camera)


# Close Camera Session Function
def close_camera():
    select_label.configure(text="\n\n\n\n\nSelect Input Way ", image="")
    vid.release()
    cv2.destroyAllWindows()


# Camera Switcher Function
def switch_camera():
    global cam

    if cam:

        open_camera()
        cam = False
    else:
        close_camera()
        cam = True


# Capture Frame From Camera And Pass It In Models To Make A Prediction
def capture():
    image = captured_image.copy()
    image.save("image.png")
    text_to_sound("image.png")
    data_label.configure(text=arabic_text)  # Set Text As Value Of Label

# Select File From PC Function
def from_file():
    global link
    link = askopenfilename()  # Initiate Link With Selected File Path
    if link:
        my_img = Image.open(link)  # Open Selected Image
        resized_img = my_img.resize((200, 200))  # Resize Image
        new_img = ImageTk.PhotoImage(resized_img)  # Convert Image to PhotoImage To Place It In CTK Window
        select_label.configure(image=new_img)  # Set Image As Value Of Label
        select_label.image = new_img
        text_to_sound(link)

def text_to_sound(link):
    global arabic_text
    if os.path.exists(link):
        try:
            arabic_text = image_to_text(link)  # Convert Image To Text
            with open('output.txt', 'w', encoding='utf-8') as file:
                file.write(arabic_text)
            text_to_speech(arabic_text)  # Convert Text To Speech
        except Exception as e:
            print(f"Error in text_to_sound: {e}")
    else:
        print("File does not exist.")

def set_text():
    data_label.configure(text=arabic_text)  # Set Text As Value Of Label

def on_closing():
    root.destroy() 
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=40)
root.rowconfigure(0,weight=10)
root.rowconfigure((1,2,3,4),weight=2)
# All Labels And Buttons
select_label = Label(root, font=('calibri', 11, 'bold'), text="\n\n\n\n\nSelect Input Way ", bg="#242424",
                     fg='#aaaaaa')
select_label.grid(row=0 ,column=0 )
data_label = customtkinter.CTkLabel(root, font=('arial', 12), text=" ", fg_color="transparent",
                                    justify='right')
data_label.grid(row=0 ,column=1 ,rowspan=4,sticky='nswe')
s_file = customtkinter.CTkButton(root, text='Browse', command=from_file, border_spacing=4)
s_file.grid(row=1 ,column=0 )
camera = customtkinter.CTkButton(root, text='Camera', command=switch_camera, border_spacing=4, width=110)
camera.grid(row=2 ,column=0 ,sticky="w",padx=110)
img_capture = customtkinter.CTkButton(root, image=cam_img, text=" ", command=capture, fg_color="transparent", width=40,
                                      hover_color="#242424")
img_capture.grid(row=2 ,column=0 ,sticky="e" ,padx=90)

text = customtkinter.CTkButton(root, image=text_img, text=" ",command=set_text,
                               hover_color="#242424",
                               fg_color="transparent", width=40)
text.grid(row=3 ,column=0 ,sticky="w",padx=105)
sound = customtkinter.CTkButton(root, image=sound_img, text=" ",command=play_audio, fg_color="transparent", width=40,
                                hover_color="#242424")
sound.grid(row=3 ,column=0 ,padx=150 ,sticky="e")
theme = Button(root, text='theme', command=theme_switch, bd=0, image=img_dark, bg="#242424")
theme.grid(row=4 ,column=1 ,sticky='se',padx=10,pady=10)
# Gui Main Function Call
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

