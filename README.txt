TimeDiffText and TimeDiffPlot
=============================

This repository contains two programs, TimeDiffText and TimeDiffPlot. Both take log-files in the form of streams as input. TimeDiffText then outputs the difference in time between log entries, TimeDiffPlot uses Matplotlib, Numpy and Scipy to graph the differences in the log-files. TimeDiffPlot also allows for saving generated graphs into a file. Supported file-formats are _.emf_, _.eps_, _.pdf_, _.png_, _.ps_, _.raw_, _.rgba_, _.svg_ and _.svgz_. Both TimeDiffText and TimeDiffPlot allow any syntax for the time through python [datetime.strftime() and datetime.strptime()](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior "Syntax for entering time formats"). Formatting presets for bothes time-diff and time-diff-plot can be set in /etc/timediff/timediff.json.

TimeDiffPlot requires Matplotlib, Numpy and Scipy.

TimeDiffText and TimeDiffPlot are both written in python 2.7  (though it should be backwards-compatible with 2.6) and compatile with Mac OSX and Linux.

TimeDiff 1.15

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

    Oct 10 10:30:33 air-vpn-10-0-82-3.portalify.com WindowServer[119]: CGXSetWindowTransform: Operation on a window 0xb6 requiring rights kCGSWindowRightPresenter by caller com.apple.appkit.xpc.openAndSav
    Oct 10 10:30:33 air-vpn-10-0-82-3.portalify.com com.apple.appkit.xpc.openAndSavePanelService[911]: CGSSetWindowTransformAtPlacement: Failed
    Oct 10 10:30:33 air-vpn-10-0-82-3.portalify.com com.apple.appkit.xpc.openAndSavePanelService[911]: ERROR: CGSSetWindowTransformAtPlacement() returned 1001
    Oct 10 10:30:33 air-vpn-10-0-82-3.portalify.com WindowServer[119]: CGXSetWindowListAlpha: Operation on a window 0xb6 requiring rights kCGSWindowRightPresenter by caller com.apple.appkit.xpc.openAndSav
    Oct 10 10:30:33 air-vpn-10-0-82-3.portalify.com WindowServer[119]: CGXSetWindowTransform: Operation on a window 0xb6 requiring rights kCGSWindowRightPresenter by caller com.apple.appkit.xpc.openAndSav
    Oct 10 10:30:33 air-vpn-10-0-82-3.portalify.com com.apple.appkit.xpc.openAndSavePanelService[911]: CGSSetWindowTransformAtPlacement: Failed
    Oct 10 10:30:33 air-vpn-10-0-82-3.portalify.com com.apple.appkit.xpc.openAndSavePanelService[911]: ERROR: CGSSetWindowTransformAtPlacement() returned 1001
    Oct 10 10:30:33 air-vpn-10-0-82-3.portalify.com WindowServer[119]: CGXSetWindowListAlpha: Operation on a window 0xb6 requiring rights kCGSWindowRightPresenter by caller com.apple.appkit.xpc.openAndSav
    Oct 10 10:30:33 air-vpn-10-0-82-3.portalify.com WindowServer[119]: CGXSetWindowTransform: Operation on a window 0xb6 requiring rights kCGSWindowRightPresenter by caller com.apple.appkit.xpc.openAndSav
    Oct 10 10:30:33 air-vpn-10-0-82-3.portalify.com com.apple.appkit.xpc.openAndSavePanelService[911]: CGSSetWindowTransformAtPlacement: Failed

Then we run TimeDiffText on _logfile_

    $ timedifftext logfile -F linux1

And we get this output:

         0 s          0 s : Oct 10 10:26:09 air-vpn-10-0-82-3.portalify.com CalendarAgent[210]: [com.apple.calendar.store.log.subscription] [Failed to refresh <CalManagedSubscriptionInfo: 0x7f8d995898e0> (entity: SubscriptionInfo; id: 0x14001ab <x-coredata://34975977-6047-4D54-96E4-8BAF120B2E45/SubscriptionInfo/p5> ; data: {

         0 s          0 s : Oct 10 10:26:09 air-vpn-10-0-82-3.portalify.com CalendarAgent[210]: [com.apple.calendar.store.log.subscription] [Failed to refresh <CalManagedSubscriptionInfo: 0x7f8d9978aaf0> (entity: SubscriptionInfo; id: 0x30001ab <x-coredata://34975977-6047-4D54-96E4-8BAF120B2E45/SubscriptionInfo/p12> ; data: {

         0 s          0 s : Oct 10 10:26:09 air-vpn-10-0-82-3.portalify.com CalendarAgent[210]: [com.apple.calendar.store.log.subscription] [Failed to refresh <CalManagedSubscriptionInfo: 0x7f8d99437bb0> (entity: SubscriptionInfo; id: 0x64001ab <x-coredata://34975977-6047-4D54-96E4-8BAF120B2E45/SubscriptionInfo/p25> ; data: {

         0 s          0 s : Oct 10 10:26:09 air-vpn-10-0-82-3.portalify.com CalendarAgent[210]: [com.apple.calendar.store.log.subscription] [Failed to refresh <CalManagedSubscriptionInfo: 0x7f8d997efc90> (entity: SubscriptionInfo; id: 0x34001ab <x-coredata://34975977-6047-4D54-96E4-8BAF120B2E45/SubscriptionInfo/p13> ; data: {

         0 s          0 s : Oct 10 10:26:09 air-vpn-10-0-82-3.portalify.com CalendarAgent[210]: [com.apple.calendar.store.log.subscription] [Failed to refresh <CalManagedSubscriptionInfo: 0x7f8d996b82f0> (entity: SubscriptionInfo; id: 0x60001ab <x-coredata://34975977-6047-4D54-96E4-8BAF120B2E45/SubscriptionInfo/p24> ; data: {

         0 s          0 s : Oct 10 10:26:09 air-vpn-10-0-82-3.portalify.com CalendarAgent[210]: [com.apple.calendar.store.log.subscription] [Failed to refresh <CalManagedSubscriptionInfo: 0x7f8d9969f760> (entity: SubscriptionInfo; id: 0x4c001ab <x-coredata://34975977-6047-4D54-96E4-8BAF120B2E45/SubscriptionInfo/p19> ; data: {

         0 s          0 s : Oct 10 10:26:09 air-vpn-10-0-82-3.portalify.com CalendarAgent[210]: [com.apple.calendar.store.log.subscription] [Failed to refresh <CalManagedSubscriptionInfo: 0x7f8d99420bb0> (entity: SubscriptionInfo; id: 0x44001ab <x-coredata://34975977-6047-4D54-96E4-8BAF120B2E45/SubscriptionInfo/p17> ; data: {

       205 s        205 s : Oct 10 10:29:34 air-vpn-10-0-82-3 kernel[0]: process plugin-container[328] caught causing excessive wakeups. Observed wakeups rate (per sec): 387; Maximum permitted wakeups rate (per sec): 150; Observation period: 300 seconds; Task lifetime number of wakeups: 188841

       205 s          0 s : Oct 10 10:29:34 air-vpn-10-0-82-3.portalify.com ReportCrash[905]: Invoking spindump for pid=328 wakeups_rate=387 duration=117 because of excessive wakeups

       209 s          4 s : Oct 10 10:29:38 air-vpn-10-0-82-3.portalify.com spindump[906]: Saved wakeups_resource.spin report for plugin-container version ??? (1.0) to /Library/Logs/DiagnosticReports/plugin-container_2014-10-10-102938_p020031.wakeups_resource.spin

Then we run TimeDiffPlot on the original log (_/var/log/messages_)

    $ timediffplot /var/log/messages -F linux1 -O graph

And we get this result:

graph histogram (over time).png
-------------------------------

![Histogram over time](graph_histogram_\(over_time\).png)

graph histogram.png
-------------------

![Interval histogram](graph_histogram.png)

graph KDE (over time).png
-------------------------

![Kernel density estimation over time](graph_KDE_\(over_time\).png)

graph KDE.png
-------------

![Interval kernel density estimation](graph_KDE.png)

Running TimeDiffText
====================

TimeDiff can be run by calling

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
