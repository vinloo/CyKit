<img src="https://raw.githubusercontent.com/CymatiCorp/CyKit/git-images/Images/CyKIT-1.png" width=34% height=34%  />


CyKIT 3.0 for Python 3.x (Linux)
=
`python cykit-linux.py` (with udev rules added)

`sudo python cykit-linux.py` (root permissions, without udev rules)

 ## Adding udev rules
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

### Troubleshooting
Verify cykit rules were read properly with the command:

`udevadm test /`

CyKIT 3.0 for Python 3.7.x (Windows)
=

Last Updated: [ December 27, 2018 - 1:00pm ]

Language Support (Python 3.x)
----------------
```

 Supported Python 3 Versions
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

Python 3.4.x  (32-bit or 64-bit)
Python 3.6.x  (32-bit or 64-bit) 
Python 3.7.x  (32-bit or 64-bit) 
Python 3.8.x  (32-bit or 64-bit) 
Python 3.9.x  (32-bit or 64-bit)

Latest Python Build: Python 3.9.5

Python 2.7.6 support will now be limited.
Python 3+ will be the focus. (Please upgrade accordingly.)

```

Headset Support
----------------
Does not currently work with Epoc-X  <br>
See Discord for details about Flex. 

Program Flowchart
-------------------

<img src="https://raw.githubusercontent.com/CymatiCorp/CyKit/git-images/Images/CyKIT-Flowchart.png" />
(MATLAB/Unity3D plugins have been created, but currently not included in repository) <br><br>

Browser Interface
-------------------

<img src="https://raw.githubusercontent.com/CymatiCorp/CyKit/git-images/Images/CyKIT-Preview.png" />

Documentation
-------------------
```
Introduction
```
* [CyKIT 3.0 (wikipage)](https://github.com/CymatiCorp/CyKit/wiki/CyKIT-3.0-Documentation)
```
Software (How To)
```
* [How to Install CyKIT](https://github.com/CymatiCorp/CyKit/wiki/How-to-Install-CyKIT)
* [How to Stream Data to OpenViBE](https://github.com/CymatiCorp/CyKit/wiki/How-to-Stream-Data-to-OpenViBE)
* [How to Pair USB device](https://github.com/CymatiCorp/CyKit/wiki/How-to-Pair-USB-device)
* [How to Change EPOC+ hertz modes](https://github.com/CymatiCorp/CyKit/wiki//How-to-Change-EPOC(plus)--modes)  


Communication
-
Chat Discussion: https://discordapp.com/invite/gTYNWc7 <br>
(Do not need discord app, just click for browser chat)

Version History
-
Deprecated CyKIT versions can be found here: <br>
[(CyKIT Version History)](https://github.com/CymatiCorp/CyKit/tree/git-images/History/) <br>

```
CyKIT v1.0 python 2.7.6 (2014)
CyKIT v1.0 python 3.3.x (2015)
CyKIT v2.0 Python 2.7.6 (2018.Jan.29)
```

Documentation
-

[Bluetooth Development Documentation](https://github.com/CymatiCorp/CyKit/blob/git-images/Documentation/Bluetooth_Development-Epoc.pdf)


<br><br>
