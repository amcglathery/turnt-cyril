from django.shortcuts import render_to_response
from django.template import RequestContext
import suggest.suggestion as suggest
import information as info

def index(request):
  return render_to_response('base.html', { "echonest_api_key" : suggest.echonest_api_key, "foo" : "bar" },
                                        context_instance=RequestContext(request))

def splash_page(request):
    return render_to_response('splash_page.html', {"echonest_api_key": suggest.echonest_api_key},
                               context_instance=RequestContext(request))


#def suggest_page(request):
#    ###get artist from request###
#    suggested_artist = suggest.suggestArtist(artist)
#    suggested_artist_bio   = info.get_bio(suggested_artist)
#    suggested_artist_art   = info.get_image(suggested_artist)
#    suggested_artist_video = info.create_video_object(youtube_link(suggested_artist))

