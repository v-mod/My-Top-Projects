import vlc
def play(fileName):
    p = vlc.MediaPlayer(fileName)
    p.play()
