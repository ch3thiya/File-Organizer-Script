# File Organizer

This Python script automatically organizes files from your Downloads folder into categorized directories based on their file types. It categorizes files into Images, Videos, Audio, and Documents, and moves them to the corresponding folders in your system.

---

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Process](#process)
4. [Usage](#usage)
5. [License](#license)
6. [Acknowledgments](#acknowledgments)

---

## Features
- **Identifies and organizes files based on their extensions.**
- **Creates necessary directories if they do not exist.**
- **Logs every file movement for tracking.**
  
---

## Installation
1. **Clone this repository or download the script.**

---

## Process
1. **Directories Setup:**
   - The script checks if the target directories (Documents, Music, Pictures, Videos) exist under `C:/Users/{your-name}/`, and creates them if they don't.

2. **File Detection:**
   - It scans the `C:/Users/{your-name}/Downloads` folder and lists all files.

3. **File Categorization:**
   - Files are categorized based on their extensions:
     - **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
     - **Videos:** `.mp4`, `.avi`, `.mkv`, `.mov`
     - **Audio:** `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.m4a`, `.wma`, `.alac`
     - **Documents:** Any other file extensions.

4. **File Movement:**
   - The script copies files to their respective directories and logs the activity.

---

## Usage
1. **Edit paths (Optional):**
   - If your system username or folder structure differs or want to organize files somewhere else, edit the following paths in the script accordingly:
   
   ```bash
    path = "C:/Users/{your-name}/Downloads"
    documentsPath = "C:/Users/{your-name}/Documents/fileorg"
    musicPath = "C:/Users/{your-name}/Music/fileorg"
    imagesPath = "C:/Users/{your-name}/Pictures/fileorg"
    videosPath = "C:/Users/{your-name}/Videos/fileorg"
   ```
   
3. **Run the script:**
   
   ```bash
   python script.py
   ```
   
4. **Check the logs:**
   - File movements are logged in file_organizer.log located in the same directory as the script.

  
**Example Output**
```bash
   photo.jpg is an Image.
   video.mp4 is a Video.
   song.mp3 is an Audio.
   document.pdf is a Document.
```

**Logging Example**
```bash
   2024-02-05 10:30:12,345 - Moved: photo.jpg to C:/Users/{your-name}/Pictures/fileorg/photo.jpg
   2024-02-05 10:30:12,346 - Moved: video.mp4 to C:/Users/{your-name}/Videos/fileorg/video.mp4
   2024-02-05 10:30:12,347 - Moved: song.mp3 to C:/Users/{your-name}a/Music/fileorg/song.mp3
   2024-02-05 10:30:12,348 - Moved: document.pdf to C:/Users/{your-name}/Documents/fileorg/document.pdf
```

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgments
* Inspired by various file organization scripts shared by developers on GitHub and Stack Overflow.
* Special thanks to the creators of the os, pathlib, shutil, and logging modules for making file handling and automation straightforward.

---


<p>
Last Updated: February 05, 2025
</p>
<br>
< Happy Coding />
<br>
<b>Chethiya Ravindranath<b>
<br>
<a href="https://www.linkedin.com/in/chethiya-ravindranath-64a1b5329/">Linkedin</a> | <a href="https://www.instagram.com/ch3thiya">Instagram</a>
</p>
