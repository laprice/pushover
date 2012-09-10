#!/usr/bin/env python

from pushover import PushoverClient, PushoverException, PushoverMessageTooBig
import sys

def test_no_config():
    try:
        ps = PushoverClient(configfile="file_does_not_exist")
    except PushoverException:
        cls, instance, traceback = sys.exc_info()
        assert(instance.message=="No valid configuration found")    
    return

def test_message_too_big():
    try:
        ps = PushoverClient()
        ps.send_message("""
Whereas recognition of the inherent dignity and of the equal and inalienable rights of all members of the human family is the foundation of freedom, justice and peace in the world,

Whereas disregard and contempt for human rights have resulted in barbarous acts which have outraged the conscience of mankind, and the advent of a world in which human beings shall enjoy freedom of speech and belief and freedom from fear and want has been proclaimed as the highest aspiration of the common people,

Whereas it is essential, if man is not to be compelled to have recourse, as a last resort, to rebellion against tyranny and oppression, that human rights should be protected by the rule of law,

Whereas it is essential to promote the development of friendly relations between nations,""")
    except PushoverMessageTooBig:
        cls, instance, traceback = sys.exc_info()
        assert(instance.message=="The supplied message is bigger than 512 characters.")
    return

def test_send_message():
    ps = PushoverClient()
    ps.send_message("Test message from PushoverClient")

if __name__=="__main__":
    test_no_config()
    test_message_too_big()
    test_send_message()

