from pyechonest import config
from pyechonest import artist
config.ECHO_NEST_API_KEY="VWFUA3PRSAGWROUNV"


def suggest_artist(seeds, fame_level):
    # fame_level 0-1, 1 is Justin Bieber, 0 is a Tufts band.
    seed_artists = []
    for a in seeds:
      seed_artists.append(artist.Artist(a))
    print "Artists similar to: ", seed_artists
  
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
    
    for similar_artist in similars: 
         print "\t%s %s %s" % (similar_artist.name, similar_artist.hotttnesss, similar_artist.familiarity)
  
suggest_artist(["purity ring"], 0.6)
