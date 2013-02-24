from pyechonest import config
from pyechonest import artist
from random import randint

echonest_api_key = "VWFUA3PRSAGWROUNV"

config.ECHO_NEST_API_KEY= echonest_api_key


def suggest_artist(seeds, neg_seeds, fame_level):
    # fame_level 0-1, 1 is Justin Bieber, 0 is a Tufts band.
    seed_artists = []
    for a in seeds:
      seed_artists.append(artist.Artist(a))
    neg_artists = [artist.Artist(a) for a in neg_seeds]

    #Totally arbitrary, but it maintains a good level of hotttnesss.
    hot_level = (1 - fame_level)/2 + 0.1
    similars = []
    dissimilars = []

    # Decreases needed hotness level and increases familiarity upper bound
    # until a band is found.
    while len(similars) < 1:
        similars = artist.similar(ids =[a.id for a in seed_artists],
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
    r = randint(0,len(similars))
    print similars
    return similars[r]

print suggest_artist(['radiohead', 'foo fighters'], ['miley cyrus'], .5)


