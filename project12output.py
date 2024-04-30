import pygame 
import time

# Initialize Pygame mixer
pygame.mixer.init()

class AlarmClock:
    def __init__(self, alarm_time):
        self.alarm_time = alarm_time
        self.is_alarm_on = False

    def set_alarm(self, alarm_time):
        self.alarm_time = alarm_time
        self.is_alarm_on = True

    def turn_off_alarm(self):
        self.is_alarm_on = False

    def play_alarm_sound(self):
        pygame.mixer.music.load("alarm_sound.mp3")
        pygame.mixer.music.play()

    def run(self):
        while True:
            current_time = time.strftime("%H:%M:%S")
            if self.is_alarm_on and current_time >= self.alarm_time:
                self.play_alarm_sound()
                user_input = input("Press Enter to turn off the alarm: ")
                if user_input == "":
                    self.turn_off_alarm()
                    break

# Example use - To get the alarm to work, you have to set it to the time  you want to be notified in HH:MM:SS format. For example, if you want to set the alarm for two minutes and it's '07:42:00', the time has to be set to '07:44:00'.
alarm_clock = AlarmClock("05:22:00")
alarm_clock.set_alarm("05:22:00")
alarm_clock.run()