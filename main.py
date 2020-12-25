import irig
import pendulum
import time

if __name__ == "__main__":
    while True:
        t=pendulum.now()
        irig.send_time(t.day,t.hour,t.min,t.sec)
        time.sleep(1)