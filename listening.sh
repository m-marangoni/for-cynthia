#!/bin/bash

# Define the path to index.html
INDEX_HTML="/path/to/index.html"

# Function to open index.html
open_index_html() {
    xdg-open "$INDEX_HTML"
}

# Loop to continuously listen to USB events
while true; do
    # Monitor USB events
    udevadm monitor --environment --subsystem-match=usb | \
    while read -r line; do
        # Check if the line contains information about the USB device being added
        if [[ $line == *"ACTION=add"* ]]; then
            # Open index.html when a USB device is connected
            open_index_html
        fi
    done
done
