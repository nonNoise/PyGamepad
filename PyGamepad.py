# -*- coding: utf-8 -*-
############################################################
#The MIT License (MIT)
#Copyright (c) 2017 Yuta KItagami
#Project:    https://github.com/nonNoise/akilib
############################################################

import struct

class Gamepad :
    def __init__(self,fileaddr):
        input_format = 'llHHI'
        self.event_size = struct.calcsize( 'llHHI')
        try:
            self.input_file = open(fileaddr, "rb")
            self.event = self.input_file.read(self.event_size)
        except IOError:
            print "!!! Preas Set sudo and check filename . "
            exit()
    def Read(self):
        s=""
        while self.event:
            self.event = self.input_file.read(self.event_size)
            (tv_sec, tv_usec, type, code, value) = struct.unpack( 'llHHI', self.event)
            #print  (tv_sec, tv_usec, type, code, value)
            #print self.CodeCheck(type, code, value)
            s = self.CodeCheck(type, code, value) 
            if(s!= ""):
                break	
	#print s
        return s

    def CodeCheck(self,type, code, value):
        if type == 0 : #
	    pass
	#--------------------------------------#
	#左右の十字キー
	#--------------------------------------#
        if type == 3 and code == 0: 
            if(value == 0):
                return "Left"#"KEY_1"
            elif(value == 127):
                return "non"#"KEY_2"
            elif(value == 255):
                return "Right"#"KEY_3"
            else:
                return ""
	#--------------------------------------#
	#上下の十字キー
	#--------------------------------------#
        if type == 3 and code == 1: 
            if(value == 0):
                return "Up"#"KEY_1"
            elif(value == 127):
                return "non"#"KEY_2"
            elif(value == 255):
                return "Down"#"KEY_3"
            else:
                return ""
	#--------------------------------------#
	# Aボタン
	#--------------------------------------#
        if type == 1 and code == 289: 
            if(value == 0):
                return "A_off"#"KEY_1"
            elif(value == 1):
                return "A_on"#"KEY_2"
	#--------------------------------------#
	# Bボタン
	#--------------------------------------#
        if type == 1 and code == 290: 
            if(value == 0):
                return "B_off"#"KEY_1"
            elif(value == 1):
                return "B_on"#"KEY_2"
	#--------------------------------------#
	# Xボタン
	#--------------------------------------#
        if type == 1 and code == 288: 
            if(value == 0):
                return "X_off"#"KEY_1"
            elif(value == 1):
                return "X_on"#"KEY_2"
	#--------------------------------------#
	# Yボタン
	#--------------------------------------#
        if type == 1 and code == 291: 
            if(value == 0):
                return "Y_off"#"KEY_1"
            elif(value == 1):
                return "Y_on"#"KEY_2"
	#--------------------------------------#
	# Lボタン
	#--------------------------------------#
        if type == 1 and code == 292: 
            if(value == 0):
                return "L_off"#"KEY_1"
            elif(value == 1):
                return "L_on"#"KEY_2"
	#--------------------------------------#
	# Rボタン
	#--------------------------------------#
        if type == 1 and code == 294: 
            if(value == 0):
                return "R_off"#"KEY_1"
            elif(value == 1):
                return "R_on"#"KEY_2"
	#--------------------------------------#
	# STARTボタン
	#--------------------------------------#
        if type == 1 and code == 297: 
            if(value == 0):
                return "START_off"#"KEY_1"
            elif(value == 1):
                return "START_on"#"KEY_2"

	#--------------------------------------#
	# SELECTボタン
	#--------------------------------------#
        if type == 1 and code == 296: 
            if(value == 0):
                return "SELECT_off"#"KEY_1"
            elif(value == 1):
                return "SELECT_on"#"KEY_2"
        return ""
    def Close(self):
        self.input_file.close()
        return 0
