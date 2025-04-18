from data_preprocessing import load_mat_file, downsample_ecg
from visualization import plot_ecg_segment
from config import file_path

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


#-----------------------
# Arrhythmia Detection
#-----------------------