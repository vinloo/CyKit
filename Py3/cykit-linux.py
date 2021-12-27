#  December.27.2021
#  cykit-linux.py
# -----------------
# Tested with Ubuntu 20.04.3 LTS, Python 3.8.8

import sys
import usb
import usb.core
from usb.backend import libusb1          # Requires libusb-1.0.so libraries.


def detach_driver(device):
    if device.is_kernel_driver_active(0):
        device.detach_kernel_driver(0)
    elif device.is_kernel_driver_active(1):
        device.detach_kernel_driver(1)


b = libusb1.get_backend()
device = usb.core.find(idVendor=0x1234)  # Find device.

if device is None:
    sys.exit("No device found!")

detach_driver(device)
headset_status = device.ctrl_transfer(0xA1, 0x01, 0x0300, 0, 31)  # Interface 0

# Lists firmwares, device id and 14/16 bit and hz mode.
print(str(headset_status))

read = ""
while read != None:
    detach_driver(device)
    read = device.read(0x82, 32, 100)
    print(str(read))

# Cleanup to reattach driver.
detach_driver(device)
