# District court timezone mappings.

# This data is from checking each district's state (or territory) in
# the tz database, and for those states with multiple zones, checking
# the first office for each district court (and presuming that
# bankruptcy courts follow their district couts).
#
# Office addressed checked against, e.g.
# https://ecf.nysd.uscourts.gov/cgi-bin/CourtInfo.pl
#
# A 'district3' is the first 3 characters of a district without the
# terminal 'd' for District Court or 'b' for Bankruptcy Court
#
# John Hawkinson <jhawk@mit.edu>
# 7 Feb 2018

class ECFTimezone:

    tz_to_states = {
        'America/Boise': ['id'],
        'America/Puerto_Rico': ['pr'],
        'America/St_Thomas': ['vi'],
        'Pacific/Guam': ['gu'],
        'US/Alaska': ['ak'],
        'US/Arizona': ['az'],
        'US/Central': ['al', 'ar', 'ia', 'il', 'ks', 'la', 'mn', 'mo', 'ms',
                       'nd', 'ne', 'ok', 'sd',
                       # some offices of WDTX are in US/Mountain (e.g. El Paso)
                       'tx',
                       'wi'],
        'US/Eastern': ['ct', 'dc', 'de',
                       # some offices NDFL are in US/Central (e.g. Pensacola,
                       # Panama City)
                       # http://www.flsd.uscourts.gov/?page_id=7850
                       'fl',
                       'ga', 'in', 'ky', 'ma', 'md', 'me', 'nc', 'nh', 'nj',
                       'ny', 'oh', 'pa', 'ri', 'sc', 'va', 'vt', 'wv'],
        'US/Hawaii': ['hi'],
        'US/Michigan': ['mi'],
        'US/Mountain': ['co', 'mt', 'nm', 'ut', 'wy'],
        'US/Pacific': ['ca', 'nv', 'or', 'wa'],
    }

    tz_to_district3 = {
        'Pacific/Guam': ['nmi'],
        'US/Central': ['tnm', 'tnw'],
        'US/Eastern': ['tne'],
    }

    tz_to_exact = {
        'US/Central': ['ca5', 'ca7', 'ca8'],
        'US/Eastern': ['ca1', 'ca2', 'ca3', 'ca4', 'ca6', 'ca11',
                       'cadc', 'cafc',
                       'cit', 'cofc', 'jpml'],
        'US/Mountain': ['ca10'],
        'US/Pacific': ['ca9'],
    }

    def _invertDictList(d):
        return dict((v, k) for k in d for v in d[k])

    state_to_tz = _invertDictList(tz_to_states)
    district3_to_tz = _invertDictList(tz_to_district3)
    exact_to_tz = _invertDictList(tz_to_exact)

    def timezone(self, district):
        tz = self.exact_to_tz.get(district)
        if tz is None:
            tz = self.district3_to_tz.get(district[0:3])
        if tz is None:
            tz = self.state_to_tz[district[0:2]]
        return tz
