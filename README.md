# Key-Logger
Key Logger which runs in background.

## What is a key-logger ?

A key-logger is a computer program, used to capture/track the keys press on a computer key-board.

A key-logger often runs in background, whilst the user is oblivious to it.
Key-loggers can be very dangerous as they mostly are used to attain a victim's credentials and other confidential data.

## How to make it work ??
Please run `pip install requirements.txt` in your command line.

Here is the file structure of this repository

```
Key-logger/
└── Files/
       └── README.md
   ├──.gitattributes
   ├──data.json
   ├──keylogger.pyw
   ├──LICENSE
   ├──README.md
   └──requirements.txt
```

You'll have to open the file `keylogger.pyw`. 

### NOTE
Notice the extension `.pyw`, this is so that it would run in background, in order to make that sure the program is running in the background, you'll have to check the task manager. In order to stop the key logger from record any further key-strokes, you can kill it from task manager.

![image](https://user-images.githubusercontent.com/83499821/139443037-83bb03ea-dc0d-4e6b-a525-e233781570a4.png)

Thereafter, we'll be seeing how to adjust the time of stroke recording and file storage.

### Duration of Recording

Notice the file `data.json`, when you'll open it, you find something like this...

```json
{ "time": 300 }
```
Basically, it is the amount of time in seconds for saving a txt file in `Files` after one-another, for example the basic time is 5 minutes in seconds, so after every 300 seconds, the keylogger will save a txt file in `Files`, these very individual text file contain all the keystrokes

---

## Usage and License

This Key-logger repository is licensed under "MIT License", so you are free to use it but the owner(s) is/are not responsible for any lose which might happen so. 

Moreover this keylogger is prepared by an Amateur, so should not be entirely trusted, this repository serves like a prototype if you were to make a real keylogger

Thank you

## Contributors

- [Navdeep](https://github.com/crypto-navdeep/) (Owner)
- [Ved Rathi](https://github.com/Ved-programmer) (Contributor)
