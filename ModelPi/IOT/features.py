#MOVEMENT

'''THIS FILE IS RESPOSIBLE FOR THE FEATURES OF THE CAR'''

#import RPi.GPIO as GPIO

class features:
    '''INITIALISING'''
    def __init__(self,headlights,taillights,buzzer,GPIO):
        self.headlights = headlights
        self.taillights = taillights
        self.buzzer = buzzer
        self.GPIO = GPIO

    '''HEADLIGHT TOGGLE SWITCH'''
    def headlights_toggle(self,toggle):
        if toggle==False:
            self.GPIO.output(self.headlights,False)
        elif toggle==True:
            self.GPIO.output(self.headlights,True)

    '''BRAKE LIGHT TOGGLE SWITCH'''
    def taillights_toggle(self,toggle):
        if toggle==False:
            self.GPIO.output(self.taillights,False)
        elif toggle==True:
            self.GPIO.output(self.taillights,True)

    '''BUZZER TOGGLE SWITCH'''
    def buzzer_toggle(self,toggle):
        if toggle==False:
            self.GPIO.output(self.buzzer,False)
        elif toggle==True:
            self.GPIO.output(self.buzzer,True)