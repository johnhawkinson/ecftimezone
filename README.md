Convert a CMECF court identifier into an IANA Timezone identifier

Sample usage:

```
>>> from ecftimezone import ECFTimezone
>>> e = ECFTimezone()
>>> e.timezone('cacd')
'US/Pacific'
>>> e.timezone('cadc')
'US/Eastern'
>>> e.timezone('nmid')
'Pacific/Guam'
>>> e.timezone('nmd')
'US/Mountain'
```

We (`generate.py`) also produce a dictionary that is precomputed:

```
>>> from ecfzones import ECFTimezones
>>> ECFTimezones.COURT['ca1']
'US/Eastern'
>>> ECFTimezones.COURT['mad']
'US/Eastern'
>>> ECFTimezones.COURT['ca9']
'US/Pacific'
>>> ECFTimezones.COURT['cacb']
'US/Pacific'
>>> 
```
