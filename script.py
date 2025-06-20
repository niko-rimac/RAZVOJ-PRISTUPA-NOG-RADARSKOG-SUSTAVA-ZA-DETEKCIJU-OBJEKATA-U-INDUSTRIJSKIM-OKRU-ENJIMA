#!/usr/bin/env python3
import pandas as pd
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

SAMPLING_FREQUENCY = 1000   # (Hz)
CSV_FILE_PATH = './samples/50cm/sample_6.csv'

def read_data_from_csv(file_path):
    try:
        df = pd.read_csv(file_path, header=None, usecols=[1])
        extracted_digits = df[1].str.extract('(\d+)', expand=False)
        sensor_data_series = pd.to_numeric(extracted_digits, errors='coerce')
        sensor_data_series = sensor_data_series.dropna()
        sensor_data = sensor_data_series.to_numpy()
        
        print(f"Successfully read {len(sensor_data)} data points from {file_path}.")
        return sensor_data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print("Please make sure the CSV file is in the same directory as the script.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def main():
    time_series_data = read_data_from_csv(CSV_FILE_PATH)

    if time_series_data is None:
        return 

    N = len(time_series_data)
    if N == 0:
        print("Error: The data file is empty.")
        return

    fft_raw = fft(time_series_data)
    
    fft_magnitude = 2.0/N * np.abs(fft_raw[0:N//2])
    
    fft_freq = fftfreq(N, 1 / SAMPLING_FREQUENCY)[:N//2]

    
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    time_axis = np.linspace(0, N / SAMPLING_FREQUENCY, N, endpoint=False)
    plt.plot(time_axis, time_series_data)
    plt.title("Raw Sensor Data (Time Domain)")
    plt.xlabel("Time (s)")
    plt.ylabel("ADC Value")
    plt.grid(True)

    plt.subplot(2, 1, 2) 
    plt.plot(fft_freq[1:], fft_magnitude[1:])
    plt.title("FFT Spectrum (Frequency Domain) - DC Component Excluded")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    
    plt.axvline(x=0, color='r', linestyle='--', linewidth=0.8, label='DC Component (0 Hz)')
    plt.legend()
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()