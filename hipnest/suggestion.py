from pyechonest import config
from pyechonest import artist
config.ECHO_NEST_API_KEY="VWFUA3PRSAGWROUNV"


def suggestArtist(seedArtists, fameLevel):
# Famelevel 0-1, 1 is Justin Bieber, 0 is a Tufts band.
  artists = []
  for a in seedArtists:
    artists.append(artist.Artist(a))
  similars = artist.similar(ids =[a.id for a in artists], results = 10, max_familiarity = fameLevel) 
  for similar_artist in similars: 
     print "\t%s" % (similar_artist.name,)

suggestArtist(["Dresden Dolls", "Weezer"], 1)
