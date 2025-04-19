import os

folder_path = 'ecg_data'  
file_name = '19070921.mat' 
file_path = os.path.join(folder_path, file_name)
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found at {file_path}")
