#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
 
trig=10#GPIO编号
 
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(trig,GPIO.OUT,initial=GPIO.HIGH)
    pass
 
def beep(seconds):
    GPIO.output(trig,GPIO.LOW) 
    time.sleep(seconds)
    GPIO.output(trig,GPIO.HIGH) 
    
def beepBatch(seconds,timespan,counts):
    for i in range(counts):
        beep(seconds)
        time.sleep(timespan) 
     
init()
#beep(0.1)
#beepBatch(0.1,0.3,3)


CODE = {
        # 26个字母
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        # 10个数字
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
        # 16个标点符号
        ',': '--..--', '.': '.-.-.-', ':': '---...', ';': '-.-.-.',
        '?': '..--..', '=': '-...-',  "'": '.----.', '/': '-..-.',
        '!': '-.-.--', '-': '-....-', '_': '..--.-', '(': '-.--.',
        ')': '-.--.-', '$': '...-..-','&': '. . . .','@': '.--.-.'
}

  
t = 0.07 #设定间隔时间 1秒=1000毫秒
# 摩尔斯电码短音(滴)记作0，长音(嗒)记作1，使用空格区分间隔 滴(1t)、嗒(3t)、间隔(1t)、字符间隔(3t)、单词间隔(7t)

#滴
def MorseDi():
    beepBatch(t,t,1)
#嗒
def MorseTa():
    beepBatch(3*t,t,1)
  
  
def MorseCode(txt):
    if txt.isspace():
        time.sleep(t*7)#单词间隔，中断7t秒
    else:
        txt = txt.upper()
        if txt in CODE.keys():
            l = CODE[txt]
            for i in list(l):
                if i == '.':
                    MorseDi()
                elif i == '-':
                    MorseTa()


def Morse_input():
    while True:
        n = raw_input("Pls enter:\n")
        if n == "":
            break
        else:
            for s in list(n):
                MorseCode(s)
                time.sleep(t*3)#字符间隔，中断3t秒


if __name__ == "__main__":
    init()
    Morse_input()
  
GPIO.cleanup()