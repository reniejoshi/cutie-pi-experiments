from gpiozero import PWMOutputDevice
from time import sleep

NOTE_C4  = 261
NOTE_D4  = 294
NOTE_E4  = 330
NOTE_F4  = 349
NOTE_G4  = 392
NOTE_A4  = 440
NOTE_B4  = 494
NOTE_C5  = 523
NOTE_D5  = 587
NOTE_E5  = 659

melody = [
    NOTE_G4, NOTE_G4, NOTE_A4, NOTE_G4, NOTE_C5, NOTE_E5, 0,
    NOTE_G4, NOTE_G4, NOTE_A4, NOTE_G4, NOTE_D5, NOTE_C5, 0,
    NOTE_C5, NOTE_C5, NOTE_C5, NOTE_D5, NOTE_E5, NOTE_C5,
    NOTE_D5, NOTE_D5, NOTE_D5, NOTE_E5, NOTE_D5, NOTE_C5, 0,
    NOTE_G4, NOTE_G4, NOTE_A4, NOTE_G4, NOTE_C5, NOTE_E5, NOTE_D5, NOTE_C5,
    NOTE_D5, NOTE_C5, 0
]

note_durations = [
    8, 8, 4, 4, 4, 2, 8,
    8, 8, 4, 4, 4, 2, 8,
    4, 8, 8, 4, 4, 4,
    4, 8, 8, 4, 4, 4, 8,
    8, 8, 4, 4, 4, 4, 4, 4,
    2, 2, 4
]

buzzer = PWMOutputDevice(2)

def play_hakuna_matata():
    tempo = 1.4
    
    for note, duration in zip(melody, note_durations):
        note_duration = tempo / duration
        
        if note == 0:
            sleep(note_duration)
        else:
            buzzer.frequency = note
            buzzer.value = 0.5
            
            sleep(note_duration * 0.80)
            buzzer.value = 0
            sleep(note_duration * 0.20)

try:
    play_hakuna_matata()
except KeyboardInterrupt:
    buzzer.off()
finally:
    buzzer.close()
