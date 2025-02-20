import os
import shutil
import random
import hashlib
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from PIL import Image
import imagehash

def get_image_files(folder):
    # List image files by checking common extensions.
    image_files = []
    for file in os.listdir(folder):
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_files.append(os.path.join(folder, file))
    return image_files

def calculate_image_hash(image_path):
    # Compute the perceptual hash of an image.
    with Image.open(image_path) as img:
        return str(imagehash.average_hash(img))

def copy_images_randomly(src_folder, dest_folder, percentage):
    # Create destination folder if it doesn't exist.
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    image_files = get_image_files(src_folder)
    total_images = len(image_files)
    num_to_copy = int(total_images * (percentage / 100))

    # Randomize the order.
    random.shuffle(image_files)

    copied_hashes = set()
    copied_images = 0

    for image_file in image_files:
        if copied_images >= num_to_copy:
            break

        img_hash = calculate_image_hash(image_file)

        # Copy image if its hash is new.
        if img_hash not in copied_hashes:
            shutil.copy(image_file, dest_folder)
            copied_hashes.add(img_hash)
            copied_images += 1

    return copied_images

def browse_source():
    folder = filedialog.askdirectory(title="Select Source Folder")
    if folder:
        src_entry.delete(0, "end")
        src_entry.insert(0, folder)

def browse_destination():
    folder = filedialog.askdirectory(title="Select Destination Folder")
    if folder:
        dest_entry.delete(0, "end")
        dest_entry.insert(0, folder)

def run_copy():
    src_folder = src_entry.get()
    dest_folder = dest_entry.get()
    try:
        percentage = float(percentage_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Percentage must be a number.")
        return

    if not os.path.exists(src_folder):
        messagebox.showerror("Error", "Source folder does not exist.")
        return

    copied_count = copy_images_randomly(src_folder, dest_folder, percentage)
    messagebox.showinfo("Done", f"Copied {copied_count} images to:\n{dest_folder}")

# Set up the GUI.
root = Tk()
root.title("Random Image Copier")

# Source folder input.
Label(root, text="Source Folder:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
src_entry = Entry(root, width=50)
src_entry.grid(row=0, column=1, padx=5, pady=5)
Button(root, text="Browse", command=browse_source).grid(row=0, column=2, padx=5, pady=5)

# Destination folder input.
Label(root, text="Destination Folder:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
dest_entry = Entry(root, width=50)
dest_entry.grid(row=1, column=1, padx=5, pady=5)
Button(root, text="Browse", command=browse_destination).grid(row=1, column=2, padx=5, pady=5)

# Percentage input.
Label(root, text="Percentage to Copy:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
percentage_entry = Entry(root, width=10)
percentage_entry.insert(0, "30")
percentage_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Run button.
Button(root, text="Run", command=run_copy).grid(row=3, column=1, padx=5, pady=15)

root.mainloop()
