from data_preprocessing import load_mat_file, downsample_ecg
from visualization import plot_ecg_segment
from config import file_path
import matplotlib.pyplot as plt
import pandas as pd
from heart_rate_variability_analysis import extract_nn_intervals, compute_hrv, compare_hrv

#-------------------
# Data Preprocessing
#-------------------

# segmnet the data into 'day' and 'sleep' segments from the .mat file
day_data, sleep_data = load_mat_file(file_path)

# Downsample both segments from 250 Hz to 100 Hz.
day_data_downsampled = downsample_ecg(day_data, original_rate=250, target_rate=100)
sleep_data_downsampled = downsample_ecg(sleep_data, original_rate=250, target_rate=100)

#  Print smple counts for verification.
print(f"Day segment: Original samples = {len(day_data)}, Downsampled samples = {len(day_data_downsampled)}")
print(f"Sleep segment: Original samples = {len(sleep_data)}, Downsampled samples = {len(sleep_data_downsampled)}")

#---------------
# Visualization
#---------------

# Plotting the first 2000 samples of the original and downsampled data
plot_ecg_segment(day_data, 250, num_samples=2000, label='Day')
plot_ecg_segment(sleep_data, 250, num_samples=2000, label='Sleep')

plot_ecg_segment(day_data_downsampled, 100, num_samples=2000, label='Downsampled_Day')
plot_ecg_segment(sleep_data_downsampled, 100, num_samples=2000, label='Downsampled_Sleep')

#---------------------------
# Heart Variability Analysis
#---------------------------

#R-peak detection 
nn_day   = extract_nn_intervals(day_data_downsampled,   sampling_rate=100)
nn_night = extract_nn_intervals(sleep_data_downsampled, sampling_rate=100)

#compute HRV metrics
sdnn_day,   rmssd_day   = compute_hrv(nn_day)
sdnn_night, rmssd_night = compute_hrv(nn_night)

# Print the results
results = pd.DataFrame({
    "SDNN_ms": [sdnn_day, sdnn_night],
    "RMSSD_ms": [rmssd_day, rmssd_night]
}, index=["Day", "Night"])

print("\nHRV Metrics:")
print(results)

#plot comparison of HRV metrics
results.plot.bar(rot=0)
plt.ylabel("ms")
plt.title("SDNN and RMSSD: Day vs. Night")
plt.tight_layout()
plt.show()

# compare rr-intervals
compare_hrv(nn_day, nn_night)

#-----------------------
# Arrhythmia Detection
#-----------------------