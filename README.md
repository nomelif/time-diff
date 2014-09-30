TimeDiff
========

This program parses log files and outputs the difference in time between log entries. Can work on either files directly, or through grep or similar. Allows for any syntax for the time through python [datetime.strftime() and datetime.strptime()](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior "Syntax for entering time formats").

TimeDiff is written in python 2.7 and compatile with Mac OSX and Linux.

Running TimeDiff
================

TimeDiff can be run by calling

    $ cat <file_to_parse> | ./<path_to_TimeDiff>/time_diff/bin/time-diff <arguments>

You may also want to pipe in data from grep

    $ grep <data_to_grep> <grep's_args> | ./<path_to_TimeDiff>/time_diff/bin/time-diff <arguments>

Example of of running TimeDiff
------------------------------

Command entered:

    $ grep usb /var/log/messages | ./time_diff/bin/time-diff
    
Output:

    
    23:58:51 0:00:00 : Sep 30 09:29:54 zaphod kernel: [    1.384309] usb 3-2: new low-speed USB device number 2 using ohci_hcd
    23:58:51 0:00:00 : Sep 30 09:29:54 zaphod kernel: [    1.553398] usb 3-2: New USB device found, idVendor=046d, idProduct=c051
    23:58:51 0:00:00 : Sep 30 09:29:54 zaphod kernel: [    1.553400] usb 3-2: New USB device strings: Mfr=1, Product=2, SerialNumber=0
    23:58:51 0:00:00 : Sep 30 09:29:54 zaphod kernel: [    1.553403] usb 3-2: Product: USB-PS/2 Optical Mouse
    23:58:51 0:00:00 : Sep 30 09:29:54 zaphod kernel: [    1.553405] usb 3-2: Manufacturer: Logitech
    23:58:51 0:00:00 : Sep 30 09:29:54 zaphod kernel: [    1.906468] input: Logitech USB-PS/2 Optical Mouse as    /devices/pci0000:00/0000:00:13.1/usb3/3-2/3-2:1.0/input/input1
    23:58:51 0:00:00 : Sep 30 09:29:54 zaphod kernel: [    1.906555] generic-usb 0003:046D:C051.0001: input,hidraw0: USB HID v1.10 Mouse [Logitech USB-PS/2 Optical Mouse] on usb-0000:00:13.1-2/input0
    23:58:51 0:00:00 : Sep 30 09:29:54 zaphod kernel: [    1.906580] usbcore: registered new interface driver usbhid
    23:58:51 0:00:00 : Sep 30 09:29:54 zaphod kernel: [    1.906581] usbhid: USB HID core driver


Arguments
=========

TimeDiff accepts the following arguments:

* **-f** and **--format:** Specify datetime format as seen [here](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior "Syntax for entering time formats"). For ex. **--format="%b %d %H:%M:%S"**. Defaults to **"%b %d %H:%M:%S"**.
* **-p** and **--format-preset**: Specify format by preset, only **--format-preset=custom1** works for now, it results in the format **"%Y%m%d_%H%M%S"**
* **-l** and **-locale:** Set locale to use for parsing dates containing human-readable words, for ex. "Tuesday", "Oct" etc. Defaults to American English locale if installed, else falls back to the system's default locale.
* **-h** and **--help:** Display a help containing basically this same information.