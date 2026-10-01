def light_offboard_led():
    pins.D13.digital_write(True)

forever(light_offboard_led)