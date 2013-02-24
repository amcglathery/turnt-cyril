##support playback from youtube###
from pyechonest import config
from pyechonest import artist
import gdata.youtube
import gdata.youtube.service
import re
import string

yt_service = gdata.youtube.service.YouTubeService()

yt_service.developer_key = ("AI39si4Bf0pusSvJer3RGlOZbDq65cHg_tteJFqfOJcPcrKz"+
                           "Qmb5WzPsLUVC-iDYb_OC4KxX0zVmRtGa0cXDJgtIbnLkXGwpVg")
yt_service.client_id     = "940552434409.apps.googleusercontent.com"
yt_service.ssl           = True

config.ECHO_NEST_API_KEY="VWFUA3PRSAGWROUNV"

### a is echonest artist object from suggestion.py ###
### return url to youtube for highly-played song by a ###
def youtube_link(a):
    ytbs = ([s for s in a.get_video(100, 0) if
            'youtube' in s['site']])
    ytbs = ([s for s in ytbs if not (('cover'  in s['title'].lower())
                                or  ('live'    in s['title'].lower())
                                or  ('karaoke' in s['title'].lower()))])
    ### filter out covers, live recordings, karaoke version###
    threshold = 10000
    while(1):
        for v in ytbs:
            monad = views_from_en_vid(v)
            if monad:
                (yt_id, vws) = monad
            else:
                continue
            if vws >= threshold:
                return yt_id
        threshold /= 10
        if threshold == 0:
            return "dtzZjauGO7s" 


###get number of views for echonest youtube video###
###return pair (url, views)###
def views_from_en_vid(v):
    yt_id = re.split('=',v['url'])[1]
    entry = yt_service.GetYouTubeVideoEntry(video_id=yt_id)
    print entry
    if "limitedSyndication" or "not found" or "Private video" in str(entry):
        return None
    return (yt_id, entry.statistics.view_count)

###given youtube url, return a string containing embeddable YouTube player###
###for valid youtube url###
def create_video_object(url):
    return "<iframe width= \"560\" height = \"315\"\n\
 src = %s \n\
frameborder=\"0\" allowfullscreen></iframe>\n" %url

def get_bio(a):
    bios = a.get_biographies(results=50)
    if len(bios) == 0:
        return "%s are so hipster, we haven't even heard of them yet. But you have!" %a.name 
    for i in bios:
        if "last" in i[unicode('url')]:
           bio = i[unicode('text')]
           short_bio = bio[:400]
           last_dot = string.rfind('.', short_bio)
           short_bio = short_bio[:last_dot]
           return short_bio + "."
    return "%s are so hipster, we haven't even heard of them yet. But you have!" %a.name 

def get_image(a):
    images = a.get_images(results=50)
    try:
        for i in images[::-1]:
            if "last" in i[unicode('url')]:
                return i[unicode('url')]
        return images[0][unicode('url')]
    except:
        return "http://i.imgur.com/iGI3S7A.jpg" 


