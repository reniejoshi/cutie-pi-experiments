from gpiozero import PWMOutputDevice
from time import sleep

NOTE_C5 = 523
NOTE_E5 = 659
NOTE_G5 = 784
NOTE_A5 = 880
NOTE_D5 = 587
NOTE_D6 = 1175
NOTE_F6 = 1397

melody = [
    NOTE_C5, NOTE_E5, NOTE_G5, NOTE_E5, NOTE_C5, NOTE_E5, NOTE_G5, NOTE_E5,
    NOTE_D5, NOTE_F6, NOTE_A5, NOTE_F6, NOTE_D5, NOTE_F6, NOTE_A5, NOTE_F6,
    NOTE_A5, NOTE_C5, NOTE_E5, NOTE_C5, NOTE_A5, NOTE_C5, NOTE_E5, NOTE_C5,
    NOTE_A5, NOTE_C5, NOTE_E5, NOTE_C5, NOTE_A5, NOTE_C5, NOTE_E5, NOTE_C5
]

note_durations = [16] * len(melody)

buzzer = PWMOutputDevice(2)

def play_postal_service():
    tempo = 2.2
    
    for note, duration in zip(melody, note_durations):
        note_duration = tempo / duration
        
        buzzer.frequency = note
        buzzer.value = 0.5
        
        sleep(note_duration * 0.75)
        buzzer.value = 0
        sleep(note_duration * 0.25)

try:
    for loop in range(2):
        play_postal_service()
except KeyboardInterrupt:
    buzzer.off()
finally:
    buzzer.close()