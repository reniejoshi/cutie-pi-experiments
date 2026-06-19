from gpiozero import PWMOutputDevice
from sshkeyboard import listen_keyboard, stop_listening
from time import sleep
import threading

NOTE_A4  = 440
NOTE_B4  = 494
NOTE_C5  = 523
NOTE_D5  = 587
NOTE_E5  = 659
NOTE_F5  = 698
NOTE_G5  = 784
NOTE_A5  = 880
NOTE_B5  = 988
NOTE_C6  = 1047
NOTE_D6  = 1175
NOTE_E6  = 1319

melody = [
    NOTE_E5, NOTE_C5, NOTE_A4, NOTE_C5, NOTE_C5, NOTE_C5, NOTE_A4, NOTE_C5, NOTE_C5, NOTE_A4,
    NOTE_E5, NOTE_G5, NOTE_D6, NOTE_E6, NOTE_D6, NOTE_G5, NOTE_C6, NOTE_A5, NOTE_E6, NOTE_D6,
    NOTE_C6, 0, NOTE_C6, 0, NOTE_C6, NOTE_A5, NOTE_C6, NOTE_C6, NOTE_E6, NOTE_C6, NOTE_A5,
    NOTE_G5, 0, NOTE_C6, 0, NOTE_C6, 0, NOTE_C6, NOTE_A5, NOTE_C6, NOTE_A5, NOTE_C6, NOTE_B5, NOTE_G5,
    NOTE_F5, 0, NOTE_G5, NOTE_E5, NOTE_C5, NOTE_D5, NOTE_C5, NOTE_E5, NOTE_F5, NOTE_G5, NOTE_E5,
    NOTE_D5, 0, NOTE_C5, NOTE_D5, NOTE_E5, NOTE_G5, NOTE_E5, NOTE_D5, NOTE_E5, 
    NOTE_E6, NOTE_D6, NOTE_C6, NOTE_G5, NOTE_C6, 0, NOTE_A5, NOTE_E6, NOTE_D6,
    NOTE_C6, 0, NOTE_C6, 0, NOTE_C6, NOTE_A5, NOTE_C6, NOTE_A5, NOTE_C6, NOTE_E6, NOTE_D6, NOTE_E6
]

note_durations = [
    4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
    4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
    2, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4,
    2, 4, 2, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4,
    2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
    4, 4, 4, 4, 4, 4, 4, 4, 4,
    4, 4, 4, 4, 2, 4, 4, 4, 4,
    2, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 1
]

buzzer = PWMOutputDevice(2)
running = True

def play_minecraft():
    tempo = 1.9
    
    while running:
        for note, duration in zip(melody, note_durations):
            if not running:
                break

            note_duration = tempo / duration
            
            if note == 0:
                sleep(note_duration)
            else:
                buzzer.frequency = note
                buzzer.value = 0.5
                
                sleep(note_duration * 0.95)
                buzzer.value = 0
                sleep(note_duration * 0.05)
        
        if running:
            sleep(2)

def on_press(key):
    global running
    if key == "q":
        running = False
        stop_listening()

try:
    music_thread = threading.Thread(target=play_minecraft)
    music_thread.start()
    listen_keyboard(on_press=on_press)
except KeyboardInterrupt:
    running = False
    stop_listening()
    buzzer.off()
finally:
    buzzer.close()
