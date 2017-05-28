import PyGamepad

gpad = PyGamepad.Gamepad("/dev/input/by-id/usb-0810_usb_gamepad-event-joystick")
while 1:
    print gpad.Read()

