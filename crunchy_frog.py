from gpiozero import PWMOutputDevice
from time import sleep

NOTE_F4  = 349
NOTE_G4  = 392
NOTE_Ab4 = 415
NOTE_A4  = 440
NOTE_Bb4 = 466
NOTE_C5  = 523
NOTE_D5  = 587
NOTE_Eb5 = 622
NOTE_F5  = 698

melody = [
    NOTE_F4, NOTE_Ab4, NOTE_Bb4, 0, NOTE_Bb4, NOTE_C5, 0, NOTE_Eb5,
    NOTE_F5, 0, NOTE_Eb5, NOTE_C5, NOTE_Bb4, 0, NOTE_Ab4, NOTE_F4,
    
    NOTE_F4, NOTE_Ab4, NOTE_Bb4, 0, NOTE_Bb4, NOTE_C5, 0, NOTE_Eb5,
    NOTE_F5, NOTE_Eb5, NOTE_F5, 0, NOTE_G5 := 784, 0, NOTE_F5, 0,
    
    NOTE_C5, NOTE_Eb5, NOTE_F5, 0, NOTE_F5, NOTE_Eb5, NOTE_F5, 0,
    NOTE_Bb4, NOTE_C5, NOTE_Eb5, NOTE_C5, NOTE_Bb4, NOTE_Ab4, NOTE_F4, 0
]

note_durations = [
    8, 8, 8, 16, 16, 8, 8, 8,
    4, 16, 16, 8, 8, 8, 8, 4,
    
    8, 8, 8, 16, 16, 8, 8, 8,
    8, 8, 4, 8, 8, 8, 8, 4,
    
    8, 8, 4, 8, 8, 8, 4, 8,
    8, 8, 8, 8, 8, 8, 4, 4
]

buzzer = PWMOutputDevice(2)

def play_crunchy_frog():
    tempo = 1.6
    
    for note, duration in zip(melody, note_durations):
        note_duration = tempo / duration
        
        if note == 0:
            sleep(note_duration)
        else:
            buzzer.frequency = note
            buzzer.value = 0.5
            
            sleep(note_duration * 0.70)
            buzzer.value = 0
            sleep(note_duration * 0.30)

try:
    play_crunchy_frog()
except KeyboardInterrupt:
    buzzer.off()
finally:
    buzzer.close()
