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


def suggestion_page(request):
    ###get artist from request###
    artist = request.REQUEST['artist']
    print artist
    fame   = .5
    suggested_artist = suggest.suggest_artist([artist], fame)
    print suggested_artist
    suggested_artist_bio   = info.get_bio(suggested_artist)
    print suggested_artist_bio
    suggested_artist_art   = info.get_image(suggested_artist)
    print suggested_artist_art
    suggested_artist_video = info.youtube_link(suggested_artist)
    print suggested_artist_video
    return render_to_response('suggestion_page.html', {"echonest_api_key": suggest.echonest_api_key,
                                                    "seed_artist":artist,
                                                    "s_artist": suggested_artist,
                                                    "bio": suggested_artist_bio,
                                                    "art": suggested_artist_art,
                                                    "vid": suggested_artist_video},
                               context_instance=RequestContext(request))

