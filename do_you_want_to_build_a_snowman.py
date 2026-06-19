from gpiozero import PWMOutputDevice
from time import sleep, time

NOTE_G4  = 392
NOTE_A4  = 440
NOTE_B4  = 494
NOTE_C5  = 523
NOTE_D5  = 587
NOTE_E5  = 659
NOTE_F5  = 698
NOTE_G5  = 784

melody = [
    NOTE_G4, NOTE_G4, NOTE_G4, 0,
    NOTE_G4, NOTE_C5, NOTE_D5, NOTE_E5, NOTE_F5, NOTE_D5,
    NOTE_C5, NOTE_D5, NOTE_E5, NOTE_C5, NOTE_D5, NOTE_G4, 0,
    NOTE_G4, NOTE_C5, NOTE_D5, NOTE_E5, NOTE_F5, NOTE_D5,
    NOTE_E5, NOTE_C5, NOTE_D5, 0,    
    NOTE_B4, NOTE_C5, NOTE_D5, NOTE_B4, NOTE_C5
]

note_durations = [
    16, 16, 16, 4,
    4, 4, 4, 4, 2, 2,
    4, 4, 4, 4, 2, 2, 4,
    4, 4, 4, 4, 2, 2,
    2, 2, 2, 4,
    4, 4, 4, 4, 1
]

buzzer = PWMOutputDevice(18)

def play_snowman():
    tempo = 1.4
    
    for note, duration in zip(melody, note_durations):
        note_duration = tempo / duration
        
        if note == 0:
            sleep(note_duration)
        else:
            buzzer.frequency = note
            buzzer.value = 0.5
            
            sleep(note_duration * 0.85)
            buzzer.value = 0
            sleep(note_duration * 0.15)

try:
    play_snowman()
except KeyboardInterrupt:
    buzzer.off()
finally:
    buzzer.close()
