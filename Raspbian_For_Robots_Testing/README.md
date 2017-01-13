# Utilities
Dexter Industries Utilities for Internal Use.


This is testing for Raspbian for Robots.


General Tests:  Run and Check for Errors
=====================================
- [ ] Is Minecraft Installed?
- [ ] Does it fit on a 4Gig Sandisk SD card?  
- [ ] Shellinabox - Login and test.  
- [ ] noVNC - Login and test.
- [ ] VNC Viewer - Login and test. Verify that cursor is all right
- [ ] Dexter Industries Update - Run the update once on Jessie.
- [ ] Dexter Industries Update - Run the update once on Wheezy.
- [ ] Scratch GUI - Run the Scratch GUI once.  
- [ ] Test change the hostname.
- [ ] Run as headless on a network.
- [ ] Run with an HDMI monitor, USB keyboard, USB mouse.
- [ ] Boot on the Pi B+
- [ ] Boot on the Pi 2
- [ ] Boot on the Pi 3

Desktop Tests:  Run These Programs to Make Sure They Work
=====================================
- [ ] Line Follower Calibration - verify files are saved in /home/pi/Dexter
- [ ] Test line follower in python and scratch
- [ ] IR Receiver Setup
- [ ] Test and Troubleshoot
- [ ] Backup Files

- [ ] Is all wifi information removed?
- [ ] Is the trash can emptied?
- [ ] Is the Desktop Version updated?  Is the date current?
- [ ] Are the serial lines on by default?
- [ ] Is the camera enabled?  Run `sudo raspistill -o 1.jpg`
- [ ] Is the recovery script in /home/pi directory there?
- [ ] Enable the IR receiver from *Advanced Communications Options* on the desktop and reboot
- [ ] Connect the IR receiver to the Serial port on the GoPiGo
- [ ] Run `sudo monit status` and check if di_ir_reader is running
- [ ] Run `ir_receiver_example.py` in /home/pi/Desktop/GoPiGo/Software/Python/ir_remote_control/gobox_ir_receiver_libs and press buttons on the remote and see if it works
- [ ] Run `GoPiGo_IR_Remote_Example.sb` for the IR receiver for scratch with GoPiGo

Branding:
=====================================
- [ ] Dexter industries Logo on Desktop.
- [ ] White Desktop Background.
- [ ] Small Dex logo in menu at top left (Jessie) (not for now)

Functional Testing:  Run the test with the hardware.
=====================================
- [ ] GrovePi -  Run the GrovePi Hardware Test - GrovePi/Software/Python/GrovePi_Hardware_Test.py
- [ ] GoPiGo - Run the test program from the Desktop GUI.
- [ ] BrickPi - Run the BrickPi Hardware Test - BrickPi_Python/Sensor_Examples/BrickPi_Hardware_Test.py
- [ ] Arduberry - Check that Arduino IDE is 1.6.0 and test that Serial Echo with Hellow world works
- [ ] Update the firmware of the GrovePi or GoPiGo to test AVRDude
- [ ] Run BrickPi Scratch Example Program
- [ ] Create new BrickPi Scratch program - example: broadcast MAE, broadcast MA200
- [ ] Run GrovePi Scratch Example Program
- [ ] Create new GrovePi Scratch program - 
- [ ] Run GoPiGo Scratch Example Program
- [ ] Create new GoPiGo Scratch Program - example: broadcast forward
- [ ] Run Spy vs Spi startup, test for success.  Connect jumpers to GPIO9 and GPIO11 and 3V3.  Connect I2C display to GrovePi Port.  If succesful, it should turn the display on and play a dialog.

Publishing Tasks for Raspbian for Robots
=====================================
- [ ] Change version number in Desktop/Version
- [ ] Generate MD5
- [ ] Make MD5 Text file, Screenshot.
- [ ] Zip file
- [ ] Rar file
- [ ] Google Drive
- [ ] Sourceforge


Cinch
=====================================
- [ ] Does it fit on a 4Gig Sandisk SD card?  
- [ ] Run Cinch and connect.
- [ ] change hostname and run Cinch and connect - should use new SSID



Publishing Tasks for Cinch
=====================================
- [ ] Reduce the Image Size with Piclone
- [ ] Generate MD5
- [ ] Make MD5 Text file, Screenshot.
- [ ] Zip file
- [ ] Rar file
- [ ] Google Drive
- [ ] Sourceforge

