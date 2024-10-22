# Efficient Data Stream Anomaly Detection

## Project Overview
This project is part of the Graduate Software Engineer role application for Cobblestone Energy. It focuses on building an efficient Python script capable of detecting anomalies in a continuous data stream, which could represent metrics like financial transactions or system health data. The solution uses the **Exponentially Weighted Moving Average (EWMA)** algorithm for anomaly detection and provides real-time visualization of the data stream.

## Features
- **Real-time anomaly detection**: Detects deviations from normal patterns using the EWMA algorithm.
- **Dynamic visualization**: Displays the evolving data stream in real-time with Matplotlib.
- **Efficient algorithm**: Optimized for speed and simplicity, making it suitable for real-time systems.
  
## Algorithm Explanation
The anomaly detection algorithm is based on the **EWMA** method. EWMA tracks the expected trend in the data stream and adapts over time. The algorithm compares the current value to the expected value (EWMA), and if the deviation is significantly larger than a set threshold, it flags the value as an anomaly. The standard deviation of the data is used to determine the threshold for anomaly detection.

Key steps in the process:
1. Generate a data stream with sinusoidal behavior, random noise, and occasional anomalies.
2. Use the EWMA to calculate the expected behavior.
3. Detect anomalies based on deviation from the EWMA and the standard deviation.

## Requirements
Make sure to install the required Python packages before running the script.

Install dependencies using `pip`:

```bash
pip install -r requirements.txt
