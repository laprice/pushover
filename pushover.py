#!/usr/bin/env python

import sys
import os
import requests
from ConfigParser import SafeConfigParser

try:
    import simplejson as json
except ImportError:
    try:
        import json
    except ImportError:
        sys.exit("Please install the simplejson library or upgrade to Python 2.6+")

import logging
# Set up logging and add a NullHandler
logger = logging.getLogger(__name__)
try:
    logger.addHandler(logging.NullHandler())
except AttributeError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass
    logger.addHandler(NullHandler())

class PushoverException(Exception):
    pass

class PushoverMessageTooBig(PushoverException):
    pass

class PushoverClient(object):
    """ PushoverClient, used to send messages to the Pushover.net service. """
    def __init__(self, configfile=""):
        self.configfile = configfile
        self.parser = SafeConfigParser()
        self.files = self.parser.read([self.configfile, os.path.expanduser("~/.pushover")])
        if not self.files:
            logger.critical("No valid configuration found, exiting.")
            raise PushoverException("No valid configuration found")
        self.conf = { "app_key": self.parser.get("pushover","app_key"),
             "user_key": self.parser.get("pushover","user_key")}

    def send_message(self, message):
        if len(message) > 512:
            raise PushoverMessageTooBig("The supplied message is bigger than 512 characters.")
        payload = {
                "token": self.conf["app_key"],
                "user" : self.conf["user_key"],
                "message": message,
        }   
        r = requests.post("https://api.pushover.net/1/messages.json", data=payload )
        if not r.status_code == requests.codes.ok:
            raise r.raise_for_status()
                      
if __name__=="__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.description = "This module will send a message through the Pushover.net notification service. It requires at least the '-m' / '--message' parameter to be passed."
    parser.add_option("-c", "--config", dest = "configfile", help = "Location of the Pushover config file.")
    parser.add_option("-d", "--debug", dest = "debug", action = "store_true", help = "Log at the DEBUG loglevel.")
    parser.add_option("-m", "--message", dest = "message", help = "The message to send, will truncate to 512 chars.")
    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)
    (options, args) = parser.parse_args()

    if options.debug:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
    logging.basicConfig(level=loglevel, format="%(asctime)s [%(module)s] %(levelname)s: %(message)s")

    if options.configfile:
        client = PushoverClient(options.configfile)
    else:
        client = PushoverClient()

    if options.message:
        options.message = options.message[:512]
    else:
        parser.error("Can't do anything without a message now can I?")

    try:
        client.send_message(options.message)
    except Exception as e:
        logger.critical("Something went wrong: {0}".format(e))

