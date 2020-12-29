import utils
import const

def send_time(year,day, hour, mi, sec):
    """
    秒:1, 2, 3, 4, 6, 7, 8码元
    分:10, 11, 12, 13,15, 16, 17码元
    时:20, 21, 22, 23, 25, 26码元
    天:30, 31, 32, 33, 35, 36, 37, 38,40, 41码元
    起始标志(基准标志、基准标志)
    秒（个位)、分隔标志、秒（十位）、基准标志
    分（个位）、分隔标志、分（十位）、基准标志
    时（个位）、分隔标志、时（十位）、基准标志
    自当年元旦开始的天（个位）、分隔标志、天（十位）、基准标志、天（百位）、分隔标志、未编码位、基准标志
    未编码位、分隔标志、未编码位、基准标志
    时间质量标志、校验位、未编码位、基准标志、
    SBS、基准标志
    SBS、结束标志
    """
    sbs=hour*3600+min*60+sec
    utils.p_unit() #起始标志(基准标志、基准标志)
    utils.p_unit()  # Pr,起始标志
    send_sec(sec)#秒（个位)、分隔标志、秒（十位）、基准标志
    send_min(mi)#分（个位）、分隔标志、分（十位）、基准标志
    send_hour(hour)#时（个位）、分隔标志、时（十位）、基准标志
    send_day(day)#自当年元旦开始的天（个位）、分隔标志、天（十位）、基准标志、天（百位）、分隔标志、未编码位、基准标志
    send_control()#未编码位、分隔标志、未编码位、基准标志+时间质量标志、校验位、未编码位、基准标志
    send_sbs(sbs)#SBS、基准标志、SBS、结束标志


def bcd(dec) -> list:
    """
    对数字进行bcd编码
    """
    result = [0,0,0,0]
    for i in range(4):
        result[i]=dec&0b1
        dec>>=1
    return result

def send_bits(bits):
    for b in bits:
        utils.bit(b)

def send_data(data,digit=2):
    dot=1
    for i in range(digit):
        dot*=10
        unit=data%dot*10//dot#单位数字
        send_bits(bcd(unit))
        if i <digit-1:
            utils.divide()
    utils.p_unit()

def send_unit(data,digit):
    bits=[]
    low=data%10
    bits.append(*bcd(low))
    bits.append(const.division_point)
    high=data//10
    bits.append(*(bcd(high)[:-1]))


def send_sec(sec):
    send_data(sec)


def send_min(min):
    send_data(min)

def send_hour(hour):
    send_data(hour)

def send_day(day):
    send_data(day)#自当年元旦开始的天（个位）、分隔标志、天（十位）、基准标志
    #天（百位）、分隔标志、未编码位、基准标志
    send_bits(bcd(day//100))
    utils.divide()
    utils.vacancy()
    utils.p_unit()

def send_control():
    """
    未编码位、分隔标志、未编码位、基准标志+时间质量标志、校验位、未编码位、基准标志
    """
    utils.vacancy()
    utils.divide()
    utils.vacancy()
    utils.p_unit()
    utils.time_quality()
    utils.verify()
    utils.vacancy()
    utils.time_quality()

def send_sbs(num):
    """
    SBS、基准标志、SBS、结束标志
    """
    utils.sbs(num)
    utils.p_unit()
    utils.sbs(num)
    utils.p_unit()

if __name__ == "__main__":
    print(bcd(10))