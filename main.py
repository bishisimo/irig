import irig
import pendulum
import time

if __name__ == "__main__":
    while True:
        t=pendulum.now()# 获取当前时间
        irig.send_time(t.year,t.day,t.hour,t.min,t.sec)
        time.sleep(1)