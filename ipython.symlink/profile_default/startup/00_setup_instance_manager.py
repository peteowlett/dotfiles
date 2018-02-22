import multiprocessing
import time
import logging
from aws_instance_manager.instance_manager import InstanceManager


def get_instance_manager():
    manager = InstanceManager()
    return manager


if __name__ == '__main__':
    proc = multiprocessing.Process(target=get_instance_manager)
    proc.start()
    proc.join(3)

    if proc.is_alive():
        logging.warn("Can't connect boto, InstanceManager unavailable")
        proc.terminate()
        proc.join()
    else:
        im = InstanceManager()

