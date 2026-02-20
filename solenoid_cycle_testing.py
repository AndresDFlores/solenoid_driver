from solenoid_manager import *
import time


#  define test parameters
solenoid_pin = 0  # raspberry pi pico W
cycles_count = 100
seconds_per_engage_cycle = 15
seconds_per_disengage_cycle = 10
continuous_load_seconds = 30


cycle_test=True
solenoid_manager_class = SolenoidManager(pin=solenoid_pin)


if cycle_test:
    for engage_cycle in range(cycles_count):
        
        print(f'CYCLE: {engage_cycle+1}')

        #  hold engage for defined time, seconds
        solenoid_manager_class.set_engage_flag(flag=True)
        solenoid_manager_class.drive_solenoid()

        time.sleep(seconds_per_engage_cycle)


        #  hold disengage for defined time, seconds
        solenoid_manager_class.set_engage_flag(flag=False)
        solenoid_manager_class.drive_solenoid()

        time.sleep(seconds_per_disengage_cycle)


else:
    
    print(f'TIMED HOLD: {seconds_per_engage_cycle*4} seconds')
    
    
    #  hold engage for defined time, seconds
    solenoid_manager_class.set_engage_flag(flag=True)
    solenoid_manager_class.drive_solenoid()

    time.sleep(continuous_load_seconds)


    #  hold disengage for defined time, seconds
    solenoid_manager_class.set_engage_flag(flag=False)
    solenoid_manager_class.drive_solenoid()
