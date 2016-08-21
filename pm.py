from gmusicapi import Mobileclient
from gmusicapi import Musicmanager
import json
import os.path
#defined imports ofc ;)

#set classes
mm = Musicmanager()
api = Mobileclient()

#we only do this one time, after that the oauth is saved.
#so uncomment this once, then comment it out, or set up some autologic.
#mm.perform_oauth()

#login to Musicmanager
#mm.login()

#login to Mobileclient
logged_in = api.login('timdwalton@gmail.com', '', Mobileclient.FROM_MAC_ADDRESS, 'en_us')

#get all tracks from library
tracks = api.get_all_songs()

#json decocde the songs list
out = json.dumps(tracks)

#turn the dict into a list
json_d = json.loads(out)

#set empty traks array
traks = []

mm.login()

for track in json_d:
        traks.append(track['id'])

for t in traks:
        try:
                filename, audio = mm.download_song(t)
        except:
                pass
        if os.path.isfile(filename):
                print filename
                with open(filename, 'wb') as f:
                        f.write(audio)
        else:
                print "skipped file"
