# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 17:49:27 2018

@author: Team #465 PlanterBot
"""
def main():
    import cv2
    import numpy as np
    import time
    import rpi
    from picamera.array import PiRGBArray
    from picamera import PiCamera

    #set the GPIO pins of raspberry pi.
    GPIO.setmode (GPIO.BCM)
    GPIO.setwarnings (False)
    #enable
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    #setting the GPIO pin as Output
    GPIO.setup (24, GPIO.OUT)
    GPIO.setup (23, GPIO.OUT)
    GPIO.setup (27, GPIO.OUT)
    GPIO.setup (22, GPIO.OUT)
    #GPIO.PWM( pin, frequency ) it generates software PWM
    PWMR = GPIO.PWM (24, 100)
    PWMR1 = GPIO.PWM (23, 100)
    PWML = GPIO.PWM (27, 100)
    PWML1 = GPIO.PWM (22, 100)
    #Starts PWM at 0% dutycycle
    PWMR.start (0)
    PWMR1.start (0)
    PWML.start (0)
    PWML1.start (0)
    #enable pins of the motor
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)

    
    camera = PiCamera()
    capture = PiRGBArray(camera,(640,480))
    camera.capture(capture, format="bgr")
    

    image = capture.array
        
    capture.set(3,320.0) #set the size
    capture.set(4,240.0)  #set the size
    capture.set(5,15)  #set the frame rate

    #set the resolution of the video to be captured
    camera.resolution = (640,480)
    #set the framerate
    cam.framerate = 30
    
    
    
    for i in range(0,2):
        flag, trash = capture.read() #starting unwanted null value


    while cv2.waitKey(1) != 27:
        flag, frame = capture.read() #read the video in frames
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#convert each frame to grayscale.
        blur=cv2.GaussianBlur(gray,(5,5),0)#blur the grayscale image
        ret,th1 = cv2.threshold(blur,35,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#using threshold remave noise
        ret1,th2 = cv2.threshold(th1,127,255,cv2.THRESH_BINARY_INV)# invert the pixels of the image frame
        _,contours, hierarchy = cv2.findContours(th2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find the contours
    #     cv2.drawContours(frame,contours,-1,(0,255,0),3)
    #     cv2.imshow('frame',frame) #show video 
        for cnt in contours:
            if cnt is not None:
                area = cv2.contourArea(cnt)# find the area of contour
            if area>=500 : #If detected area of contour is greater than 500 then it indicates Zone Indicator and thus further searches for contours shapes
            # find moment and centroid of detect contours and then search the loop for appropriate image for zone indicator to overlay
                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                rect = cv2.minAreaRect(cnt) 
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(frame,[box],0,(0,0,255),2)
                if box>=5000
                #motor stop code
                pixel = frame [cy,cx]
               if pixel[0] != 255 and pixel[1] != 255 and pixel[2] != 255:

                 x,y,w,h = cv2.boundingRect(cnt)  #compute bounding rectangle  of each contour
           
                 if pixel[0] == 254 :
                       mycolor='BLUE'  #.. I have BLUE Contour
                       
                 if pixel[1] == 127 :
                        mycolor='GREEN'  #.. I have Green Contour put Red Flower
                        overlay_image = cv2.resize(image_green,(h,w))
                 if pixel[2] == 254 :
                        mycolor='RED'  #.. I have RED Contour   
                        overlay_image = cv2.resize(image_red,(h,w))           
                
                 try:
                     if len(approx)==3:
                        myshape= "Triangle"
                     if len(approx)==4:
                        myshape= "Quadrilateral"
                     if len(approx)==5:
                        myshape= "Pentagon"
                     if len(approx)==6:
                        myshape= "Hexgaon"
                     if len(approx) > 7:
                        myshape= "CIRCLE"

                    
                     

                     
                 except:
                   print 'ERROR IN PROCESSING'
                   #Approx polyDP is used to remove shadow (noise) and thus enable us to detect pure path to follow
                     approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
                     frame[y:y+w,x:x+h,:] = blend_transparent(frame[y:y+w,x:x+h,:], overlay_image) # this will call the blend function to overlay

                time.sleep(5)  #motor will stop for 5 seconds and overlay will start
                #To detect color and shape and choosing proper image
                if mycolor=='BLUE':
                    if myshape=="Triangle":
                        overlay_image = cv2.resize('tulipblue.png',(h,w))
                    elif myshape== "Square":
                        overlay_image = cv2.resize('hydrangeablue.png',(h,w))
                    elif myshape=="Circle":
                        overlay_image = cv2.resize('orchid.png',(h,w))
                if mycolor == 'GREEN':
                    if myshape=="Triangle":
                        overlay_image = cv2.resize('hydrangeayellow.png',(h,w))
                    elif myshape== "Square":
                        overlay_image = cv2.resize('sunflower.png',(h,w))
                    elif myshape=="Circle":
                        overlay_image = cv2.resize('lily-double.png',(h,w))
                if mycolor == 'RED':
                    if myshape=="Triangle":
                        overlay_image = cv2.resize('tulipred.png',(h,w))
                    elif myshape== "Square":
                        overlay_image = cv2.resize('gerber.png',(h,w))
                    elif myshape=="Circle":
                        overlay_image = cv2.resize('carnation.png',(h,w))
                
                  
                # If Zone Indicator is not detected then Search for contour's position and decide to move accordingly
                # If cx is less than 150 means centroid detect to left so take LEFT turn
                else cx<=150:
                    l=(cx*100/160)
                    PWMR.start (0)
                    PWML.start (0)
                    PWMR1.ChangeDutyCycle (100)
                    PWML1.ChangeDutyCycle (abs(l-25))
                    time.sleep(.08)
                # If cx is greater than 170 means centroid detect to right so take RIGHT turn
       
                elif cx>=170:
                    r=((320-cx)*100/160)
                    PWMR.start (0)
                    PWML.start (0)
                    PWMR1.ChangeDutyCycle (abs(r-25))
                    PWML1.ChangeDutyCycle (100)
                    time.sleep(.08)
               # If in between this range then take a slight LEFT 
                elif cx>151 and cx<169:
                    PWMR.start (0)
                    PWML.start (0)
                    PWMR1.ChangeDutyCycle (96)
                    PWML1.ChangeDutyCycle (100)
                    time.sleep(.3)
               # ELSE carry moving forward straight direction
                else:
                    PWMR1.start (0)
                    PWML1.start (0)
                    PWMR.ChangeDutyCycle (100)
                    PWML.ChangeDutyCycle (100)
                    time.sleep(.08)
                #Continue Forward both duty cycle same 100
            else:
                PWMR1.start (0)
                PWML1.start (0)
                PWMR.ChangeDutyCycle (100)
                PWML.ChangeDutyCycle (100)
                time.sleep(.1)
        #Re initialise motor config
        PWMR.start (0)
        PWMR1.start (0)                 
        PWML.start (0)                 
        PWML1.start (0)
# ==============================================================================

def blend_transparent(face_img, overlay_t_img):
    # Split out the transparency mask from the colour info
    overlay_img = overlay_t_img[:,:,:3] # Grab the BRG planes
    overlay_mask = overlay_t_img[:,:,3:]  # And the alpha plane

    # Again calculate the inverse mask
    background_mask = 255 - overlay_mask

    # Turn the masks into three channel, so we can use them as weights
    overlay_mask = cv2.cvtColor(overlay_mask, cv2.COLOR_GRAY2BGR)
    background_mask = cv2.cvtColor(background_mask, cv2.COLOR_GRAY2BGR)

    # Create a masked out face image, and masked out overlay
    # We convert the images to floating point in range 0.0 - 1.0
    face_part = (face_img * (1 / 255.0)) * (background_mask * (1 / 255.0))
    overlay_part = (overlay_img * (1 / 255.0)) * (overlay_mask * (1 / 255.0))

    # And finally just add them together, and rescale it back to an 8bit integer image    
    return np.uint8(cv2.addWeighted(face_part, 255.0, overlay_part, 255.0, 0.0))

# ==============================================================================

    
    
    
    
    
