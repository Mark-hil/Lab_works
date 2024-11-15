import os
import shutil
import requests
from datetime import datetime


first_name = "Mark-Hill"
last_name = "Ampomah"
directory_name = f"{first_name}_{last_name}"

if os.path.exists(directory_name):
    try:
        shutil.rmtree(directory_name)
        print(f"Directory '{directory_name}' has been removed successfully.")
    except Exception as e:
        print(f"Error: {e}")


download_folder = 'mark_hill'

# Create the directory if it doesn't exist
if not os.path.exists(download_folder):
    os.makedirs(download_folder)
    print(f"Directory: {download_folder} created.")
else:
    print(f"Directory: {download_folder} already exists.")

# Define the local file pat
local_file_path = os.path.join(download_folder, "mark_hill.txt")

# URL of the file you want to download and using `requests.get()` to fetch it and also Check the response status 
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"
response = requests.get(url)
if response.status_code == 200:
    with open(local_file_path, "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")

# Prompting the user for input and overwrite the downloaded file
user_input = input("Describe what you have learned so far in a sentence: ")
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")


with open(local_file_path, "w") as file:
    file.write(user_input + "\n")
    file.write(f"Last modified on: {current_time}")
    print("File successfully modified.")


# Displaying the Updated File Content
with open(local_file_path, "r") as file:
    print("\nYou Entered: ", end=' ')
    print(file.read())