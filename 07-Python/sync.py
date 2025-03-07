import os 
import shutil
import time

def sync_files(src_folder, dest_folder):
    # Check if the source and destination folders exist
    if not os.path.exists(src_folder):
        print(f"Source folder does not exist: {src_folder}")
        return
    if not os.path.exists(dest_folder):
        print(f"Destination folder does not exist: {dest_folder}")
        return

    # List all files in the source folder
    try:
        src_files = set(os.listdir(src_folder))
    except Exception as e:
        print(f"Error listing files in source folder: {e}")
        return

    # List all files in the destination folder
    try:
        dest_files = set(os.listdir(dest_folder))
    except Exception as e:
        print(f"Error listing files in destination folder: {e}")
        return

    # Iterate over the files in the source folder
    for file in src_files:
        # Check if the file is not in the destination folder
        if file not in dest_files:
            src_path = os.path.join(src_folder, file)
            dest_path = os.path.join(dest_folder, file)

            # Copy the file from source to destination
            if os.path.isfile(src_path):  # Ensure it's a file and not a directory
                shutil.copy(src_path, dest_path)
                print(f"File copied: {file}")
            else:
                print(f"Skipping directory (not a file): {file}")

def auto_sync(src_folder, dest_folder, interval_minutes=5):
    while True:
        print("Starting synchronization...")
        sync_files(src_folder, dest_folder)
        print(f"Synchronization completed. Waiting for {interval_minutes} minutes...")
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    source_directory = r"L:\Reports-PDF-Sync"  # Replace with your source folder path
    destination_directory = r"I:\Laboratory\MedChem\07_Projects\03_PIP5K1A\04_Synthesis\LC-MS\Reports_LCMS"  # Replace with your destination folder path
    interval_minutes = 5  # Adjust this value to set the interval (in minutes)

    # Start the automatic synchronization process
    auto_sync(source_directory, destination_directory, interval_minutes)
