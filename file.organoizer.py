# os      → finds/checks files and folders
# shutil  → moves the files
print("===== FILE ORGANIZER =====") 
import os 
import shutil 
folder_path = input("Enter your folder path: ") 
# listdir → lists the contents of a directory (folder) 
file = os.listdir(folder_path) 
for files in file: 
    if os.path.isfile(os.path.join(folder_path, files)): 
        filename, extension = os.path.splitext(files) 
        folders_to_skip = ["Images", "Document", "Music", "Video", "Python", "Other"] 
        if files in folders_to_skip: 
            # Skip this item and go to the next item."
            continue 
        # IF the file I'm currently looking at is MY Python file → SKIP IT.
        if files == os.path.basename(__file__):
            # file.organoizer.py tell only this basename 
            continue
         # Skip this item and go to the next item." 
        match extension.lower(): 
        # match extension: 
            case ".jpg" | ".jpeg" | ".png" | ".gif": 
                # Create Images folder if it does not exist 
                os.makedirs(os.path.join(folder_path, "Images"), exist_ok=True)  
                # Move file to Images folder 
                destination = os.path.join(folder_path, "Images", files)
                if os.path.exists(destination):
                    continue
# The first part is where the file currently is and The second part is where you want it to go:
# shutill is used to move the files into the folder
                shutil.move(os.path.join(folder_path, files), os.path.join(folder_path, "Images")) 
                print(files, "Images") 
            case ".pdf" | ".docx" | ".txt" | ".xlsx": 
                os.makedirs(os.path.join(folder_path, "Document"), exist_ok=True) 
                destination = os.path.join(folder_path, "Document", files)
                if os.path.exists(destination):
                    continue
                shutil.move(os.path.join(folder_path, files), os.path.join(folder_path, "Document")) 
                print(files, "Document") 
            case ".mp3" | ".wav": 
                os.makedirs(os.path.join(folder_path, "Music"), exist_ok=True) 
                destination = os.path.join(folder_path, "Music", files)
                if os.path.exists(destination):
                    continue
                shutil.move(os.path.join(folder_path, files), os.path.join(folder_path, "Music")) 
                print(files, "Music") 
            case ".mp4" | ".mkv" | ".mov": 
                os.makedirs(os.path.join(folder_path, "Video"), exist_ok=True) 
                destination = os.path.join(folder_path, "Video", files)
                if os.path.exists(destination):
                    continue
                shutil.move(os.path.join(folder_path, files), os.path.join(folder_path, "Video")) 
                print(files, "Video") 
            case ".py": 
                os.makedirs(os.path.join(folder_path, "Python"), exist_ok=True) 
                destination = os.path.join(folder_path, "Python", files)
                if os.path.exists(destination):
                    continue
                shutil.move(os.path.join(folder_path, files), os.path.join(folder_path, "Python")) 
                print(files, "Python") 
            case _: 
                os.makedirs(os.path.join(folder_path, "Other"), exist_ok=True) 
                destination = os.path.join(folder_path, "Other", files)
                if os.path.exists(destination):
                    continue
                shutil.move(os.path.join(folder_path, files), os.path.join(folder_path, "Other")) 
                print(files, "Other") 
print() 
print("===== ORGANIZATION COMPLETE =====") 
print("All files have been organized successfully!")


          

         



