import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize lists to store data
data_x = []
data_y = []
data_z = []

# Establish serial connection
ser = serial.Serial(
    "COM3", 115200
)  # Replace 'COM3' with your microcontroller's serial port and baud rate


# Function to handle incoming data
def handle_data(data):
    data = (
        data.decode().strip()
    )  # Decode byte data and remove trailing newline/whitespace
    if data:  # Check if the received data is not empty
        try:
            # Assuming the format is "X:value, Y:value, Z:value"
            values = data.split(",")  # Split data into individual values
            x_value = int(values[0].split(":")[1])  # Extract X value
            y_value = int(values[1].split(":")[1])  # Extract Y value
            z_value = int(values[2].split(":")[1])  # Extract Z value

            # Store the received values
            data_x.append(x_value)
            data_y.append(y_value)
            data_z.append(z_value)
        except (ValueError, IndexError):
            pass  # Ignore invalid data or index errors


# Update function for the animation
def update(frame):
    if ser.in_waiting > 0:
        data = ser.readline()  # Read data from the serial port
        handle_data(data)  # Handle the received data

        # Plot the received data
        plt.cla()  # Clear the previous plot
        plt.plot(data_x, label="X")  # Plot X values
        plt.plot(data_y, label="Y")  # Plot Y values
        plt.plot(data_z, label="Z")  # Plot Z values
        plt.xlabel("Data Point")
        plt.ylabel("Value")
        plt.title("Real-time Data Plot")
        plt.legend()  # Show legend


# Set up the animation
ani = FuncAnimation(plt.gcf(), update, interval=100)  # Update plot every 100ms

plt.show()  # Display the animated plot

# Close the serial connection (not reached in this example)
ser.close()
