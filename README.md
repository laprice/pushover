# Python Pushover

This is a library and a commandline client to the [Pushover.net](http://pushover.net/ "Pushover") notification service.

## Requirements

 * Either JSON (Python 2.6+) or [simplejson](http://pypi.python.org/pypi/simplejson/ "simplejson") (Python 2.5+)
 * [requests](http://docs.python-requests.org/en/latest/index.html "python requests") 

## Import as a module

You can import pushover simply with ```import pushover```

When initialising a ```PushoverCLient``` you may pass a path to a pushover configuration file as seen in example.pushover. The library will also look for a ```$HOME/.pushover``` but the configuration file passed in manually takes precedence.

```python
import pushover
client = pushover.PushoverClient("/a/path/to/a/file")
try:
    client.send_message("Some message")
except SomeError:
    ... deal with it ...
```

Take note that when using this as a module the message you send will not be automatically truncated to 512 characters. It is up to your application code to ensure the message passed meets the requirements or catch the ```pushover.PushoverMessageTooBig``` exception.

## Commandline

Just run ```pushover.py --help``` (don't forget to make the script executable) or ```python pushover.py --help``` for help.

You'll have to at least supply a ```-m some_message``` or ```--message=some_message``` and you may supply the debug flag or an alternative configuration file.

Contrary to when this module is imported, when called on the commandline the message will be truncated to 512 characters in order to avoid that kind of errors.

```
Usage: pushover.py [options]

This module will send a message through the Pushover.net notification service.
It requires at least the '-m' / '--message' parameter to be passed.

Options:
  -h, --help            show this help message and exit
  -c CONFIGFILE, --config=CONFIGFILE
                        Location of the Pushover config file.
  -d, --debug           Log at the DEBUG loglevel.
  -m MESSAGE, --message=MESSAGE
                        The message to send, will truncate to 512 chars.
```

## Todo

 * Be able to pass in a configurationobject instead of a file when being imported.
