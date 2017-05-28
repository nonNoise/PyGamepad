=========================================================
Python GettingGamepad
=========================================================


1.How to use
-------------------------------------------------------------------------------------------------------------

- git clone https://github.com/nonNoise/PyGamepad.git

- GamePad dreiver pass Check.
 
> ls /dev/input/by-id/

	usb-0810_usb_gamepad-event-joystick    <- This One.

	usb-0810_usb_gamepad-joystick
	
	* usb-0810_usb = Your Driver name
  
2.Example
-------------------------------------------------------------------------------------------------------------

	import PyGamepad

	gpad = PyGamepad.Gamepad("/dev/input/by-id/usb-0810_usb_gamepad-event-joystick")

	while 1:

	    print gpad.Read()



X.License
-------------------------------------------------------------------------------------------------------------

    The MIT License (MIT)
    Copyright (c) 2015 Yuta KItagami (kitagami@artifactnoise.com,@nonnoise)
