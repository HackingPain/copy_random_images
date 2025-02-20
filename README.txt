# Random Image Copier with GUI

This program randomly selects images from a source folder and copies them to a destination folder based on a user-specified percentage. It uses perceptual image hashing to avoid duplicates and features a simple Tkinter-based GUI.

---

## Features

- Select source and destination folders with file dialogs.
- Input the percentage of images to copy.
- Avoid duplicate or similar images using perceptual hashing.
- Randomizes image selection.
- Easy-to-use graphical interface.
- Option to package as an executable with PyInstaller.

---

## Requirements

- Python 3.x
- Tkinter (bundled with Python)
- Pillow  
- imagehash

---

## Installation

1. **Install Python 3.x** if you haven’t already.

2. **Install required packages** using pip:

   ```
   pip install Pillow imagehash
   ```

---

## Usage

1. **Run the script:**

   ```
   python your_script.py
   ```

2. **Use the GUI to:**
   - Select your source folder.
   - Select your destination folder.
   - Enter the percentage of images to copy.
   - Click the **Run** button to start copying.

---

## Creating an Executable

1. **Install PyInstaller:**

   ```
   pip install pyinstaller
   ```

2. **Navigate to the script’s directory** in your command prompt or terminal.

3. **Run PyInstaller:**

   ```
   pyinstaller --onefile your_script.py
   ```

4. **Find the executable** in the generated "dist" folder.

---

## References

(Python Software Foundation, n.d.)  
(Pillow, n.d.)  
(Buchner, n.d.)  
(PyInstaller, n.d.)

---

Python Software Foundation. (n.d.). *tkinter — Python interface to Tcl/Tk*. Retrieved from https://docs.python.org/3/library/tkinter.html

Pillow. (n.d.). *Pillow documentation*. Retrieved from https://pillow.readthedocs.io/

Buchner, J. (n.d.). *ImageHash*. Retrieved from https://github.com/JohannesBuchner/imagehash

PyInstaller. (n.d.). *PyInstaller documentation*. Retrieved from https://pyinstaller.org/