import os
import shutil
import streamlit as st

# Function to organize files
def organize_files(directory):
    # Create a dictionary to hold file types and their corresponding folders
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Audio': ['.mp3', '.wav'],
        'Archives': ['.zip', '.tar', '.gz'],
    }

    # Create folders for each file type
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to their respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(filename.endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    moved = True
                    break
            if not moved:
                # Move to 'Others' if no type matches
                others_folder = os.path.join(directory, 'Others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, os.path.join(others_folder, filename))

# Streamlit UI
st.title("File Organizer")
st.write("Select a directory to organize files by type.")

# Directory input
directory = st.text_input("Directory Path", "")

if st.button("Organize Files"):
    if directory and os.path.exists(directory):
        organize_files(directory)
        st.success("Files organized successfully!")
    else:
        st.error("Please enter a valid directory path.")