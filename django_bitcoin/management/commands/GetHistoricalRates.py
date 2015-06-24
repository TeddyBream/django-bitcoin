from django.core.management.base import NoArgsCommand
from django.conf import settings
import os
import sys
import re
import codecs
import subprocess
import urllib.request, urllib.error, urllib.parse
import urllib.request, urllib.parse, urllib.error
import json
import random
from time import sleep
import math
import datetime
from django_bitcoin.models import get_historical_price

import pytz  # 3rd party

class Command(NoArgsCommand):
    help = 'Create a profile object for users which do not have one.'

    def handle_noargs(self, **options):
        u = datetime.datetime.utcnow()
        u = u.replace(tzinfo=pytz.utc)
        print(u, get_historical_price())
