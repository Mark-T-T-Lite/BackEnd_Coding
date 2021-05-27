class Song(object):
    def __init__(self, lyrics):
        self.song_lyrics = lyrics
        print("Initialized object",self)
        
    def sing_me_a_song(self):
        for line in self.song_lyrics:
            print(line)
