# 📁 File Organizer

A simple **Python File Organizer** that automatically organizes files into different folders based on their file extensions.

I made this project as a beginner Python project to practice working with files, folders, loops, conditions, and Python modules.

## ✨ Features

* Organizes images into the `Images` folder
* Organizes documents into the `Document` folder
* Organizes music into the `Music` folder
* Organizes videos into the `Video` folder
* Organizes Python files into the `Python` folder
* Places other file types into the `Other` folder
* Skips files that are already organized
* Skips the File Organizer Python program itself

## 🗂️ File Categories

| File Type                        | Folder   |
| -------------------------------- | -------- |
| `.jpg`, `.jpeg`, `.png`, `.gif`  | Images   |
| `.pdf`, `.docx`, `.txt`, `.xlsx` | Document |
| `.mp3`, `.wav`                   | Music    |
| `.mp4`, `.mkv`, `.mov`           | Video    |
| `.py`                            | Python   |
| Other extensions                 | Other    |

## 🛠️ Technologies Used

* Python
* `os` module
* `shutil` module
* `match-case`

## ▶️ How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open the Python file.
4. Run the program.
5. Enter the path of the folder you want to organize.

Example:

```text
Enter your folder path: E:\My Files
```

The program will automatically create the required folders and move the files into their correct categories.

## 📚 What I Learned

While making this project, I practiced:

* Using `os.listdir()`
* Checking files with `os.path.isfile()`
* Getting file extensions with `os.path.splitext()`
* Using `os.path.basename()`
* Creating folders with `os.makedirs()`
* Moving files with `shutil.move()`
* Using `for` loops
* Using `if` statements
* Using `match-case`
* Working with file paths
* Handling existing files and folders

## 🚀 Future Improvements

I would like to improve this project in the future by adding:

* More file extensions
* Better error handling
* A user-friendly interface
* Duplicate file handling
* More customizable folder categories

## 👩‍💻 About

This is one of my beginner Python projects. I built it to improve my Python programming skills and learn how Python can be used to automate everyday tasks.

---

