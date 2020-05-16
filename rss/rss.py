#!/usr/bin/env python3
import feedparser
import os
import sys
import urllib.request
import json
import argparse
import time
import hashlib

def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue

parser = argparse.ArgumentParser()
parser.add_argument("-feed", metavar="url", required=True, help="rss feed url")
parser.add_argument("-interval", metavar="seconds", type=check_positive, default=60, help="update interval")

action = parser.add_mutually_exclusive_group()
action.add_argument("-next", action="store_true", help="show next entity")
action.add_argument("-prev", action="store_true", help="show previous entity")

args = parser.parse_args()
if args.interval < 0:
    parser.error("interval should be positive integer")


feedurl = args.feed
h = hashlib.md5(feedurl.encode())
cachefile = h.hexdigest() + ".cache"


n = os.environ.get("I3__n")
if n is None:
    n = 0
else:
    n = int(n)

if not os.path.isfile(cachefile):
    urllib.request.urlretrieve(feedurl, cachefile)
    n = 0
else:
    mt = os.path.getmtime(cachefile)
    if time.time() - mt > args.interval:
        urllib.request.urlretrieve(feedurl, cachefile)
        n = 0

NewsFeed = feedparser.parse(cachefile)


if args.next:
    n += 1

if args.prev:
    n -= 1

if n >= len(NewsFeed.entries):
    n = len(NewsFeed.entries) - 1

if n < 0:
    n = 0


entry = NewsFeed.entries[n]

urgent = False
if n == 0 and not entry.link == os.environ.get("I3__link"):
    urgent = True

blocks = [
        {
            "full_text": entry.title,
            "_link": entry.link,
            "_n": n,
            }
        ]

print(json.dumps(blocks))
