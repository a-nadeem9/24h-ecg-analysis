import matplotlib.pyplot as plt

def plot_ecg_segment(ecg_data, fs, num_samples=2000, label=''):
    """
    Plots the first num_samples of the given ECG data.

    Parameters:
        ecg_data (array-like): 1D ECG data array.
        num_samples (int): Number of samples to plot.
        fs (int or float): Sampling rate in Hz, included in the title.
        label (str): Descriptor for the data (e.g., 'Day', 'Sleep').
    """
    plt.figure(figsize=(12, 4))
    plt.plot(ecg_data[:num_samples], linewidth=1)
    plt.title(f"{label} ECG Data (First {num_samples} Samples at {fs} Hz)")
    plt.xlabel("Sample Number")
    plt.ylabel("ECG Signal Value")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_rr_intervals_over_time(rr_intervals, rr_times, label="Segment"):
    plt.figure(figsize=(12, 4))
    plt.plot(rr_times, rr_intervals, marker='o', linestyle='-', alpha=0.7)
    plt.title(f"RR Intervals Over Time – {label}")
    plt.xlabel("Time (s)")
    plt.ylabel("RR Interval (ms)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

