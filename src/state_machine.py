import alarm, led_green, led_red, button_alarm, button_home, sensor_data_dict
import RPi.GPIO as GPIO
from send_data import send_data
from time import sleep
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("SERVER_URL")
DEVICE_ID = 'a7382f5c33264cf8b717549affe1c2eb'

counter_read_data = 0
counter_send_data = 0
counter_snooze = 1

delay_read_data = 30
delay_send_data = 100
delay_snooze = 15

led_red_status = False
led_green_status = False
alarm_status = False
button_home_status = False
button_alarm_status = False

temp = 0
motion = False

state = "DEFAULT"

HOT = 29.8
COLD = 9.3

readings_list = []

snooze_time = {}

def switcher(temp, motion, button_home_status, button_alarm_status):
    global HOT
    global COLD
    global state

    if temp > HOT and motion == True and button_home_status == False and button_alarm_status == False:
        state = "Alarm - HOT"
    elif temp < COLD and motion == True and button_home_status == False and button_alarm_status == False:
        state = "Alarm - COLD"
    elif (temp > HOT or temp < COLD) and motion == True and button_home_status == False and button_alarm_status == True:
        state = "Snooze - HOT or COLD"
    elif temp < HOT and temp > COLD and motion == False and button_home_status == True and button_alarm_status == False:
        state = "Out Of House - OK"
    elif (temp > HOT or temp < COLD) and motion == False and button_home_status == True and button_alarm_status == False:
        state = "Out Of House - HOT of COLD"
    else:
        state = "In House - OK"

def get_time():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    
    return {
        "hour": hour,
        "minute": minute,
        "second": second
    }



try:
    while True:
        try:
            counter_read_data += 1
            counter_send_data += 1

            current_time = get_time()

            if button_alarm_status == True:
                counter_snooze += 1

            if button_alarm.pushed():
                button_alarm_status = True
                # snooze_time = get_time()["second"] + 10
                # if current_time["second"] == snooze_time:
                #     button_alarm_status = False

                print("BUTTON ALARM PUSHED")

            if button_home.pushed():
                button_home_status = True
                print("BUTTON HOME PUSHED")

            ######### MANAGE SNOOZE #########
            if counter_snooze % delay_snooze == 0:
                button_alarm_status = False
                counter_snooze = 1
                print("SNOOZE OFF")

            ########### READ DATA ###########
            if counter_read_data % delay_read_data == 0:
                data = sensor_data_dict.create(alarm_status, button_home_status)
                temp = data['temperature_c']
                motion = data['motion']

                readings_list.append(data)
                print(readings_list)
                print("------------------------------")

                counter_read_data = 0

                # print("temp", temp)
                # print("motion", motion)
                # print("button_home_status", button_home_status)
                # print("button_alarm_status", button_alarm_status)
                # print("-----------------")
                # print("snooze time", snooze_time)
                # print("current time", current_time)


            ########### SEND DATA ###########
            if counter_send_data % delay_send_data == 0:
                # print(URL)
                # print(DEVICE_ID)
                print("/////////////////////////SEND")
                print(readings_list)
                print("/////////////////////////SEND")


                # send_data(readings_list, URL, DEVICE_ID)
                readings_list = []
                counter_send_data = 0
            
            

            # print(".")
            if motion == True:
                button_home_status = False
            ##### CHANGE STATE IF NEEDED ######
            # print(temp)
            switcher(temp, motion, button_home_status, button_alarm_status)

            ########## STATE MANAGER ##########
            match state:
                case "In House - OK":
                    # alarm.off()
                    led_green.on()
                    led_red.off()
                    # print("//////////////////////////// IN HOUSE - OK")
                case "Alarm - HOT":
                    alarm.on_hot()
                    led_green.off()
                    led_red.blink()
                    print("//////////////////////////// ALARM - HOT")
                case "Alarm - COLD":
                    # alarm.on_cold()
                    led_green.off()
                    led_red.blink()
                    print("//////////////////////////// ALARM - COLD")
                case "Snooze - HOT or COLD":
                    alarm.off()
                    led_green.blink()
                    led_red.blink()
                    print("//////////////////////////// SNOOZE - HOT OR COLD")
                case "Out Of House - OK":
                    # alarm.off()
                    led_green.on()
                    led_red.off()
                    print ("//////////////////////////// OUT OF HOUSE - OK") 
                case "Out Of House - HOT of COLD":
                    # alarm.off()
                    led_green.off()
                    led_red.blink()
                    print ("//////////////////////////// OUT OF HOUSE - TEMP HOT OR COLD") 


        except Exception as e:
            counter_read_data = 0
            print(e)

        sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()  

