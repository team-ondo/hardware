import asyncio
import time
import socketio
import logging
import redis
from socketio.exceptions import ConnectionError


r = redis.Redis(host = 'localhost', port=6379, db=0)



def setup_logger(name: str) -> logging.Logger:
    """Set up logger.
    Args:
        name (str): name of logger.
    Returns:
        logger (logging.Logger): logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler_format = logging.Formatter(
        '[%(levelname)s]: %(asctime)s - %(name)s: %(message)s'
    )
    handler.setFormatter(handler_format)

    logger.addHandler(handler)
    logger.propagate = False
    return logger

logger = setup_logger(__name__)


sio = socketio.Client()


class HardwareNamespace(socketio.AsyncClientNamespace):
    def on_connect(self):
        logger.info("Connected")

    def on_disconnect(self):
        logger.info("Disconnected")

    def on_set_alarm_off(self):
        logger.info("Set alarm off")
        r.set("button_snooze_status", int(True))
        logger.info(f"Redis: {r.get('button_snooze_status')}")



class SocketIOClient:
    def __init__(self, url, socketio_path, namespace, device_id):
        self.url = url
        self.socketio_path = socketio_path
        self.namespace = namespace
        self.device_id = device_id
        self.sio = socketio.AsyncClient(
            reconnection=True,
            reconnection_attempts=10,
            reconnection_delay=3,
        )

    async def connect(self):
        self.sio.register_namespace(HardwareNamespace(self.namespace))
        await self.sio.connect(self.url, socketio_path=self.socketio_path,
                            namespaces=self.namespace, wait_timeout=10)
        await self.sio.emit('register_device', {
            "device_id": self.device_id
        }, namespace=self.namespace)
        await self.sio.wait()


async def main():
    sio_client = SocketIOClient(
        "https://ondo-backend-test.onrender.com",
        "/ws/socket.io",
        '/hardware',
        "a7382f5c-3326-4cf8-b717-549affe1c2eb"
    )
    while True:
        try:
            time.sleep(3)
            await sio_client.connect()
        except ConnectionError as e:
            error_message = e.args[0]
            if error_message == 'Already connected':
                pass
            logger.error(e)
        except Exception as e:
            logger.error(e)


if __name__ == '__main__':
    asyncio.run(main())