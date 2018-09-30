# Rekordboxlib.py
# Version 0.1
# Date: 2018-09-30
# Author: @vjandrea
#
# Provides some methods to work on collections exported in XML from Rekordbox

import untangle
from urllib.parse import unquote


class Rekordbox:
    def __init__(self, filename):
        self.filename = filename
        self.collection = None
        self.tracks = {}  # indexed by TrackID
        self.songs = {}  # will associate any song (artist - title) to its TrackID in the collection
        self.locations = {}  # associates any location to its TrackID

        self.load_collection()

    # this is called automatically by the constructor, so the data becomes immediately available
    def load_collection(self):
        self.collection = untangle.parse(self.filename)
        for track in self.collection.DJ_PLAYLISTS.COLLECTION.TRACK:
            self.tracks[track['TrackID']] = {
                'TrackID': track['TrackID'],
                'Name': track['Name'],
                'Artist': track['Artist'],
                'Composer': track['Composer'],
                'Grouping': track['Grouping'],
                'Genre': track['Genre'],
                'Kind': track['Kind'],
                'Size': track['Size'],
                'TotalTime': track['TotalTime'],
                'DiscNumber': track['DiscNumber'],
                'TrackNumber': track['TrackNumber'],
                'Year': track['Year'],
                'AverageBpm': track['AverageBpm'],
                'DateAdded': track['DateAdded'],
                'BitRate': track['BitRate'],
                'SampleRate': track['SampleRate'],
                'Comments': track['Comments'],
                'PlayCount': track['PlayCount'],
                'Rating': track['Rating'],
                'Location': track['Location'],
                'Remixer': track['Remixer'],
                'Tonality': track['Tonality'],
                'Label': track['Label'],
                'Mix': track['Mix']
            }

    # loads a dictionary indexed by "<Artist> - <Song>", used to find duplicates
    # the value is a list of TrackIDs that match the key
    def load_songs(self):
        for track in self.collection.DJ_PLAYLISTS.COLLECTION.TRACK:
            song = track['Artist'] + ' - ' + track['Name']
            if song not in self.songs:
                self.songs[song] = [track['TrackID']]
            else:
                self.songs[song].append(track['TrackID'])

    # loads a dictionary indexed by "<Location>", used to find duplicates
    # the associated value is a list of TrackIDs that match the location
    def load_locations(self):
        for track in self.collection.DJ_PLAYLISTS.COLLECTION.TRACK:
            location = track['Location']
            if location not in self.locations:
                self.locations[location] = [track['Location']]
            else:
                self.songs[location].append(track['Location'])

    # scans the songs dictionary and prints out the duplicate entries
    def list_duplicate_songs(self):
        if self.songs == {}:
            self.load_songs()

        for song, val in self.songs.items():
            if len(val) > 1:
                print('Duplicate: %s' % song)
                for track_id in val:
                    print('TrackID: %s' % track_id)
                    # print('Artist: %s' % self.tracks[track_id]['Artist'])
                    # print('Title: %s' % self.tracks[track_id]['Name'])
                    print(self.pretty_location(self.tracks[track_id]['Location']), " (%s bytes)" % self.tracks[track_id]['Size'])
                print()

    # formats the Location value to make it more readable
    def pretty_location(self, path):
        return unquote(path, 'utf-8')

    # prints the songs list sorted alphabetically case insensitive
    def list_sorted_songs(self):
        if self.songs == {}:
            self.load_songs()

        for song in sorted(self.songs, key=lambda s: s.lower()):
            print(song)
