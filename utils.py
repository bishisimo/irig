import time
import drive
import const

def unit(n):
    drive.gpio_high()
    time.sleep(n)
    drive.gpio_low
    time.sleep(const.pu_time-n)

def zero():
    unit(const.zero_time)

def one():
    unit(const.one_time)

def p_unit():
    unit(const.p_time)

def bit(b):
    """
    发送单个bit电平
    """
    if b==1:
        one()
    else:
        zero()

def divide():
    zero()

def vacancy():
    zero()

def time_quality():
    pass

def verify():
    pass

def sbs(sbs):
    pass