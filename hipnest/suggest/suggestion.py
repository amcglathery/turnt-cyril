from pyechonest import config
from pyechonest import artist

echonest_api_key = "VWFUA3PRSAGWROUNV"

config.ECHO_NEST_API_KEY= echonest_api_key


def suggest_artist(seeds, fame_level):
    # fame_level 0-1, 1 is Justin Bieber, 0 is a Tufts band.
    seed_artists = []
    for a in seeds:
      seed_artists.append(artist.Artist(a))

    #Totally arbitrary, but it maintains a good level of hotttnesss.
    hot_level = (1 - fame_level)/2 + 0.1
    similars = []

    # Decreases needed hotness level and increases familiarity upper bound
    # until a band is found.
    while len(similars) < 1:
        similars = artist.similar(ids =[a.id for a in seed_artists],
                                  results = 1,
                                  max_familiarity = fame_level,
                                  min_hotttnesss = hot_level)

        hot_level -= 0.05
        fame_level += 0.025
    return similars[0]


