from phue import Bridge
import speech_recognition as sr
import time


def callback(recognizer, audio): 
    try:
        data_conversion = recognizer.recognize(audio).lower().strip()        
        # Swtiching On or Off
        # On
        if data_conversion == "on" or data_conversion == "porn":          # Detects 'On' as 'Porn'. Idk why, Indian accent maybe?
            print("On")
            b.set_light(2, 'on', True)
        # Off
        elif data_conversion == "off" or data_conversion == "of":
            print("Off")
            b.set_light(2, 'on', False)        
            
        # Changing colours
        # Blue
        elif data_conversion == "blue":
            print("Blue-ish season.")
            lights[1].xy = (0.15, 0.1)
        # Green
        elif data_conversion == "green" or data_conversion == "dream":    # Detects 'Green' as 'Dream' sometimes.
            print("Greenary all-around.")
            lights[1].xy = (0.3, 0.65)  
        # Red
        elif data_conversion == "red" or data_conversion == "zedge":      # Detects 'Red' as 'zedge' sometimes.
            print("Red, it is!")
            lights[1].xy = (0.65, 0.3) 
        
        # Change in brightness
        # Decrease brightness
        elif data_conversion == "decrease brightness":
            print("Brightness decreased")
            if lights[1].brightness == 254:
                lights[1].brightness = 127
            elif lights[1].brightness == 127:
                lights[1].brightness = 1
        # Increase brightness
        elif data_conversion == "increase brightness":
            print("Brightness increased")
            if lights[1].brightness == 1:
                lights[1].brightness = 127
            elif lights[1].brightness == 127:
                lights[1].brightness = 254
     
       
        else:
            print("It was interpreted as: " + data_conversion + ". Try again.")
    except LookupError:
        print("Oops! Didn't catch that. Incorrect command. Try again.")    


if __name__ == "__main__":
    b = Bridge('192.168.1.15')
    b.connect()
    b.get_api()    
    lights = b.lights
    
    b.set_light(2, 'on', False)    
    time.sleep(3)
    r = sr.Recognizer()
    r.pause_threshold = 0.8
    r.energy_threshold = 350
    print("Speak Now!")
    r.listen_in_background(sr.Microphone(), callback)    