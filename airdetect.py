# encoding=utf-8
import time
from struct import *
import sqlite3
import serial




# 打开串口
print ("Opening Serial Port...",)
ser = serial.Serial("/dev/ttyAMA0", 9600)
print ("Done")


def main():
    cnt = 0
    conn = sqlite3.connect('pm25.db')
    c = conn.cursor()
    while True:
        # 获得接收缓冲区字符
        count = ser.inWaiting()
        if count >= 24:
            # 读取内容并回显
            recv = ser.read(count)
            cnt = cnt + 1
            print ("[%d]Recieve Data" % cnt,)
            print (len(recv), "Bytes:")
            tmp = recv[4:16]
            datas = unpack('>hhhhhh', tmp)
            print (datas)
            sql_str = """insert into pm_log ('pm1','pm2_5','pm10') values (%d,%d,%d)""" % (
                datas[0], datas[1], datas[2])
            c.execute(sql_str)
            conn.commit()
            # ser.write(recv)
            # 清空接收缓冲区
            ser.flushInput()
        # 必要的软件延时
        time.sleep(0.1)
    c.close()
    conn.close()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()
