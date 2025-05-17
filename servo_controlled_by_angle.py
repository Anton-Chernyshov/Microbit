from microbit import *

# Configure PWM period for servo
pin0.set_analog_period(20)

# Constants for min and max pulse widths
MIN_PULSE = 25    # Pulse for 0 degrees
MAX_PULSE = 130   # Pulse for 180 degrees

def set_servo_angle(degrees):
    """Set the servo to the given angle (0 to 180 degrees)."""
    # Clamp degrees to 0–180
    if degrees < 0:
        degrees = 0
    if degrees > 180:
        degrees = 180

    # Map degrees to PWM value
    pulse_width = MIN_PULSE + (degrees / 180) * (MAX_PULSE - MIN_PULSE)
    
    # Write the PWM value to the pin
    pin0.write_analog(int(pulse_width))

# Example usage
set_servo_angle(0)
sleep(1000)

set_servo_angle(90)
sleep(1000)

set_servo_angle(180)
sleep(1000)
