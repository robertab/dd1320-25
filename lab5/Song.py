"""
Kurs: DD1320/25 Tillämpad datalogi med Etik
Författare: Robert Åbert, Sara Ervik, CDATE_2.
Uppgift: Lab5.1
"""

class Song:
    """docstring for Song"""
    def __init__(self, track_id, song_id, artist, song_title):
        self.track_id = track_id
        self.song_id = song_id
        self.artist = artist
        self.song_title = song_title

    def get_track_id(self):
        return self.track_id

    def get_song_id(self):
        return self.song_title

    def get_artist(self):
        return self.artist

    def get_song_title(self):
        return song_title

    def __lt__(self, other):
        return self.artist < other.artist



