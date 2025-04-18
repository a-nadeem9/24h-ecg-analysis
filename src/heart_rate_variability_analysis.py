'''
Objective: Calculate HRV metrics for daytime and nighttime recordings.

1. Detect R-peaks in the ECG data using NeuroKit2.
2. Calculate HRV metrics for both daytime and nighttime segments.
  -- RMSSD, SDNN.
3. Compare metrics between daytime and nighttime segments.

'''

import neurokit2 as nk
import numpy as np

def extract_nn_intervals(ecg_signal, sampling_rate):
    #Clean & find peaks
    ecg_cleaned = nk.ecg_clean(ecg_signal, sampling_rate=sampling_rate)
    _, info = nk.ecg_peaks(ecg_cleaned, sampling_rate=sampling_rate)
    rpeaks = info["ECG_R_Peaks"]

    #Convert sample indices to times (s)
    peak_times = np.array(rpeaks) / sampling_rate

    #Compute successive R–R intervals (ms)
    rr_intervals = np.diff(peak_times) * 1000  # ms
    return rr_intervals

# Compute SDNN and RMSSD
def compute_hrv(nn_intervals):
    sdnn  = np.std(nn_intervals, ddof=1)
    rmssd = np.sqrt(np.mean(np.diff(nn_intervals)**2))
    return sdnn, rmssd