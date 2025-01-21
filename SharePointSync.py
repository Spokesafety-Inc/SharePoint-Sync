#!/usr/bin/env python3
"""
__authors__    = ["Blaze Sanders"]
__contact__    = ["blaze.sanders@spokesafety.com]
__copyright__  = "Copyright 2025"
__license__    = "MIT"
__status__     = "Development"
__deprecated__ = "False"
__version__    = "0.1.0"
__doc__        = "Sync folder structures between mulitple Microsoft SharePoints and One Dive"
"""

## Standard Python libraries
import sys, os                                  # Filename and Operating System helper functions
from datetime import datetime, time, timedelta  # Schedule rsync (https://en.wikipedia.org/wiki/Rsync)
from time import sleep                          # Enable pausing of the python program
from typing import Dict                         # Enable optional data types used in creation of GUI tabs and .ENV file access
import subprocess                               # Enable the running of CLI commands like "pip3 install -r requirements.txt"
import requests                                 # Grab data from external API's
