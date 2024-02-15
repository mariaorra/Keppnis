t = int(input())
listArtist = {}

for i in range(t):
    n = int(input())
    artist = input()
    lengthArtist = sum(len(word) for word in artist.split())
    listSongs = []

    for j in range(n):
        songs = input()
        lengthSongs = sum(len(word) for word in songs.split())
        if lengthArtist == lengthSongs:
            listSongs.append(songs)

    if artist in listArtist:
        listArtist[artist].append(sorted(listSongs))
    else:
        listArtist[artist] = [sorted(listSongs)]

for artist, listSongs in listArtist.items():
    for songs in listSongs:
        print(artist + ":")
        for song in songs:
            print(song)
