##support playback from youtube###
from pyechonest import config
from pyechonest import artist
import gdata.youtube
import gdata.youtube.service
import re

yt_service = gdata.youtube.service.YouTubeService()

yt_service.developer_key = ("AI39si4Bf0pusSvJer3RGlOZbDq65cHg_tteJFqfOJcPcrKz"+
                           "Qmb5WzPsLUVC-iDYb_OC4KxX0zVmRtGa0cXDJgtIbnLkXGwpVg")
yt_service.client_id     = "940552434409.apps.googleusercontent.com"
yt_service.ssl           = True

config.ECHO_NEST_API_KEY="VWFUA3PRSAGWROUNV"

### a is artist string from suggestion.py ###
def youtube_link(a):
    ytbs = ([s for s in artist.Artist(a).get_video(100, 0) if
            'youtube' in s['site']])
    ytbs = ([s for s in ytbs if not (('cover'  in s['title'].lower())
                                or  ('live'    in s['title'].lower())
                                or  ('karaoke' in s['title'].lower()))]) 
    ytbs = [views_from_en_vid(s) for s in ytbs]
    ### filter out covers, live recordings, karaoke version###
    return ytbs

###get number of views for echonest youtube video###
###return pair (url, views)###
def views_from_en_vid(v):
    yt_id = re.split('=',v['url'])[1]
    entry = yt_service.GetYouTubeVideoEntry(video_id=yt_id)
    return (v['url'], entry.statistics.view_count)
for y in youtube_link("radiohead"):
    print y
