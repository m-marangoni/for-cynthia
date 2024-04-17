import usb.core
import usb.util
import time
import webbrowser

# Vendor and product IDs of the USB device
VENDOR_ID = 0x1234  # Replace with your device's vendor ID
PRODUCT_ID = 0x5678  # Replace with your device's product ID

# Function to check if the USB device is connected
def is_device_connected():
    device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
    return device is not None

# Main loop to continuously monitor USB connections
while True:
    if is_device_connected():
        print("USB device connected")

# Open index.html in a web browser
webbrowser.open("/home/pi/Desktop/for-cynthia-main/index.html")
        # Perform your desired action here
        # For example, open index.html in a web browser
        # You can use webbrowser.open("file:///path/to/index.html")
        break  # Break out of the loop once action is performed
    else:
        print("Waiting for USB device...")
        time.sleep(1)  # Wait for 1 second before checking again
