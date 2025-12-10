# Soundify - Arabic OCR & Text-to-Speech

**Soundify** is a Python desktop application that converts Arabic text from images into spoken audio. It offers two OCR recognition modes in a single unified interface:

1.  **Full Text (Tesseract)**: For recognizing sentences, paragraphs, or full pages of Arabic text
2.  **Character (CNN)**: For recognizing single Arabic characters using a custom-trained neural network

## Features

-   **Dual OCR Modes**: Switch between Tesseract (full text) and CNN (single character) recognition
-   **Image Input Options**:
    -   Live camera feed capture
    -   File upload from local storage
-   **Text-to-Speech**: Automatically converts recognized text to speech (MP3)
-   **Modern GUI**: Dark/Light theme toggle with customtkinter
-   **Robust Error Handling**: Gracefully handles missing dependencies

## Project Structure

-   `soundify.py`: Main application with unified Tesseract & CNN modes
-   `utils_tesseract.py`: Tesseract OCR integration functions
-   `utils_cnn.py`: CNN model prediction and character mapping
-   `model_training_notebook.ipynb`: Jupyter notebook for CNN model training
-   `model/arabic-OCR.h5`: Pre-trained CNN model (72MB)
-   `assets/`: GUI icons and images
-   `requirements.txt`: Python dependencies

## Installation

### Prerequisites

-   **Python 3.7+**
-   **Tesseract OCR** (Required for Full Text mode)
    -   Windows: Download from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
    -   Add Tesseract to your system PATH
    -   Install Arabic language data during setup

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/3bsalam-1/Arabic-OCR.git
    cd Arabic-OCR/Code
    ```

2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

    This will install:
    - `customtkinter` - Modern GUI framework
    - `opencv-python` - Camera and image processing
    - `Pillow` - Image manipulation
    - `pygame` - Audio playback
    - `pytesseract` - Tesseract OCR wrapper
    - `gTTS` - Google Text-to-Speech
    - `tensorflow` - CNN model (large package ~330MB)

3.  **Download the CNN Model** (Required for Character mode):
    - The pre-trained model file `arabic-OCR.h5` (72MB) is not included in the repository
    - Download it from: [Release Page](https://github.com/3bsalam-1/Arabic-OCR/releases) or contact the author
    - Place it in the `model/` directory: `Code/model/arabic-OCR.h5`
    - If you skip this step, only Tesseract mode will work

## Usage

### Running the Application

```bash
python soundify.py
```

### Mode Selection

Use the **mode switcher** at the bottom-left of the window:

-   **Full Text (Tesseract)**: Best for sentences, paragraphs, or documents
    -   Requires: Tesseract OCR installed on your system
    -   Use case: Reading full pages, signs, documents
    
-   **Character (CNN)**: Best for single Arabic characters
    -   Requires: Tensorflow (installed via requirements.txt)
    -   Use case: Individual letter recognition

### Controls

| Button | Function |
|--------|----------|
| **Browse** | Select an image file from your computer |
| **Camera** | Toggle live camera feed on/off |
| **📷 Icon** | Capture current camera frame |
| **🔊 Icon** | Play audio of recognized text |
| **📝 Icon** | Display recognized text on screen |
| **Theme** | Switch between Light/Dark mode |

### Workflow

1. Select your preferred mode (Tesseract or CNN)
2. Choose input method:
   - Click **Browse** to select an image file, OR
   - Click **Camera** to enable live feed, then click 📷 to capture
3. Click **🔊** to hear the text read aloud
4. Click **📝** to see the recognized text

## Troubleshooting

### "Tesseract is not installed or not found in PATH"
- Install Tesseract OCR from the link above
- Ensure it's added to your system PATH
- Restart your terminal/IDE after installation

### "CNN Model or Tensorflow not found"
- Run: `pip install tensorflow`
- Note: This is a large package (~330MB) and may take time to download

### Camera not working
- Ensure your camera is not being used by another application
- Check camera permissions in your system settings
- The app will show "Camera not accessible" if no camera is detected

### No audio playback
- Ensure `test.mp3` is being generated in the project directory
- Check your system audio settings
- Verify pygame is installed: `pip install pygame`

## Dependencies

All dependencies are listed in `requirements.txt`:

```
customtkinter
opencv-python
Pillow
pygame
pytesseract
gTTS
tensorflow
```

## Credits

**Author**: 3bsalam-1  
**Last Updated**: December 2025

---

