from PIL import Image
import os
import shutil

def sort_images(source_folder, landscape_folder, portrait_folder):
    # Ensure destination folders exist
    if not os.path.exists(landscape_folder):
        os.makedirs(landscape_folder)
    if not os.path.exists(portrait_folder):
        os.makedirs(portrait_folder)

    # Loop through each image in the source folder
    for i in range(1, 24):
        file_name = f"photo{i}.jpg"
        file_path = os.path.join(source_folder, file_name).replace('\\', '/')
        print(file_path)
        if os.path.isfile(file_path):
            with Image.open(file_path) as img:
                # Check if the image is landscape or portraitcd 
                if img.width > img.height:
                    # Landscape
                    dest_path = os.path.join(landscape_folder, file_name)
                else:
                    # Portrait
                    dest_path = os.path.join(portrait_folder, file_name)

                # Copy the image to the appropriate folder
                shutil.copy(file_path, dest_path)

# Define your paths
source_folder = "./assets/Photos"
landscape_folder = "./assets/Photos/Landscape"
portrait_folder = "./assets/Photos/Portrait"

sort_images(source_folder, landscape_folder, portrait_folder)
