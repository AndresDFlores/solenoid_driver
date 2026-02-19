from time import sleep

from solenoid_manager import *
from button_class import *


class SolenoidApplication(SolenoidManager):    
    
    
    #  class variables
    _solenoid_pin=0
    _engage_button_pin=5
    _disengage_button_pin=28
    
    _solenoid_engage_timeout=5
    
    
    def __init__(self):
        
        #  initialize solenoid pin
        self.solenoid_class = SolenoidManager(pin=self._solenoid_pin)
        
        #  initialize button instances for the engage and disengage parameters
        self.engage_button = ButtonPress(pin=self._engage_button_pin)
        self.disengage_button = ButtonPress(pin=self._disengage_button_pin)
        
                
    def main(self):
        
        while True:            

            #  check the state of the button: 0=engage, 1=disengage
            engage_button_state = self.engage_button.get_button_pin_state()

            
            #  define solenoid pin state based on button state
            if engage_button_state == 1:
                pin_state = False
            else:        
                pin_state = True
                
            
            #  command solenoid state
            self.solenoid_class.set_engage_flag(pin_state)
            self.solenoid_class.drive_solenoid()
            

            #  if solenoid is engaged, begin disengage protocol
            if engage_button_state==0:
                
                seconds_elapsed=0
                while True:
                    
                    #  check the state of the button: 0=disengage, 1=engage
                    disengage_button_state = self.disengage_button.get_button_pin_state()
                    sleep(.01)
                    seconds_elapsed+=.01
                    
                    
                    #  if disengage button state is 0 or the engage timeout is exceeded, disengage solenoid
                    #  engage timeout is a safety parameter to ensure that the solenoid does not burn out with an extended hold time
                    if disengage_button_state==0 or seconds_elapsed>=self._solenoid_engage_timeout:
                        self.solenoid_class.set_engage_flag(False)
                        self.solenoid_class.drive_solenoid()
                        break



