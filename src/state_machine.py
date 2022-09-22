import alarm, led_green, led_red, button_snooze, button_home, sensor_data_dict
import RPi.GPIO as GPIO
from send_data import send_data, send_alarm
from time import sleep
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("SERVER_URL")
DEVICE_ID = 'a7382f5c-3326-4cf8-b717-549affe1c2eb'

counter_read_data = 0
counter_send_data = 0
counter_send_alarm = 0
counter_snooze = 1
counter_red_blink = 0
counter_green_blink = 0
counter_leave_house = 0

delay_read_data = 30
delay_send_data = 120
delay_send_alarm = 600
delay_snooze = 450
delay_leave_house = 450

blink_red_status = False
blink_green_status = False
alarm_status = False
button_home_status = False
button_snooze_status = False
alarm_notification_sent = False
can_reset_home_button = False

temp = 0
motion = False

state = "DEFAULT"

HOT = 26.5
COLD = 15.3

readings_list = []

snooze_time = {}

def switcher(temp, motion, button_home_status, button_snooze_status):
    global HOT
    global COLD
    global state

    if temp >= HOT and (motion or not motion) and button_home_status == False and button_snooze_status == False:
        state = "Alarm - HOT"
    elif temp <= COLD and motion and button_home_status == False and button_snooze_status == False:
        state = "Alarm - COLD"
    elif (temp >= HOT or temp <= COLD) and (motion or not motion) and button_home_status == False and button_snooze_status == True:
        state = "Snooze - HOT or COLD"
    elif temp <= HOT and temp >= COLD and (motion or not motion) and button_home_status == True and button_snooze_status == False:
        state = "Out Of House - OK"
    elif (temp >= HOT or temp <= COLD) and not motion and button_home_status == True and (button_snooze_status == False or button_snooze_status == True):
        state = "Out Of House - HOT or COLD"
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

            ##### REGISTER BUTTON PRESS #####
            if button_snooze.pushed():
                button_snooze_status = True
                print("BUTTON SNOOZE PUSHED")

            if button_home.pushed():
                button_home_status = True
                print("BUTTON HOME PUSHED")

            ######### MANAGE SNOOZE #########
            if counter_snooze % delay_snooze == 0:
                button_snooze_status = False
                counter_snooze = 1
                print("SNOOZE OFF")

            ########### READ DATA ###########
            if counter_read_data % delay_read_data == 0:
                data = sensor_data_dict.create(alarm_status, button_home_status, button_snooze_status)
                temp = data['temperature_c']
                motion = data['motion']

                readings_list.append(data)
                print(readings_list)
                # print("------------------------------")
                # print("time:", data["created_at"])

                counter_read_data = 0

                # print("temp", temp)
                # print("HOT", HOT)
                # print("motion", motion)
                # print("button_home_status", button_home_status)
                # print("button_snooze_status", button_snooze_status)
                # print("snooze time", snooze_time)
                # print("current time", current_time)
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< READ")

            print("motion", motion)
            print("button_home_status", button_home_status)
            print("button_snooze_status", button_snooze_status)

            ########### SEND DATA ###########
            if counter_send_data % delay_send_data == 0:
                # print("............................................................SEND")
                # print(readings_list)
                print("............................................................SEND")

                # response_code = send_data(readings_list, URL, DEVICE_ID)
                # print("@@@@@@@@@@@@RESPONSE CODE: ", response_code)
                # if response_code == 200:
                #     readings_list = []
                counter_send_data = 0
            print(temp)

            ##### UPDATE SNOOZE COUNTER #####
            if button_snooze_status == True:
                counter_snooze += 1
                motion = False

            ####### RED BLINK #######
            if blink_red_status:
                counter_red_blink += 1
                led_red.on()
                if counter_red_blink % 6 == 0: # and not counter_red_blink % 18 == 0:
                    led_red.on()
                else:
                    led_red.off()

                if counter_red_blink == 6:
                    counter_red_blink = 0

            ####### GREEN BLINK #######
            if blink_green_status:
                counter_green_blink += 1
                led_green.off()
                if counter_green_blink % 6 == 0: # and not counter_green_blink % 6 == 0:
                    led_green.on()
                else:
                    led_green.off()

                if counter_green_blink == 6:
                    counter_green_blink = 0

            ######## DELAY HOME BUTTON ########
            if button_home_status == True and not can_reset_home_button:
                counter_leave_house += 1
                print(counter_leave_house)
                if counter_leave_house % delay_leave_house == 0:
                    can_reset_home_button = True
                    counter_leave_house = 0

            ######## RESET HOME BUTTON ########
            if motion and can_reset_home_button:
                button_home_status = False
                can_reset_home_button = False


            #### CHECK NOTIFICATION STATUS ####
            if alarm_notification_sent:
                counter_send_alarm += 1
                if counter_send_alarm % delay_send_alarm == 0:
                    alarm_notification_sent = False

            ##### SEND ALARM NOTIFICATION #####
            # if alarm_status and not alarm_notification_sent:
            #     text = ""
            #     if state == "Alarm - HOT":
            #         text = "It's too hot in the room! Please check on your loved one"
            #     elif state == "Alarm - COLD":
            #         text = "It's too cold in the room! Please check on your loved one"
                    
            #     alarm_notification = {"message": text}

            #     response_code = send_alarm(alarm_notification, URL, DEVICE_ID)
            #     while response_code != 200:
            #         response_code = send_alarm(alarm_notification, URL, DEVICE_ID)
            #         print(response_code, ":", "TRY AGAIN")

            #     alarm_status = False
            #     alarm_notification_sent = True

            ##### CHANGE STATE IF NEEDED ######
            switcher(temp, motion, button_home_status, button_snooze_status)

            ########## STATE MANAGER ##########
            match state:
                case "In House - OK":
                    alarm_status = alarm.off()
                    led_green.on()
                    led_red.off()
                    blink_green_status = False
                    blink_red_status = False
                    print("//////////////////////////// IN HOUSE - OK")
                case "Alarm - HOT":
                    alarm_status = alarm.on_hot()
                    led_green.off()
                    blink_green_status = False
                    blink_red_status = True
                    print("//////////////////////////// ALARM - HOT")
                case "Alarm - COLD":
                    alarm_status = alarm.on_cold()
                    led_green.off()
                    blink_green_status = False
                    blink_red_status = True
                    print("//////////////////////////// ALARM - COLD")
                case "Snooze - HOT or COLD":
                    alarm_status = alarm.off()
                    blink_green_status = True
                    blink_red_status = True
                    print("//////////////////////////// SNOOZE - HOT OR COLD")
                case "Out Of House - OK":
                    alarm_status = alarm.off()
                    # led_green.on()
                    led_red.off()
                    blink_green_status = True
                    blink_red_status = False
                    print ("//////////////////////////// OUT OF HOUSE - OK") 
                case "Out Of House - HOT or COLD":
                    alarm_status = alarm.off()
                    led_green.off()
                    blink_green_status = False
                    blink_red_status = True
                    print ("//////////////////////////// OUT OF HOUSE - TEMP HOT OR COLD") 


        except Exception as e:
            counter_read_data = 0
            print(e)

        sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()  

