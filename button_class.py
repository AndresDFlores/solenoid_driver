from machine import Pin


class ButtonPress:
    
    def __init__(self, pin:int):       
        self.button = Pin(pin, Pin.IN, Pin.PULL_UP)


    def get_button_pin_state(self):
        return self.button.value()
    
