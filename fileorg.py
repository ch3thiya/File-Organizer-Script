import os
import pathlib
import shutil
import logging

logging.basicConfig(filename="file_organizer.log", level=logging.INFO, format='%(asctime)s - %(message)s')

available_files = []
path = "C:/Users/{your-name}/Downloads"
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
video_extensions = [".mp4", ".avi", ".mkv", ".mov"]
audio_extensions = [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma", ".alac"]

documentsPath = f"C:/Users/{your-name}/Documents/fileorg"
musicPath = f"C:/Users/{your-name}/Music/fileorg"
imagesPath = f"C:/Users/{your-name}/Pictures/fileorg"
videosPath = f"C:/Users/{your-name}/Videos/fileorg"

for dir_path in [documentsPath, musicPath, imagesPath, videosPath]:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

directory_list  = os.listdir(path)
for item in directory_list:
    if "." in item:
        available_files.append(item)

for file in available_files:
    sourcePath = f"C:/Users/{your-name}/Downloads/{file}"
    extension = pathlib.Path(file).suffix
    
    if extension in image_extensions:
        print(f"{file} is an Image.")
        shutil.copyfile(sourcePath, os.path.join(imagesPath, file))
        logging.info(f"Moved: {file} to {imagesPath}/{file}")

    elif extension in video_extensions:
        print(f"{file} is a Video.")
        shutil.copyfile(sourcePath, os.path.join(videosPath, file))
        logging.info(f"Moved: {file} to {videosPath}/{file}")

    elif extension in audio_extensions:
        print(f"{file} is an Audio.")
        shutil.copyfile(sourcePath, os.path.join(musicPath, file))
        logging.info(f"Moved: {file} to {musicPath}/{file}")
        
    else:
        print(f"{file} is a Document")
        shutil.copyfile(sourcePath, os.path.join(documentsPath, file))
        logging.info(f"Moved: {file} to {documentsPath}/{file}")
