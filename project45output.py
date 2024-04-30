import pygame
import tkinter as tk

# Initialize Pygame mixer
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load("song.mp3")

# Play the MP3 file
pygame.mixer.music.play()

# Keep the program running until the music stops
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Initialize Pygame mixer
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load("song.mp3")

# Create a Tkinter window
window = tk.Tk()
window.title("MP3 Player")

# Create play/pause/stop buttons
play_button = tk.Button(window, text="Play", command=lambda: pygame.mixer.music.play())
pause_button = tk.Button(window, text="Pause", command=lambda: pygame.mixer.music.pause())
stop_button = tk.Button(window, text="Stop", command=lambda: pygame.mixer.music.stop())

# Create a volume slider
volume_slider = tk.Scale(window, from_=0, to=1, orient=tk.HORIZONTAL, command=lambda value: pygame.mixer.music.set_volume(float(value)))

# Pack the buttons and slider into the window
play_button.pack()
pause_button.pack()
stop_button.pack()
volume_slider.pack()

# Start the Tkinter event loop
window.mainloop()
