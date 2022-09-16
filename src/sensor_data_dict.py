from sensor_temp import get_temp
from sensor_motion import get_motion
import alarm
import button_home
from time import sleep
import datetime

def create(alarm_status, button_home_status):
    """Create data from multiple sensors

    Raises:
        e: Failed to get data from sensor

    Returns:
        dict: Dictionary of sensor data
    """
    
    try:
        sensor_temp = get_temp()
        temp_c = round(sensor_temp["temperature_c"], 1)
        temp_f = round(sensor_temp["temperature_f"], 1)
        humidity = sensor_temp["humidity"]
        motion = get_motion()
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return {
            'temperature_c': temp_c,
            'temperature_f': temp_f,
            'humidity': humidity,
            'motion': motion,
            'alarm': alarm_status,
            'button_home': button_home_status,
            'created_at': timestamp
        }

    except Exception as e:
        raise e

if __name__ == '__main__': 
    while True:
        print(create(True, True))
        sleep(2)
