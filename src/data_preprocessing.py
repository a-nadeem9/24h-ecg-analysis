'''
Objective: Prepare the raw ECG data for analysis.

1. Use scipy to read the raw ECG data from the .mat file.
2. Downsample the data from 250Hz to 100Hz.
3. Segment Day and night recordings for HRV analysis.

'''

import os
import scipy.io as sio
import numpy as np
from scipy.signal import resample
import matplotlib.pyplot as plt

# reading .mat file with scipy

def load_mat_file(file_path):
    """
    Loads a .mat file and returns both 'day' and 'sleep' segments as 1D numpy arrays.
    """
    data = sio.loadmat(file_path)
    ecg_day = data['day'].flatten()
    ecg_night = data['sleep'].flatten()
    return ecg_day, ecg_night

# downsample the data from 250Hz to 100Hz

def downsample_ecg(ecg_data, original_rate=250, target_rate=100):
    """
    Downsamples the ECG data from original_rate to target_rate.
    """
    num_samples = int(len(ecg_data) * target_rate / original_rate)
    downsampled_ecg = resample(ecg_data, num_samples)
    return downsampled_ecg