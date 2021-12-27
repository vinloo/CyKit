# CyKIT 3.0 for Linux
> Currently only works with Python 3.7.x and 3.10.x

> Only tested on Ubuntu 20.04 LTS with the Emotiv Insight

This is a stripped down fork of [CymatiCorp/CyKit](https://github.com/CymatiCorp/CyKit) ported to Linux.  

## Running
---

Since this application needs to access your machine's USB ports, you either have to run it with root permissions or add udev rules.

### Running as root
`sudo python CyKIT.py`

### Adding udev rules

`sudo nano /etc/udev/rules.d/99-cykit.rules `

Save the following to file:
```
ACTION=="add", \
SUBSYSTEM="usb", \
ATTRS{idVendor}=="1234", \
ATTRS{idProduct}=="ed02", \
MODE="0666"
```

Then reload udev rules:

`sudo udevadm control --reload-rules && sudo udevadm trigger`

Next:
 * Remove USB device.
 * Insert USB device.
 * Run python cykit-linux.py


Verify cykit rules were read properly with the command:

`udevadm test /`

## Troubleshooting
---
### How to solve `KeyError: 'Sec-WebSocket-Key'`
Run the program with the `+generic` flag as such: `python CyKIT.py 127.0.0.1 54123 4 +generic` (use sudo if not using udev rules).

### How to solve `TypeError: 'type' object is not iterable`
An unfixed bug causes the program to crash when the TCP server recieves data more than once. So in your TCP client, when connecting to the server, only send data once to trigger the data stream. (Example TCP client coming soon!)

