TimeDiff and TimeDiffPlot
=========================

TimeDiff parses log files and outputs the difference in time between log entries. Can work on either files directly, or through grep or similar. Allows for any syntax for the time through python [datetime.strftime() and datetime.strptime()](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior "Syntax for entering time formats").

TimeDiffPlot plots graphs on how common a certain difference in time between log entries is. Is called like TimeDiff (see above). Supports both linear and logarithmical scales. TimeiffPlot requires Matplotlib, Numpy and Scipy.

TimeDiff and TimeDiffPlot are both written in python 2.7 and compatile with Mac OSX and Linux.

Running TimeDiff
================

TimeDiff can be run by calling

    $ cat <file_to_parse> | ./<path_to_TimeDiff>/time_diff/bin/time-diff <arguments>

You may also want to pipe in data from grep

    $ grep <data_to_grep> <grep's_args> | ./<path_to_TimeDiff>/time_diff/bin/time-diff <arguments>

TimeDiff will then output the following

    <difference_from_time_of_first_line> <difference_from_time_of_previous_line> <line_processed>

Example of of running TimeDiff
------------------------------

Command entered:

    $ grep Logitech /var/log/messages | ./time_diff/bin/time-diff F=custom1
    
Output:

    
    0:00:00 0:00:00 : Sep 29 09:31:03 zaphod kernel: [    1.895439] input: Logitech USB-PS/2 Optical Mouse as /devices/pci0000:00/0000:00:13.1/usb3/3-1/3-1:1.0/input/input1
    0:00:00 0:00:00 : Sep 29 09:31:03 zaphod kernel: [    1.895683] generic-usb 0003:046D:C051.0001: input,hidraw0: USB HID v1.10 Mouse [Logitech USB-PS/2 Optical Mouse] on usb-0000:00:13.1-1/input0
    4:34:23 4:34:23 : Sep 29 14:05:26 zaphod kernel: [  170.629218] usb 2-1: Manufacturer: Logitech
    4:34:23 0:00:00 : Sep 29 14:05:26 zaphod kernel: [  170.678132] input: Logitech USB-PS/2 Optical Mouse as /devices/pci0000:00/0000:00:13.0/usb2/2-1/2-1:1.0/input/input4
    4:34:23 0:00:00 : Sep 29 14:05:26 zaphod kernel: [  170.678506] generic-usb 0003:046D:C051.0001: input,hidraw0: USB HID v1.10 Mouse [Logitech USB-PS/2 Optical Mouse] on usb-0000:00:13.0-1/input0
    5:00:10 0:25:47 : Sep 29 14:31:13 zaphod kernel: [    1.549321] usb 3-2: Manufacturer: Logitech
    5:00:10 0:00:00 : Sep 29 14:31:13 zaphod kernel: [    1.899382] input: Logitech USB-PS/2 Optical Mouse as /devices/pci0000:00/0000:00:13.1/usb3/3-2/3-2:1.0/input/input1
    5:00:10 0:00:00 : Sep 29 14:31:13 zaphod kernel: [    1.899472] generic-usb 0003:046D:C051.0001: input,hidraw0: USB HID v1.10 Mouse [Logitech USB-PS/2 Optical Mouse] on usb-0000:00:13.1-2/input0
    23:58:51 18:58:41 : Sep 30 09:29:54 zaphod kernel: [    1.553405] usb 3-2: Manufacturer: Logitech
    23:58:51 0:00:00 : Sep 30 09:29:54 zaphod kernel: [    1.906468] input: Logitech USB-PS/2 Optical Mouse as /devices/pci0000:00/0000:00:13.1/usb3/3-2/3-2:1.0/input/input1
    23:58:51 0:00:00 : Sep 30 09:29:54 zaphod kernel: [    1.906555] generic-usb 0003:046D:C051.0001: input,hidraw0: USB HID v1.10 Mouse [Logitech USB-PS/2 Optical Mouse] on usb-0000:00:13.1-2/input0
    2 days, 0:01:22 1 day, 0:02:31 : Oct  1 09:32:25 zaphod kernel: [    1.549285] usb 3-2: Manufacturer: Logitech
    2 days, 0:01:22 0:00:00 : Oct  1 09:32:25 zaphod kernel: [    1.902569] input: Logitech USB-PS/2 Optical Mouse as /devices/pci0000:00/0000:00:13.1/usb3/3-2/3-2:1.0/input/input1
    2 days, 0:01:22 0:00:00 : Oct  1 09:32:25 zaphod kernel: [    1.902656] generic-usb 0003:046D:C051.0001: input,hidraw0: USB HID v1.10 Mouse [Logitech USB-PS/2 Optical Mouse] on usb-0000:00:13.1-2/input0

Arguments of TimeDiff
---------------------

TimeDiff accepts the following arguments:

* **-p** : If not set the time will be parsed like all numerical parts of it would be zero-padded, eg. Tue Oct 5 would become Tue Oct 05.
* **-f** : Specify datetime format as seen [here](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior "Syntax for entering time formats"). For ex. **-f="%b %d %H:%M:%S"**. Defaults to **"%Y%m%d_%H%M%S"**.
* **-F** : Specify format by preset, only **-F=custom1** works for now, it results in the format **"%b %d %H:%M:%S"**
* **-l** : Set locale to use for parsing dates containing human-readable words, for ex. "Tuesday", "Oct" etc. Defaults to American English locale if installed, else falls back to the system's default locale.
* **-h** : Display a help containing basically this same information.
* **-v** : Set program to verbose mode, program will output python errors regarding parsings of logs. If not set program only outputs "Pattern "[formatting_pattern_used]" does not match logs".

Running TimeDiffPlot
====================

TimeDiffPlot can be run by calling

    $ cat <file_to_parse> | ./<path_to_TimeDiff>/time_diff/bin/time-diff-plot <arguments>

You may also want to pipe in data from grep

    $ grep <data_to_grep> <grep's_args> | ./<path_to_TimeDiff>/time_diff/bin/time-diff-plot <arguments>

TimeDiffPlot outputs nothing.

Arguments of TimeDiffPlot
-------------------------

TimeDiffPlot accepts the following arguments:

* **-p**    : If not set the time will be parsed like all numerical parts of it would be zero-padded, eg. Tue Oct 5 would become Tue Oct 05.
* **-f**    : Specify datetime format as seen [here](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior "Syntax for entering time formats"). For ex. **-f="%b %d %H:%M:%S"**. Defaults to **"%Y%m%d_%H%M%S"**.
* **-F**    : Specify format by preset, only **-F=custom1** works for now, it results in the format **"%b %d %H:%M:%S"**
* **-l**    : Set locale to use for parsing dates containing human-readable words, for ex. "Tuesday", "Oct" etc. Defaults to American English locale if installed, else falls back to the system's default locale.
* **-h**    : Display a help containing basically this same information.
* **-v**    : Set program to verbose mode, program will output python errors regarding parsings of logs. If not set program only outputs "Pattern "[formatting_pattern_used]" does not match logs".
* **--log** : If **--log** is specified, the program will set the scaling for the y-axis to be logarithmic. If not specified, it is set to linear.