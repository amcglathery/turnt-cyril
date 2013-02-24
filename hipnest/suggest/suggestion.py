from pyechonest import config
from pyechonest import artist
from random import randint

echonest_api_key = "VWFUA3PRSAGWROUNV"

config.ECHO_NEST_API_KEY= echonest_api_key


def suggest_artist(pos_seeds, neg_seeds, fame):
    # fame_level 0-10, 1 is Justin Bieber, 0 is a Tufts band.
    fame_level = fame / 10.0
    print pos_seeds
    print neg_seeds
    pos_artists = [artist.Artist(a) for a in pos_seeds] if pos_seeds else None
    neg_artists = [artist.Artist(a) for a in neg_seeds] if neg_seeds else None

    #Totally arbitrary, but it maintains a good level of hotttnesss.
    hot_level = (1 - fame_level)/2 + 0.1
    similars = []
    dissimilars = []

    # Decreases needed hotness level and increases familiarity upper bound
    # until a band is found.
    if pos_artists and neg_artists:
      while len(similars) < 1:
          similars = artist.similar(ids =[a.id for a in pos_artists],
                                    results = 20,
                                    max_familiarity = fame_level,
                                    min_hotttnesss = hot_level)
          dissimilars = artist.similar(ids = [a.id for a in neg_artists],
                                       results = 20,
                                       max_familiarity = fame_level,
                                       min_hotttnesss = hot_level)
          hot_level -= 0.05
          fame_level += 0.025
      similars = [a for a in similars if not a in dissimilars]
    else:
      while len(similars) < 1:
          similars = artist.similar(ids =[a.id for a in pos_artists],
                                    results = 20,
                                    max_familiarity = fame_level,
                                    min_hotttnesss = hot_level)
          hot_level -= 0.05
          fame_level += 0.025

    r = randint(0,len(similars)-1)
    return similars[r]




