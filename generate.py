#!/usr/bin/env python

# Generate the list of ECF server domains (ecf.*.uscourts.gov)
# And dump their timezones to ecfzones.json

import collections
import json
import lxml.html
import re
import urllib2

from ecftimezone import ECFTimezone

PACERLINKS = 'http://www.pacer.gov/psco/cgi-bin/links.pl'

courts = set()

html = lxml.html.parse(urllib2.urlopen(PACERLINKS))
for e in html.iter('a'):
    link = e.get('href')
    if not link:
        continue
    match = re.match(r'^https?://ecf\.([^.]+)\.uscourts.gov', link)
    if match:
        courts.add(match.group(1))


f = open('ecfdomains.txt', 'w')
for c in sorted(courts):
    f.write(c + "\n")
f.close()

e = ECFTimezone()
d = {c: e.timezone(c) for c in courts}

# Unfortunately pprint dumps dictionaries with then open { on the ame
# line as the first line of the dictionary. Go with JSON instead.

f = open('ecfzones.json', 'w')
od = collections.OrderedDict(sorted(d.items()))
f.write(json.dumps(od, indent=4))
f.close()
