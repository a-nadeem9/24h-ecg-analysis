import os
import scipy.io as sio
import numpy as np
from scipy.signal import resample
import matplotlib.pyplot as plt

def load_mat_file(file_path):
    """
    Loads a .mat file and returns both 'day' and 'sleep' segments as 1D numpy arrays.
    """
    data = sio.loadmat(file_path)
    day_data = data['day'].flatten()
    sleep_data = data['sleep'].flatten()
    return day_data, sleep_data

def downsample_signal(signal, original_fs=250, target_fs=100):
    """
    Downsamples a signal from original_fs to target_fs using resampling.
    """
    num_samples = int(len(signal) * target_fs / original_fs)
    return resample(signal, num_samples)

# Specify the sample file path
folder_path = 'ecg_data'  
file_name = '19070921.mat' 
file_path = os.path.join(folder_path, file_name)

# Load the 'day' and 'sleep' segments from the file.
day_data, sleep_data = load_mat_file(file_path)

# Downsample both segments from 250 Hz to 100 Hz.
day_data_downsampled = downsample_signal(day_data, original_fs=250, target_fs=100)
sleep_data_downsampled = downsample_signal(sleep_data, original_fs=250, target_fs=100)

#  Print sample counts for verification.
print(f"File: {file_name}")
print(f"  Day segment: Original samples = {len(day_data)}, Downsampled samples = {len(day_data_downsampled)}")
print(f"  Sleep segment: Original samples = {len(sleep_data)}, Downsampled samples = {len(sleep_data_downsampled)}")

# Visualize a short segment (first 2000 samples) of the downsampled day data.
plt.figure(figsize=(12, 4))
plt.plot(day_data_downsampled[:2000])
plt.title("Downsampled Day ECG Data (First 2000 Samples at 100 Hz)")
plt.xlabel("Sample Number")
plt.ylabel("ECG Signal Value")
plt.show()

# Visualize a short segment (first 2000 samples) of the downsampled sleep data.
plt.figure(figsize=(12, 4))
plt.plot(sleep_data_downsampled[:2000])
plt.title("Downsampled Sleep ECG Data (First 2000 Samples at 100 Hz)")
plt.xlabel("Sample Number")
plt.ylabel("ECG Signal Value")
plt.show()
