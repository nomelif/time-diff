TimeDiffText and TimeDiffPlot
=============================

This repository contains two programs, TimeDiffText and TimeDiffPlot. Both take log-files in the form of streams as input. TimeDiffText then outputs the difference in time between log entries, TimeDiffPlot uses Matplotlib, Numpy and Scipy to graph the differences in the log-files. TimeDiffPlot also allows for saving generated graphs into a file. Supported file-formats are _.emf_, _.eps_, _.pdf_, _.png_, _.ps_, _.raw_, _.rgba_, _.svg_ and _.svgz_. Both TimeDiffText and TimeDiffPlot allow any syntax for the time through python [datetime.strftime() and datetime.strptime()](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior "Syntax for entering time formats"). Formatting presets for bothes time-diff and time-diff-plot can be set in /etc/timediff/timediff.json.

TimeDiffPlot requires Matplotlib, Numpy and Scipy.

TimeDiffText and TimeDiffPlot are both written in python 2.7 and compatile with Mac OSX and Linux.

TimeDiff 1.17

Known issues:
- Formatting java1 does not read in milliseconds, due to restrictions in Python's datetime module.

Installing TimeDiff
===================

TimeDiff can be installed through pip by calling

    # pip install timediff

TimeDiffPlot is also dependent of MatPlotLib, NumPy and SciPy. These can be installed by calling

    # pip install matplotlib

to install MatPlotLib,

    # pip install numpy

to install NumPy and

    # pip install scipy

to install SciPy.

During its installation, TimeDiff will write a configuration file to _/etc/timediff/timediff.json_. This is why it requires root to install. If _/etc/timediff/timediff.json_ is not found, TimeDiff will quit.

Example of running TimeDiffText and TimeDiffPlot
================================================

Here is an example of running TimeDiffText and TimeDiffPlot.

We begin by taking the 10 last lines of _/var/log/syslog_

    $ tail /var/log/sysolg > logfile

The file _logfile_ looks like this:

    Oct 10 10:30:33 p WindowServer[119]: CGXSetWindowTransform: Operation on a window 0xb6 requiring rights kCGSWindowRightPresenter by caller com.apple.appkit.xpc.openAndSav
    Oct 10 10:30:33 p com.apple.appkit.xpc.openAndSavePanelService[911]: CGSSetWindowTransformAtPlacement: Failed
    Oct 10 10:30:33 p com.apple.appkit.xpc.openAndSavePanelService[911]: ERROR: CGSSetWindowTransformAtPlacement() returned 1001
    Oct 10 10:30:33 p WindowServer[119]: CGXSetWindowListAlpha: Operation on a window 0xb6 requiring rights kCGSWindowRightPresenter by caller com.apple.appkit.xpc.openAndSav
    Oct 10 10:30:33 p WindowServer[119]: CGXSetWindowTransform: Operation on a window 0xb6 requiring rights kCGSWindowRightPresenter by caller com.apple.appkit.xpc.openAndSav
    Oct 10 10:30:33 p com.apple.appkit.xpc.openAndSavePanelService[911]: CGSSetWindowTransformAtPlacement: Failed
    Oct 10 10:30:33 p com.apple.appkit.xpc.openAndSavePanelService[911]: ERROR: CGSSetWindowTransformAtPlacement() returned 1001
    Oct 10 10:30:33 p WindowServer[119]: CGXSetWindowListAlpha: Operation on a window 0xb6 requiring rights kCGSWindowRightPresenter by caller com.apple.appkit.xpc.openAndSav
    Oct 10 10:30:33 p WindowServer[119]: CGXSetWindowTransform: Operation on a window 0xb6 requiring rights kCGSWindowRightPresenter by caller com.apple.appkit.xpc.openAndSav
    Oct 10 10:30:33 p com.apple.appkit.xpc.openAndSavePanelService[911]: CGSSetWindowTransformAtPlacement: Failed

Then we run TimeDiffText on _logfile_

    $ timedifftext logfile -F linux1

And we get this output:

         0 s          0 s : Oct 10 10:30:33 p WindowServer[119]: CGXSetWindowTransform: Operation on a window 0xb6 requiring rights kCGSWindowRightPresenter by caller com.apple.appkit.xpc.openAndSav
         
         0 s          0 s : Oct 10 10:30:33 p com.apple.appkit.xpc.openAndSavePanelService[911]: CGSSetWindowTransformAtPlacement: Failed
         
         0 s          0 s : Oct 10 10:30:33 p com.apple.appkit.xpc.openAndSavePanelService[911]: ERROR: CGSSetWindowTransformAtPlacement() returned 1001
         
         0 s          0 s : Oct 10 10:30:33 p WindowServer[119]: CGXSetWindowListAlpha: Operation on a window 0xb6 requiring rights kCGSWindowRightPresenter by caller com.apple.appkit.xpc.openAndSav
         
         0 s          0 s : Oct 10 10:30:33 p WindowServer[119]: CGXSetWindowTransform: Operation on a window 0xb6 requiring rights kCGSWindowRightPresenter by caller com.apple.appkit.xpc.openAndSav
         
         0 s          0 s : Oct 10 10:30:33 p com.apple.appkit.xpc.openAndSavePanelService[911]: CGSSetWindowTransformAtPlacement: Failed
         
         0 s          0 s : Oct 10 10:30:33 p com.apple.appkit.xpc.openAndSavePanelService[911]: ERROR: CGSSetWindowTransformAtPlacement() returned 1001
         
         0 s          0 s : Oct 10 10:30:33 p WindowServer[119]: CGXSetWindowListAlpha: Operation on a window 0xb6 requiring rights kCGSWindowRightPresenter by caller com.apple.appkit.xpc.openAndSav
         
         0 s          0 s : Oct 10 10:30:33 p WindowServer[119]: CGXSetWindowTransform: Operation on a window 0xb6 requiring rights kCGSWindowRightPresenter by caller com.apple.appkit.xpc.openAndSav
         
         0 s          0 s : Oct 10 10:30:33 p com.apple.appkit.xpc.openAndSavePanelService[911]: CGSSetWindowTransformAtPlacement: Failed

Then we run TimeDiffPlot on the original log (_/var/log/messages_)

    $ timediffplot /var/log/messages -F linux1 -O graph
    $ ls -l

And we get this result:

    -rw-r--r-- 1 usr usr  26K Oct 10 11:03 graph_histogram_absolute_lin.png
    -rw-r--r-- 1 usr usr  24K Oct 10 11:03 graph_histogram_interval_lin.png
    -rw-r--r-- 1 usr usr  50K Oct 10 11:01 graph_KDE_absolute_lin.png
    -rw-r--r-- 1 usr usr  39K Oct 10 11:03 graph_KDE_interval_lin.png


graph_histogram_absolute_lin.png
--------------------------------

![Histogram over time](examples/graph_histogram_absolute_lin.png)

In this plot we see the quantity of log entries per second plotted against time. The spike at about 260 s means a lot of log activity.

graph_histogram_interval_lin.png
--------------------------------

![Interval histogram](examples/graph_histogram_interval_lin.png)

In this plot we see the quantity of errors per interval of n seconds, n increasing as the x-coordinate increases. Put in an other way: a spike somewhere means that there have been logs coming in a repetitive way every n seconds. The big spike at the left side tells us that the interval between log-entries has been mostly short (one second).

graph_KDE_absolute_lin.png
--------------------------

This plot is the KDE of the first plot. A smooth version of it in other words. Handy if you had a lot of noise in the original plot.

![Kernel density estimation over time](examples/graph_KDE_absolute_lin.png)

graph_KDE_interval_lin.png
--------------------------

This plot is the KDE of the second plot.

![Interval kernel density estimation](examples/graph_KDE_interval_lin.png)

Running TimeDiffText
====================

TimeDiffText can be run by calling

    $ cat <file_to_parse> | timedifftext <arguments>

You may also want to pipe in data from grep

    $ grep <data_to_grep> <grep's_args> | timedifftext <arguments>

TimeDiffText can also read a file by given filename.

    $ timedifftext <filename> <arguments>

TimeDiffText will then output the following

    <difference_from_time_of_first_line> <difference_from_time_of_previous_line> <line_processed>

Usage of TimeDiffText
---------------------

    usage: timedifftext  [-h] [--format [FORMAT]] [--format-preset [{linux1,custom1}]]
                         [--locale [LOCALE]] [--verbose] [--cancel-padding]
                         [--round-to {s,ms,min,h,d}]

    Calculate differences in time of log entries and output them into the console.

    optional arguments:
    -h, --help            show this help message and exit
    --format [FORMAT], -f [FORMAT]
                        Sets datetime format options, defaults to
                        "%Y%m%d_%H%M%S" overrides given presets.
    --format-preset [{linux1,custom1,java1}], -F [{linux1,custom1,java1}]
                        Set datetime formatting preset, defaults to custom1.
                        Values are: linux1 -> %b %d %H:%M:%S, custom1 ->
                        %Y%m%d_%H%M%S java1 -> %Y-%m-%d %H:%M:%S
    --locale [LOCALE], -l [LOCALE]
                        Sets locale to be used with parsing month and weekday
                        names, defaults to American English (en_US).
    --verbose, -v         Sets program to verbose mode. This will result in
                        loger descriptions of errors being written to the
                        stderr.
    --cancel-padding, -p  Cancels adding zero-padding, eg. without -p 2 would
                        become 02.
    --round-to {s,ms,min,h,d}, -r {s,ms,min,h,d}
                        Sets what time-unit to round to while doing
                        formatting.

Running TimeDiffPlot
====================

TimeDiffPlot can be run by calling

    $ cat <file_to_parse> | timediffplot <arguments>

You may also want to pipe in data from grep

    $ grep <data_to_grep> <grep's_args> | timediffplot <arguments>

TimeDiffPlot can also read a file by given filename.

    $ timediffplot <filename> <arguments>

TimeDiffPlot only outputs errors by default. Instead, TimeDiffPlot will open windows and draw graphs using matplotlib. This behaviour can be changed, resulting in TimeDiffPlot rather writing the graphs to disk. Using TimeDiffPlot with logs of over 50 000 lines may take some time.

Usage of TimeDiffPlot
---------------------

    usage: timediffplot   [-h] [--format [FORMAT]]
                          [--format-preset [{linux1,custom1}]] [--locale [LOCALE]]
                          [--verbose] [--cancel-padding] [--logarithmic]

    Calculate differences in time of log entries and output them into the console.

    optional arguments:
      -h, --help            show this help message and exit
      --format [FORMAT], -f [FORMAT]
                            Sets datetime format options, overrides given presets.
      --format-preset [{linux1,custom1,java1}], -F [{linux1,custom1,java1}]
                            Set datetime formatting preset, defaults to custom1.
                            Values are: linux1 -> %b %d %H:%M:%S, custom1 ->
                            %Y%m%d_%H%M%S java1 -> %Y-%m-%d %H:%M:%S
      --locale [LOCALE], -l [LOCALE]
                            Sets locale to be used with parsing month and weekday
                            names, defaults to American English (en_US).
      --verbose, -v         Sets program to verbose mode. This will result in
                            loger descriptions of errors being written to the
                            stderr.
      --cancel-padding, -p  Cancels adding zero-padding, eg. without -p 2 would
                            become 02.
      --logarithmic, -L     Sets y-axis of plots to be on a logarithmic scale

      --output-path, -O     Path for outputting images to disk.

      --output-format, -o   Format of outputted graphs. Choices are .emf, .eps, .pdf, .png, .ps, .raw, .rgba, .svg and .svgz.
