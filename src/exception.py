# For temperature, humidity sensor
class CouldNotReadTempHumiditySensorRuntimeError(Exception):
    pass

class CouldNotReadTempHumiditySensorUnRecoverableError(Exception):
    pass

# For motion sensor
class CouldNotReadMotionSensorError(Exception):
    pass

