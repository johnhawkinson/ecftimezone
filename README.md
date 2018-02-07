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
