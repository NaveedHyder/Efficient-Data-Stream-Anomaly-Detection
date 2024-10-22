import numpy as np  # Handle mathematical operations, generate sine wave, and add noise to the wave function
import random  # Randomly inject anomalies to the stream
import matplotlib.pyplot as plt  # Plot the data stream in real-time
from matplotlib.animation import FuncAnimation  # Create animations to show the continuous data stream

# This function simulates a data stream with occasional anomalies
def data_stream_simulator():
    t = 0
    while True:  # Simulate an infinite real-time data stream
        seasonal = np.sin(2 * np.pi * t / 50)  # Sinusoidal pattern to simulate seasonality
        noise = np.random.normal(0, 0.5)  # Add random noise around the seasonal data
        value = seasonal + noise  # The final value is the sum of the sine wave and noise
        if random.random() < 0.01:  # 10% chance of anomaly
            anomaly = random.uniform(5, 10)  # Inject a random anomaly between 5 and 10
            value += anomaly  # Add the anomaly to the current value
        yield t, value  # Yield both the current time step and value
        t += 1  # Increment time to simulate a continuous data stream

# This function detects anomalies in the data stream using the exponentially Weighted Moving Average (EWMA) algorithm
def anomaly_detector(data_stream, lambda_=0.7, threshold=1.0):
    ewma = None
    variance = 0  # Initialize variance to 0
    for t, value in data_stream:
        if ewma is None:
            ewma = value  # Initialize EWMA with the first value
            variance = 0  # Initialize variance as 0
        else:
            ewma_old = ewma
            ewma = lambda_ * value + (1 - lambda_) * ewma_old  # Update EWMA
            variance = lambda_ * (value - ewma) ** 2 + (1 - lambda_) * variance  # Update variance
        
        std_dev = np.sqrt(variance)
        deviation = abs(value - ewma)
        
        # Detect anomalies based on deviation from EWMA
        if std_dev > 1e-6 and deviation > threshold * std_dev:  # Avoid division by zero for very small std dev
            print(f"Anomaly detected at time step {t}, value: {value:.2f}")
        
        yield t, value  # Yield the time step and value for visualization

# This function visualizes the data stream
def visualize():
    data_stream = data_stream_simulator()  # Start the data stream
    fig, ax = plt.subplots()  # Create the figure and axis for plotting
    
    xs = []  # X-axis (time steps)
    ys = []  # Y-axis (data stream values)

    # Plot object for the data stream
    line, = ax.plot([], [], 'b-', label='Data Stream')  # Blue line for the data stream

    def init():
        ax.set_xlim(0, 100)  # X-axis limit
        ax.set_ylim(-5, 15)  # Y-axis limit
        ax.set_title('Real-Time Data Stream')
        ax.set_xlabel('Time Step')
        ax.set_ylabel('Value')
        return line,

    def update(frame):
        t, value = frame  # Get data from the anomaly detector
        xs.append(t)  # Time step
        ys.append(value)  # Data value

        # Update the main data stream line
        line.set_data(xs, ys)

        # Adjust x-axis limits to keep the plot moving
        if len(xs) > 100:
            ax.set_xlim(len(xs) - 100, len(xs))

        # Adjust y-axis limits dynamically based on data
        y_min = min(ys[-100:])
        y_max = max(ys[-100:])
        ax.set_ylim(y_min - 1, y_max + 1)

        return line,

    # Create the animation, updating the data stream without marking anomalies
    ani = FuncAnimation(fig, update, frames=anomaly_detector(data_stream, lambda_=0.7, threshold=1.0), init_func=init, blit=False)
    plt.show()

# Main execution point
if __name__ == "__main__":
    visualize()  # Start visualization