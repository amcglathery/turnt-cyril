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
    pos_string = request.REQUEST['pos_artists']
    neg_string = request.REQUEST['neg_artists']
    pos_artists = pos_string.rsplit(',') if len(pos_string) > 0 else None
    neg_artists = neg_string.rsplit(',') if len(neg_string) > 0 else None
    fame   = float(request.REQUEST['fame'])
    suggested_artist = suggest.suggest_artist(pos_artists, neg_artists, fame)
    print suggested_artist
    suggested_artist_bio   = info.get_bio(suggested_artist)
    print suggested_artist_bio
    suggested_artist_art   = info.get_image(suggested_artist)
    print suggested_artist_art
    suggested_artist_video = info.youtube_link(suggested_artist)
    print suggested_artist_video
    return render_to_response('suggestion_page.html', {"echonest_api_key": suggest.echonest_api_key,
                                                    "seed_artist": pos_artists[-1],
                                                    "s_artist": suggested_artist,
                                                    "bio": suggested_artist_bio,
                                                    "art": suggested_artist_art,
                                                    "vid": suggested_artist_video},
                               context_instance=RequestContext(request))

