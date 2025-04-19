'''
Objective: Calculate HRV metrics for daytime and nighttime recordings.

1. Detect R-peaks in the ECG data using NeuroKit2.
2. Calculate HRV metrics for both daytime and nighttime segments.
  -- RMSSD, SDNN.
3. Compare metrics between daytime and nighttime segments.

'''

import neurokit2 as nk
import numpy as np

def extract_nn_intervals(ecg_signal, sampling_rate, return_timestamps=False):
    ecg_cleaned = nk.ecg_clean(ecg_signal, sampling_rate=sampling_rate)
    _, info = nk.ecg_peaks(ecg_cleaned, sampling_rate=sampling_rate)
    rpeaks = info["ECG_R_Peaks"]
    
    rpeak_times = np.array(rpeaks) / sampling_rate
    rr_intervals = np.diff(rpeak_times) * 1000  # ms
    rr_times = rpeak_times[1:]  # timestamps of RR intervals

    # Filter out abnormal values
    mask = (rr_intervals > 300) & (rr_intervals < 2000)
    rr_clean = rr_intervals[mask]
    rr_times_clean = rr_times[mask]

    if return_timestamps:
        return rr_clean, rr_times_clean
    else:
        return rr_clean



# Compute SDNN and RMSSD
def compute_hrv(nn_intervals):
    """
    Compute HRV metrics from NN intervals.
    Returns:
        sdnn  (float): Standard deviation of NN intervals in ms.
        rmssd (float): Root mean square of successive differences in ms.
    """
    sdnn  = np.std(nn_intervals, ddof=1)
    rmssd = np.sqrt(np.mean(np.diff(nn_intervals)**2))
    return sdnn, rmssd

