import os

import yaml


#写入
def write_yaml(data):
    with open(os.getcwd()+"/extra.yaml",encoding="utf-8",mode="a+") as f:
        yaml.dump(data,stream=f,allow_unicode=True)


#读取
def read_yaml(key):
    with open(os.getcwd()+"/extra.yaml",encoding="utf-8",mode="r") as f:
        value = yaml.load(f,yaml.FullLoader)
        return value[key]

#清空yaml文件
def clear_yaml():
    with open(os.getcwd()+"/extra.yaml",encoding="utf-8",mode="w") as f:
        f.truncate()


#读取
def read_testdata(path):
    with open(path,encoding="utf-8",mode="r") as f:
        value = yaml.load(f,yaml.FullLoader)
        return value



