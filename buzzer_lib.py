from machine import Pin, PWM
import time

buzzer = PWM(Pin(20))
buzzer.duty_u16(0) 
TONES = [262, 294, 330, 349]

def play_tone(freq, duration):
    buzzer.freq(freq)
    buzzer.duty_u16(32768) 
    time.sleep(duration)
    buzzer.duty_u16(0)     
    time.sleep(0.05)       

def beep_click(idx):
    play_tone(TONES[idx], 0.1)

def beep_success():
    play_tone(523, 0.1) 
    play_tone(659, 0.1) 
    play_tone(784, 0.3) 

def beep_error():
    play_tone(150, 0.3)
    time.sleep(0.1)
    play_tone(100, 0.5)

def get_tone(idx):
    return TONES[idx]
