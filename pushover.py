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
py27 = (2,7)
cur_py = sys.version_info
logger = logging.getLogger(__name__)
if cur_py < py27:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass
    logger.addHandler(NullHandler())
else:
    logger.addHandler(logging.NullHandler())

class PushoverException(Exception):
    pass

class PushoverMessageTooBigException(PushoverException):
    pass

class PushoverClient(object):
    """ PushoverClient, used to send messages to the Pushover.io service. """
    def __init__(self, configfile=''):
        self.configfile = configfile
        self.parser = SafeConfigParser()
        self.files = self.parser.read([self.configfile, os.path.expanduser('~/.pushover')])
        if not self.files:
            logger.critical("No valid configuration found, exiting.")
            sys.exit(1)
        self.conf = { 'app_key': self.parser.get('pushover','app_key'),
             'user_key': self.parser.get('pushover','user_key')}

    def send_message(self, message):
        if len(message) > 512:
            raise PushoverMessageTooBigException("The supplied message is bigger than 512 characters.")
        payload = {
                'token': self.conf['app_key'],
                'user' : self.conf['user_key'],
                'message': message,
        }   
        r = requests.post('https://api.pushover.net/1/messages.json', data=payload )
        if not r.status_code == requests.codes.ok:
            raise r.raise_for_status()
                      
if __name__=='__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(module)s] %(levelname)s: %(message)s')
    client = PushoverClient()
    try:
        client.send_message("This is a test message")
    except Exception as e:
        logger.critical("Something went wrong: {0}".format(e))
