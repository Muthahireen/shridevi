import os

# Define the desktop path (replace with your actual desktop path if needed)
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# Folder name (replace with your desired name)
main_folder_name = "My Organized Folder"

# Number of subfolders
num_subfolders = 10

# Create the main folder if it doesn't exist
main_folder_path = os.path.join(desktop_path, main_folder_name)
try:
    os.makedirs(main_folder_path)
except FileExistsError:
    print(f"Folder '{main_folder_name}' already exists on your desktop.")

# Create subfolders and files within the main folder
for i in range(1, num_subfolders + 1):
    subfolder_name = f"Subfolder {i}"
    subfolder_path = os.path.join(main_folder_path, subfolder_name)
    os.makedirs(subfolder_path, exist_ok=True)  # Handle existing subfolders gracefully

    # Create the file in each subfolder
    file_path = os.path.join(subfolder_path, "shridevi.py")
    with open(file_path, 'w') as f:
        f.write("# This is an empty shridevi.py file.\n")  # Add some content (optional)

print(f"Successfully created folder '{main_folder_name}' with {num_subfolders} subfolders and shridevi.py files on your desktop.")