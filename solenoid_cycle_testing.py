from solenoid_manager import *
import time


#  define test parameters
solenoid_pin = 0  # raspberry pi pico W
cycles_count = 10
seconds_per_cycle = 10


solenoid_manager_class = SolenoidManager(pin=solenoid_pin)
for engage_cycle in range(cycles_count):


    #  hold engage for defined time, seconds
    solenoid_manager_class.set_engage_flag(flag=True)
    solenoid_manager_class.drive_solenoid()

    time.sleep(seconds_per_cycle)


    #  hold disengage for defined time, seconds
    solenoid_manager_class.set_engage_flag(flag=False)
    solenoid_manager_class.drive_solenoid()

    time.sleep(seconds_per_cycle)