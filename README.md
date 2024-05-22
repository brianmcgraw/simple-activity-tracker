# simple-activity-tracker

Computer Time Tracking

How to set this up on MacOS

Place these files into a directory where you are comfortable storing log files. The logger will check if you are logged in every 5 minutes, the summary will run once daily and summarize time spent logged in on any previous days.

`touch ~/Library/LaunchAgents/com.user.activitylogger.plist`

Update the path to your script below.

```

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.activitylogger</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/path/to/your_script.py</string>
    </array>
    <key>StartInterval</key>
    <integer>300</integer>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/activitylogger.out</string>
    <key>StandardErrorPath</key>
    <string>/tmp/activitylogger.err</string>
</dict>
</plist>
```

launchctl load ~/Library/LaunchAgents/com.user.activitylogger.plist

`touch ~/Library/LaunchAgents/com.user.activitysummary.plist`

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.activitysummary</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/path/to/your_script.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/activitysummary.out</string>
    <key>StandardErrorPath</key>
    <string>/tmp/activitysummary.err</string>
</dict>
</plist>

```

launchctl load ~/Library/LaunchAgents/com.user.activitysummary.plist
