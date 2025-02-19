import os
import time
import re

def wait_for_download_file(target_filename):
    download_dir = os.getcwd()
    while True:
        files = os.listdir(download_dir)
        if target_filename in files:
            break
        time.sleep(1)


def get_file_size_and_delete(filename):
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, filename)
    file_size_bytes = os.path.getsize(file_path)
    file_size_mb = file_size_bytes / (1024 * 1024)
    os.remove(file_path)
    return float(round(file_size_mb, 2))

def get_size(text):
    match = re.search(r'(\d+\.\d+)', text)
    return float(match.group(1))

