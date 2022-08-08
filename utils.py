# -*- coding: utf-8 -*-
from copy import copy, deepcopy
import os
import sqlite3
import sys
import time
from types import NoneType

from nonebot.log import logger
from numpy import blackman

pluginname = __name__
class Text_colors:
    HEADER = '\033[95m'
    '''紫色'''
    OKBLUE = '\033[94m'
    '''蓝色'''
    OKGREEN = '\033[92m'
    '''翠绿'''
    WARNING = '\033[93m' 
    '''浅黄'''
    ERROR = '\033[91m' 
    '''红色'''
    SAMPLE = '\033[0m' 
    '''默认'''
    BOLD = '\033[1m' 
    '''加粗(真的有用吗)'''
    UNDERLINE = '\033[4m' 
    '''下划线'''
    TWO_UNDERLINE = '\033[21m' 
    '''双下划线'''
    OTHER = None
    r'''
    \033[nA 光标上移n行

    \033[nB 光标下移n行

    \033[nC 光标右移n行

    \033[nD 光标左移n行

    \033[y;xH设置光标位置

    \033[2J 清屏

    \033[K 清除从光标到行尾的内容

    \033[s 保存光标位置

    \033[u 恢复光标位置

    \033[?25l 隐藏光标

    \033[?25h 显示光标'''
    
    class Light():
        BLACK = '\033[90m'
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        WHITE= '\033[97m'
    class Dark():
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        PURPLE = '\033[35m'
        CYAN = '\033[36m'
        WHITE= '\033[37m'
    class Background():
        BLACK = '\033[40m'
        RED = '\033[41m'
        GREEN = '\033[42m'
        YELLOW = '\033[43m'
        BLUE = '\033[44m'
        PURPLE = '\033[45m'
        CYAN = '\033[46m'
        WHITE= '\033[47m'
    class Attributes():
        SAMPLE = '\033[0m'
        HIGH_LIGHT = '\033[1m'
        LOW_LIGHT = '\033[2m'
        MID_LIGHT = '\033[3m'
        UNDERLINE = '\033[4m'
        BLINK = '\033[5m'
        REVERSE = '\033[7m'
        ELIMINATE = '\033[8m'
        BANG = '\033[9m'
        TWO_UNDERLINE = '\033[21m' 

class Log:
    '''
    @说明:
        对官方log方法的改写,将文件地址写入log消息方便查看日志
    '''
    def __init__(self,name:str) -> None:
        self.name = name
    def debug(self,*text:str):     
        for i in text:          
            if __name__ == '__main__':
                print(f'{Text_colors.OKGREEN}' + time.strftime('%m-%d %H:%M:%S ',time.localtime()) + f'{Text_colors.SAMPLE}[{Text_colors.HEADER}DEBUG{Text_colors.SAMPLE}] | {str(i)}')
            else:
                logger.debug('\033[95m' + self.name[12:] + '\033[0m | ' + str(i))
    def warning(self,*text:str):
        for i in text:        
            if __name__ == '__main__':
                print(f'{Text_colors.OKGREEN}' + time.strftime('%m-%d %H:%M:%S ',time.localtime()) + f'{Text_colors.SAMPLE}[{Text_colors.WARNING}WARNING{Text_colors.SAMPLE}] | {str(i)}')
            else:
                logger.warning('\033[95m' + self.name[12:] + '\033[0m | ' + str(i))
    def info(self,*text:str): 
        for i in text:              
            if __name__ == '__main__':
                print(f'{Text_colors.OKGREEN}' + time.strftime('%m-%d %H:%M:%S ',time.localtime()) + f'{Text_colors.SAMPLE}[{Text_colors.Light.WHITE}INFO{Text_colors.SAMPLE}] | {str(i)}')
            else:
                logger.info('\033[95m' + self.name[12:] + '\033[0m | ' + str(i))
    def success(self,*text:str): 
        for i in text:              
            if __name__ == '__main__':
                print(f'{Text_colors.OKGREEN}' + time.strftime('%m-%d %H:%M:%S ',time.localtime()) + f'{Text_colors.SAMPLE}[{Text_colors.OKGREEN}SUCCESS{Text_colors.SAMPLE}] | {str(i)}')
            else:
                logger.success('\033[95m' + self.name[12:] + '\033[0m | ' + str(i))
    def error(self,*text:str):     
        for i in text:          
            if __name__ == '__main__':
                print(f'{Text_colors.OKGREEN}' + time.strftime('%m-%d %H:%M:%S ',time.localtime()) + f'{Text_colors.SAMPLE}[{Text_colors.ERROR}ERROR{Text_colors.SAMPLE}] | {str(i)}')
            else:
                logger.error('\033[95m' + self.name[12:] + '\033[0m | ' + str(i))
__log = Log(pluginname)
_debug = __log.debug
_warning = __log.warning
_info = __log.warning
_success = __log.success
_error = __log.error





