'''

THIS FILE HAS BEEN MADE RESPONSIBLE FOR ALL THE GPIO FUNCTIONS

#⚠️--CAUTION--⚠️#

THIS FILE IS A WORK IN PROGRESS
'''
#--DEPENDENCIES--#
#import RPi.GPIO as GPIO

class Setup():
    def __init__(self,GPIO,in1,in2,en,in3,in4,en2,TRIG,ECHO,headlights,taillights,buzzer) -> None:
        self.GPIO = GPIO
        self.in1 = in1
        self.in2 = in2
        self.en = en
        self.in3 = in3
        self.in4 = in4
        self.en2 = en2
        self.TRIG = TRIG
        self.ECHO = ECHO
        self.headlights = headlights
        self.taillights = taillights
        self.buzzer = buzzer

    def setup(self):
        self.GPIO.setmode(self.GPIO.board)
        self.GPIO.setup(self.in1,self.GPIO.OUT)
        self.GPIO.setup(self.in2,self.GPIO.OUT)
        self.GPIO.setup(self.en,self.GPIO.OUT)
        self.GPIO.setup(self.in3,self.GPIO.OUT)
        self.GPIO.setup(self.in4,self.GPIO.OUT)
        self.GPIO.setup(self.en2,self.GPIO.OUT)
        self.GPIO.setup(self.TRIG,self.GPIO.OUT)
        self.GPIO.setup(self.ECHO,self.GPIO.IN)
        self.GPIO.setup(self.headlights,self.GPIO.OUT)
        self.GPIO.setup(self.taillights,self.GPIO.OUT)
        self.GPIO.setup(self.buzzer,self.GPIO.OUT)
    

class Movement():

    def __init__(self,GPIO,in1,in2,en,in3,in4,en2,p,h) -> None:
        self.GPIO = GPIO
        self.in1 = in1
        self.in2 = in2
        self.en = en
        self.in3 = in3
        self.in4 = in4
        self.en2 = en2
        self.p = p
        self.h = h 
    

    #FRONT FUNCTION
    def move_front(self,dutyCycle) -> None:
        self.p.ChangeDutyCycle(dutyCycle)
        self.GPIO.output(self.in1,self.GPIO.HIGH)
        self.GPIO.output(self.in2,self.GPIO.LOW)

    def move_back(self,in1,in2,en,dutyCycle) -> None:
        self.p.ChangeDutyCycle(dutyCycle)
        self.GPIO.output(self.in1,self.GPIO.LOW)
        self.GPIO.output(self.in2,self.GPIO.HIGH)

    def turn_left(self) -> None:
        #COPY FROM PREVIOUS RASPI FILES
        self.p.ChangeDutyCycle(100)
        self.GPIO.output(self.in1,self.GPIO.LOW)
        self.GPIO.output(self.in3,self.GPIO.HIGH)
        self.h.ChangeDutyCycle(100)

    def turn_right(self) -> None:
        #COPY FROM PREVIOUS RASPI FILES
        self.p.ChangeDutyCycle(100)
        self.GPIO.output(self.in1,self.GPIO.HIGH)
        self.GPIO.output(self.in3,self.GPIO.LOW)

    def idle(self,gear) -> None:
        self.p.ChangeDutyCycle(40)
        if gear=='R':
            self.GPIO.output(self.in1,self.GPIO.LOW)
            self.GPIO.output(self.in2,self.GPIO.HIGH)
        elif gear=='D':
            self.GPIO.output(self.in1,self.GPIO.HIGH)
            self.GPIO.output(self.in2,self.GPIO.LOW)

    def stop(self) -> None:
        self.GPIO.output(self.in1,self.GPIO.LOW)
        self.GPIO.output(self.in2,self.GPIO.LOW)