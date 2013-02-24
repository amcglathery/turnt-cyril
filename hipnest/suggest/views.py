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
    suggested_artist_bio   = info.get_bio(suggested_artist)
    suggested_artist_art   = info.get_image(suggested_artist)
    suggested_artist_video = info.youtube_link(suggested_artist)
    pos_string_plus_current = neg_string + ',' + suggested_artist.name
    print pos_string_plus_current
    neg_string_plus_current = neg_string + ',' + suggested_artist.name if neg_string > 0 else suggested_artist.name
    print neg_string_plus_current
    return render_to_response('suggestion_page.html', {"echonest_api_key": suggest.echonest_api_key,
                                                    "seed_artist": pos_artists[-1],
                                                    "s_artist": suggested_artist,
                                                    "pos_string" : pos_string.join(" "),
                                                    "neg_string": neg_string.join(" "),
                                                    "pos_string_plus_current" : pos_string_plus_current,
                                                    "neg_string_plus_current" : neg_string_plus_current,
                                                    "fame" : fame,
                                                    "fame_up" : fame + 0.1,
                                                    "fame_down" : fame - 0.1,
                                                    "bio": suggested_artist_bio,
                                                    "art": suggested_artist_art,
                                                    "vid": suggested_artist_video},
                               context_instance=RequestContext(request))

