#IMPORTING DEPENDENCIES

from flask import Flask,render_template,redirect,request
from threading import Thread, Event
from movement import Setup, Movement
import time

#---------------------#

#INITIATING REQUIREMENTS
app = Flask(__name__,template_folder="templates",static_folder="static") #INITIALISING APP FOR FLASK
exit_event = Event() #CREATING EXIT EVENT

#---------------------#

#GPIO CONFIGURATIONS

#in1
#in2
#en
#in3
#in4
#en2
#duty_cycle

#---------------------#

#DRIVE MODE INFORMATION
drivemode_info = [
    ("City",70),
    ("Eco",50),
    ("Sport",100),
]

current_drive_mode = drivemode_info[1][0]
parking_brake_engaged = "Engaged"
current_gear = 'N'
cruise_status = 'Disengaged'
#THE FUNCTION TO CALL ADAPTIVE CRUISE CONTROL
def adaptive_cruise_control():
    while True:
        if exit_event.is_set():
            pass
        elif not exit_event.is_set():
            time.sleep(1)
            print("ACC")

#ADAPTIVE CRUISE CONTROL THREAD
adaptive_cruise = Thread(target = adaptive_cruise_control)
adaptive_cruise.start()
#STOPPING THE THREAD
exit_event.set()
print(exit_event)

#THE REDIRECTER
@app.route('/')
def login():
    return redirect('/welcome')

#THE MAIN WEB PAGE
@app.route('/welcome')
def home():
    #RECIEVING AJAX DATA

    global exit_event #GLOBALISING EXIT EVENT
    global current_drive_mode
    global current_gear
    global parking_brake_engaged

    m = request.args.get("movement")
    t = request.args.get("thread")
    drive_mode = request.args.get("drive_mode")
    gear = request.args.get("transmission")
    p = request.args.get("park")
    c = request.args.get("cruise")

    
    current_gear = gear
    if p=='Engaged' or current_gear=='N':
        print("Stop")

    elif p=='Disengaged' and current_gear!='N':
        #idle
        if t=='start':
            print("came here!")
            exit_event.clear()
        elif t=='kill':
            exit_event.set()
        
        #--DRIVE MODE STUFF--#
        if drive_mode!=current_drive_mode:
            current_drive_mode=drive_mode
            print(current_drive_mode)
        elif drive_mode==current_drive_mode:
            print(current_drive_mode)
            pass

    #--MOVEMENT--#
    #if (m=='right'):
        #print("go right!")
    #elif (m=='left'):
        #print("go left!")
    #elif (m=='idle'):
        #('Idle car!')
    #elif (m=='stop'):
        #("APPLYING EMERGENCY BRAKES!")
    #elif("front"):
        #apply gas

    return render_template("welcome.html")

if __name__=='__main__':
    app.run(host='0.0.0.0')

