import subprocess
import json

def stars():
    """star function will create line of 50 stars"""
    line_star = ""
    for i in range (50):
        line_star += "*"
    print(line_star)

def play_song():
    """play_song function will read a json dictionary of songs and the albums they are from, 
    then print all the songs, and asks user to pick one. 
    returns album song is from and plays song for 1 minute with the option to stop the song"""
    #opens song_dict json dictionary of all songs and albums
    with open("song_dict.json", "r") as f:
        #creates song_dict dictionary
        song_dict = json.load(f)
    #initializes songs list
    songs = []
    #appends each song from song_dict dictionary
    for song in song_dict.keys():
        songs.append(song)
    #calls star function
    stars()
    #prints f string with list of songs and asks user to pick one
    print(f"Here are a list of songs: {songs}. Pick one and I will give you the album the song is on and I will also play it!")
    #calls star function
    stars()
    #user input song
    user_song= input("Pick one song: ")
    #calls star function
    stars()
    #if the user song is in songs list, prints album song is from and plays song for 1 minute unless user clicks 'control + c'
    if user_song in songs:
        album = song_dict[user_song]
        print(f"{user_song} is from the {album} album")
        print(f"{user_song} is playing now for 1 minute. If you would like for {user_song} to stop, press 'control + c!")
        subprocess.Popen(['mpg123', '-q', user_song + ".mp3"]).wait()
        
    #if user types in song that is not in list, says song is not availible
    else:
        print("Song is not availible because what you typed in is not in the given song list")
#calls play_song function
play_song()

