import subprocess
song_dict= {"Cruel Summer":"Lover", "Look What You Made Me Do":"Reputation", "Style":"1989", "Karma":"Midnights", "Bad Blood":"1989", "Lover":"Lover"}


def stars():
    line_star = ""
    for i in range (50):
        line_star += "*"
    print(line_star)

def play_song():
    songs = []
    for song in song_dict.keys():
        songs.append(song)
    stars()
    print(f"Here are a list of songs: {songs}. Pick one and I will give you the album the song is on and I will also play it!")
    stars()
    user_song= input("Pick one song: ")
    stars()
    if user_song in songs:
        album = song_dict[user_song]
        print(f"{user_song} is from the {album} album")
        print(f"{user_song} is playing now for 1 minute. If you would like for {user_song} to stop, press 'q'!")
        subprocess.Popen(['mpg123', '-q', user_song + ".mp3"]).wait()
        

    else:
        print("Song is not availible because what you typed in is not in the given song list")

play_song()

