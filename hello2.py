import obspy
from obspy.clients.fdsn import Client
print("Hello Binder")
year = 2023
cat = Client("IRIS").get_events(minmag=6, maxmag=8, starttime=obspy.UTCDateTime(str(year) + \"-01-01T00:00\"), endtime=obspy.UTCDateTime(str(year+1) + \"-01-01T00:00\"))
print(cat)
