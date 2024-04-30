import time
import pygame

def countdown(t):
    pygame.mixer.init()
    pygame.mixer_music.load('countdown.wav')  # Load the sound effect file
    pygame.mixer_music.play()
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Time Is Up!')
    pygame.mixer.music.stop()

# Set the time in seconds
t = 65 * 5  # 5 minutes and 20 seconds

# Call the countdown function
countdown(int(t))
