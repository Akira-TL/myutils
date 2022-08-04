import json
from types import NoneType
from copy import deepcopy
import os,sqlite3
from utils import debug




class Sql_handle():
    '''
    需要传入文件路径实例化
    '''
    # global file_path
    def __init__(self,file_path) -> None:
        self.file_path = file_path
    def write_file(x):
        def _write_file(self,data):
            '''
            说明:送进来的data是{listname:{key1:value1,key2:value2,......},....}的格式,且value均为str
            '''
            self.check_sq_file()
            self.data = data
            a = sqlite3.connect(f'{self.file_path}')
            b = a.cursor()
            x(self,b)
            b.close()
            a.commit()
            a.close()
            # print(self.data)
        return _write_file

    @write_file
    def sq_append(self,b):
        for listname in self.data:
            keys = str(tuple(self.data[listname].keys())).replace("'","")
            values = str(tuple(self.data[listname].values()))
            try:
                b.execute(f'insert into {listname}{keys} values{values}')
            except:
                debug(f'传入数据错误,数据写入失败! -> {self.data[listname]}',__name__)

    def check_file(self):
        '''
        说说明:送进来的data是{listname:{key1:value1,key2:value2,......},....}的格式,value需要值定位类型
        '''
        try:
            with open(f'{self.file_path}','r') as f:
                pass
        except FileNotFoundError:
            try:
                os.mkdir('data')
            except:
                pass
            a = sqlite3.connect(f'{self.file_path}')
            b = a.cursor()
            self.data2 = deepcopy(self.data)
            keys = list(self.data2.keys())
            for listname in keys:
                for key in self.data2[listname]:
                    self.data2[listname][key] = key + self.get_sq_type(self.data2[listname][key])
                value = str(tuple(self.data2[listname].values())).replace("'","")
                b.execute(f'create table {listname}{value}')
            b.close()
            a.commit()
            a.close()

    def get_sq_type(self):
        if type(self.data) == str:
            return ' text'
        elif type(self.data) == int:
            return ' integer'
        elif type(self.data) == float:
            return ' real'
        elif type(self.data) == bytes:
            return ' blob'
        elif type(self.data) == NoneType:
            return ' null'

class Json_handle():
    '''
    需要传入文件路径实例化
    '''
    def __init__(self,file_path:str) -> None:
        self.file_path:str = file_path
        try:
            with open(self.file_path,'r',encoding='utf-8') as f:
                json.load(f)
        except FileNotFoundError:
            with open(self.file_path,'w',encoding='utf-8') as f:
                json.dump({},f)
        self.load()

    def load(self):
        with open(self.file_path,'r',encoding='utf-8') as f:
            self.data:dict =  json.load(f)
            return self

    def dump(self,data:dict):
        with open(self.file_path,'w',encoding='utf-8') as f:
            self.data.update(data)
            json.dump(self.data,f,ensure_ascii=False)
            return self

if __name__ == '__main__':
    a =Json_handle('test.json')
    a.dump({'listname':{'key1':'value1','key2':'value2'},'listname2':{'key1':'value1','key2':'value2'}})
