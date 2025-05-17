from microbit import * 
# Servo control: 
# 50 = ~1 millisecond pulse all right 
# 75 = ~1.5 millisecond pulse center 
# 100 = ~2.0 millisecond pulse all left 


# Configure the analog period to 20 milliseconds (standard for servo motors)
pin0.set_analog_period(20)

# Define minimum and maximum allowed pulse widths
MIN_PULSE = 25   # Minimum safe pulse width
MAX_PULSE = 130  # Maximum safe pulse width

# Initial servo position (close to the minimum position)
motorangle = 25

def angle(num):
    # clamping function, makes sure the number num is always MIN_PULSE < num < MAX_PULSE
    if num < MIN_PULSE:
        num = MIN_PULSE
    if num > MAX_PULSE:
        num = MAX_PULSE
    return num

# Main loop to check button inputs and move the servo
while True:

    if button_a.is_pressed():
        # Button A pressed -> move servo left (decrease angle)
        motorangle -= 1
        goto = angle(motorangle)   # Clamp to valid range
        motorangle = goto          # Update angle
        pin0.write_analog(motorangle)    # Send PWM signal to servo

    elif button_b.is_pressed():
        # Button B pressed -> move servo right (increase angle)
        motorangle += 1
        goto = angle(motorangle)   # Clamp to valid range
        motorangle = goto          # Update angle
        pin0.write_analog(motorangle)    # Send PWM signal to servo

    # Small delay to prevent reading buttons too rapidly
    sleep(10)
