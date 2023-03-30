import RPi.GPIO as GPIO
import time
import os
import boto3

button_pin = 18
s3 = boto3.resource('s3')

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def take_photo(channel):
    os.system('fswebcam -r 640x480 --no-banner /home/pi/PythonFiles/image.jpg')
    images=[('image.jpg','image')]
    for image in images:
        file = open('/home/pi/PythonFiles/' + image[0],'rb')
        object = s3.Object('iotimages2023',image[0])
        ret = object.put(Body=file, Metadata={'FullName':image[1]})
    print("Image uploaded to S3")

GPIO.add_event_detect(button_pin, GPIO.RISING, callback=take_photo, bouncetime=300)

while True:
    time.sleep(2)

