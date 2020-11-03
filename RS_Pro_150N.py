#-----------------------------------------------
#Libraries
#-----------------------------------------------

#Libraries used:
#RPi.GPIO - Standard Raspberry Pi GPIO library

#Try to import the libraries and exit the program if some are missing
try:
    import RPi.GPIO as GPIO
except RuntimeError as e:
    print(e)
    sys.exit(1)


#-----------------------------------------------
#Constants
#-----------------------------------------------

#Default States
HIGH_LOCK_STATE = GPIO.HIGH
LOW_LOCK_STATE = GPIO.LOW

#Default Pins
DEFAULT_LOCK_PIN = 37 
GROUND = 39 			#Isn't used in code. Default ground pin on Raspberry Pi


#-----------------------------------------------
#Class Definition
#-----------------------------------------------

class Maglock:
  

#-----------------------------------------------
#Class Variables
#-----------------------------------------------

    #Pins
    lock_pin = None		#The GPIO pin associated with the lock. When set to the same state as lock_state, the lock will be magnetized
    
    #States
    lock_state = None		#The state which will cause the lock to be magnetized. Should be either GPIO.HIGH or GPIO.LOW
    
#Flags
#-----------------------------------------------

    lock_open = None		#Flag that indicates the lock is not magnetized when True


#-----------------------------------------------
#Functions
#-----------------------------------------------

#GPIO Functions
#-----------------------------------------------
    
    def initialize_gpio(self):
        """Initialize all the GPIO pins that the lock uses"""

        #Set GPIO mode to board
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        #Initialize lock pin 
        GPIO.setup(self.lock_pin, GPIO.OUT)
        if self.lock_open == False:
            GPIO.output(self.lock_pin,self.lock_state)
        else:
            GPIO.output(self.lock_pin,not(self.lock_state))          
    
    def cleanup_gpio(self):
        """Clears all the GPIO pins that the lock uses"""
        
        #Set GPIO mode to board
        GPIO.setmode(GPIO.BOARD)
        
        #Cleanup pins
        GPIO.cleanup(self.lock_pin)
    
    def activate_lock(self):
        """Set the lock pin to lock state"""
        
        #Set lock pin to lock state
        GPIO.output(self.lock_pin,self.lock_state)

        #Set flags
        lock_open = False
    
    def deactivate_lock(self):
        """Set the lock pin to non-lock state"""
        
        #Set lock pin to non-lock state
        GPIO.output(self.lock_pin,not(self.lock_state))

        #Set flags
        lock_open = True


#Class Initializtion Function
#-----------------------------------------------
    
    def __init__(self, lock_pin=DEFAULT_LOCK_PIN, lock_state=HIGH_LOCK_STATE, lock_open = True):
        """Constructor. Creates an object instance of this class
        Parameters:
            lock_pin (int): The GPIO pin (Board numbering) that is assigned to the lock operation
            lock_state (GPIO.HIGH or GPIO.LOW): The state which, when the lock_pin is set to that state, will result in the magnetic lock being active
            lock_open (boolean): True to initialize the object with the lock disengaged, or False to initialize the object with the lock engaged"""
        
        #Set all class variables
        self.lock_pin = lock_pin
        self.lock_state = lock_state
        self.lock_open = lock_open
        
        #Initialize GPIO
        self.initialize_gpio()
