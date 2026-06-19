from gpiozero import PWMOutputDevice
from time import sleep

NOTE_G4  = 392
NOTE_A4  = 440
NOTE_B4  = 494
NOTE_C5  = 523
NOTE_D5  = 587
NOTE_E5  = 659
NOTE_F5  = 698
NOTE_G5  = 784

melody = [
    NOTE_G4, NOTE_G4, NOTE_A4, NOTE_G4, NOTE_C5, NOTE_B4,
    NOTE_G4, NOTE_G4, NOTE_A4, NOTE_G4, NOTE_D5, NOTE_C5,
    NOTE_G4, NOTE_G4, NOTE_G5, NOTE_E5, NOTE_C5, NOTE_B4, NOTE_A4,
    NOTE_F5, NOTE_F5, NOTE_E5, NOTE_C5, NOTE_D5, NOTE_C5
]

note_durations = [
    8, 8, 4, 4, 4, 2,
    8, 8, 4, 4, 4, 2,
    8, 8, 4, 4, 4, 4, 4,
    8, 8, 4, 4, 4, 2
]

buzzer = PWMOutputDevice(2)

def play_melody():
    tempo = 1.3 

    for note, duration in zip(melody, note_durations):
        note_duration = tempo / duration
        
        buzzer.frequency = note
        buzzer.value = 0.5
        
        sleep(note_duration * 0.9)
        
        buzzer.value = 0
        sleep(note_duration * 0.1)

try:
    play_melody()
except KeyboardInterrupt:
    buzzer.off()
finally:
    buzzer.close()