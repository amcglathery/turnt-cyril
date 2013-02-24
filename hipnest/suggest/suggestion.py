from pyechonest import config
from pyechonest import artist
config.ECHO_NEST_API_KEY="VWFUA3PRSAGWROUNV"


def suggestArtist(seeds, fameLevel):
    # fameLevel 0-1, 1 is Justin Bieber, 0 is a Tufts band.
    seedArtists = []
    for a in seeds:
      seedArtists.append(artist.Artist(a))
    print "Artists similar to: ", seedArtists
  
    #Totally arbitrary, but it maintains a good level of hotttnesss.
    hotLevel = (1 - fameLevel)/2 + 0.1
    similars = []
  
    # Decreases needed hotness level and increases familiarity upper bound
    # until a band is found.
    while len(similars) < 1:
        similars = artist.similar(ids =[a.id for a in seedArtists], 
                                  results = 1, 
                                  max_familiarity = fameLevel,
                                  min_hotttnesss = hotLevel)
    
        hotLevel -= 0.05
        fameLevel += 0.025
    
    for similar_artist in similars: 
         print "\t%s %s %s" % (similar_artist.name, similar_artist.hotttnesss, similar_artist.familiarity)
  
suggestArtist(["purity ring"], 0.6)
