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

def plot_rr_24h(rr_times, rr_intervals, label="Full 24h", anomaly_thresholds=(500, 1200)):
    plt.figure(figsize=(14, 5))

    # Main RR plot
    plt.plot(rr_times, rr_intervals, color="steelblue", linewidth=0.6, label="RR Intervals")

    # Optional: clean anomaly markers
    short_rr = rr_intervals < anomaly_thresholds[0]
    long_rr = rr_intervals > anomaly_thresholds[1]

    if short_rr.any():
        plt.scatter(rr_times[short_rr], rr_intervals[short_rr], color="crimson", s=10, label="Short RR (<500 ms)")
    if long_rr.any():
        plt.scatter(rr_times[long_rr], rr_intervals[long_rr], color="darkorange", s=10, label="Long RR (>1200 ms)")

    plt.title(f"RR Intervals Over Time – {label}")
    plt.xlabel("Time (s)")
    plt.ylabel("RR Interval (ms)")
    plt.grid(True, linestyle="--", linewidth=0.4)
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.show()

