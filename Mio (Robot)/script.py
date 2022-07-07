# Imports
import webiopi
from RPLCD import CharLCD
import urllib
import os
# Retrieve GPIO lib
GPIO = webiopi.GPIO

# -------------------------------------------------- #
# Constants definition                               #
# -------------------------------------------------- #

# Right motor GPIOs
R1=9 # H-Bridge 1
R2=10 # H-Bridge 2
RS=18 # H-Bridge 1,2EN

# Left motor GPIOs
L1=5 # H-Bridge 3
L2=6 # H-Bridge 4
LS=13 # H-Bridge 3,4EN

NORMAL_SPEED=1

#LCD PINS
LCD_RS=22
LCD_E=18
LCD_D4=16
LCD_D5=11
LCD_D6=40
LCD_D7=15

# -------------------------------------------------- #
# Convenient PWM Function                            #
# -------------------------------------------------- #

# Set the speed of two motors
def set_speed(speed):
    GPIO.pulseRatio(LS, speed)
    GPIO.pulseRatio(RS, speed)

# -------------------------------------------------- #
# Left Motor Functions                               #
# -------------------------------------------------- #

def left_stop():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.LOW)

def left_forward():
    GPIO.output(L1, GPIO.HIGH)
    GPIO.output(L2, GPIO.LOW)

def left_backward():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.HIGH)

def set_left_speed(speed):
    GPIO.pulseRatio(LS, speed)
    
# -------------------------------------------------- #
# Right Motor Functions                              #
# -------------------------------------------------- #
def right_stop():
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.LOW)

def right_forward():
    GPIO.output(R1, GPIO.HIGH)
    GPIO.output(R2, GPIO.LOW)

def right_backward():
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.HIGH)

def set_right_speed(speed):
    GPIO.pulseRatio(RS, speed)
# -------------------------------------------------- #
# Macro definition part                              #
# -------------------------------------------------- #
@webiopi.macro
def go_forward():
    set_speed(NORMAL_SPEED)
    left_forward()
    right_forward()
    lcd_display('      ^^^^')

@webiopi.macro
def go_backward():
    set_speed(NORMAL_SPEED)
    left_backward()
    right_backward()
    lcd_display('                      VVVV')

@webiopi.macro
def turn_left():
    set_speed(NORMAL_SPEED)
    left_backward()
    right_forward()
    lcd_display('<<              <<')
    
@webiopi.macro
def bear_left():
    set_speed(NORMAL_SPEED)
    set_left_speed(NORMAL_SPEED * 0.7)
    left_forward()
    right_forward()
    lcd_display('<<              <<')

@webiopi.macro
def turn_right():
    set_speed(NORMAL_SPEED)
    left_forward()
    right_backward()
    lcd_display('              >>              >>')

@webiopi.macro
def bear_right():
    set_speed(NORMAL_SPEED)
    set_right_speed(NORMAL_SPEED * 0.7)
    left_forward()
    right_forward()
    lcd_display('              >>              >>')

@webiopi.macro
def stop():
    left_stop()
    right_stop()
    lcd_display('      Hello!')
    
@webiopi.macro
def lcd_display(txt):
    lcd = CharLCD(cols=16, rows=2, pin_rs=LCD_RS, pin_e=LCD_E, pins_data=[LCD_D4, LCD_D5, LCD_D6, LCD_D7])
    lcd.write_string(urllib.parse.unquote(txt))

@webiopi.macro
def speak(txt):
    os.system("espeak '" + txt + "'")

# Called by WebIOPi at script loading
def setup():
    # Setup GPIOs
    GPIO.setFunction(LS, GPIO.PWM)
    GPIO.setFunction(L1, GPIO.OUT)
    GPIO.setFunction(L2, GPIO.OUT)
    
    GPIO.setFunction(RS, GPIO.PWM)
    GPIO.setFunction(R1, GPIO.OUT)
    GPIO.setFunction(R2, GPIO.OUT)
    
    set_speed(NORMAL_SPEED)
    stop()


# Called by WebIOPi at server shutdown
def destroy():
    # Reset GPIO functions
    GPIO.setFunction(LS, GPIO.IN)
    GPIO.setFunction(L1, GPIO.IN)
    GPIO.setFunction(L2, GPIO.IN)
    
    GPIO.setFunction(RS, GPIO.IN)
    GPIO.setFunction(R1, GPIO.IN)
    GPIO.setFunction(R2, GPIO.IN)
    