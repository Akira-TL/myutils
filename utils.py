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
    """
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

    \033[?25h 显示光标"""
    
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
    class Log():
        debug = '\033[95m'
        warning = '\033[93m'
        info = '\033[97m'
        success = '\033[94m'
        error = '\033[91m' 

class Log:
    '''
    @说明:
        对官方log方法的改写,将文件地址写入log消息方便查看日志
    '''
    def __init__(self,name:str = 'unknow',fucname:str = 'debug') -> None:
        if '.plugins.' in name:
            name = name.split('.')[-1]
            self.is_nonebot = True
        else:self.is_nonebot = False
        self.name = name
        self.fucname = fucname.lower()
    def log(self,*text:str):
        for i in text:          
            if not self.is_nonebot:
                print(f'{Text_colors.OKGREEN}' + time.strftime('%m-%d %H:%M:%S ',time.localtime()) + f'{Text_colors.SAMPLE}[{eval(f"Text_colors.Log.{self.fucname}")}{self.fucname.upper()}{Text_colors.SAMPLE}] | {str(i)}')
            else:
                eval(f'logger.{self.fucname}')('\033[95m' + self.name + '\033[0m | ' + str(i))
__log = Log(pluginname)
_debug = Log(pluginname).log
_warning = Log(pluginname,'warning').log
_info = Log(pluginname,'info').log
_success = Log(pluginname,'success').log
_error = Log(pluginname,'error').log

if __name__ == '__main__':
    debug = Log('src.plugins.hhh').log
    debug('src.plugins.hhh')




