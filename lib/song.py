class Song:
    # Class variables to keep track of counts, artists, and genres
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update counts, artists, and genres on song creation
        Song.count += 1
        if artist not in Song.artists:
            Song.artists.append(artist)
        if genre not in Song.genres:
            Song.genres.append(genre)

        # Update genre count
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1

        # Update artist count
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

