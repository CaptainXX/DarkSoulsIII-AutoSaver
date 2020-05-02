#!/usr/bin/python3
# -*- coding: utf-8 -*-

import win32com.client as wc
import time, shutil, json, os

class DS3Tool():

    def __init__(self):
        with open('./config.json', 'r') as f:
            self.config = json.loads(f.read())
        self.userName = self.config['pcUserName']
        self.savePath = "./savings"
        self.savePathNotAuto = "./savings-notauto"
        self.saveInterval = self.config['saveInterval']
        self.saveMaxFiles = self.config['saveMaxFiles']

        # DarkSoulsIII数据文件路径
        self.dataPath = os.getenv("APPDATA") + "\\DarkSoulsIII"
        #self.dataPath = "C:/Users/{0}/AppData/Roaming/DarkSoulsIII".format(self.userName)
        # 已备份存档列表
        self.savingList = sorted(os.listdir('./savings'), reverse=True)
        self.savingListNotAuto = sorted(os.listdir('./savings-notauto'), reverse=True)

    def checkDS3ProcessAlive(self):
        procName = "DarkSoulsIII.exe"
        WMI = wc.GetObject('winmgmts:')
        procCodeCov = WMI.ExecQuery('select * from Win32_Process where Name like "%{}%"'.format(procName))
        
        if len(procCodeCov) > 0:
            return True
        else:
            return False

    def saveDS3Data(self):     
        timeLabel = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.path = "{0}/{1}/DarkSoulsIII".format(self.savePath, timeLabel)
        try:
            shutil.copytree(self.dataPath, self.path)
        except FileNotFoundError:
            print("Cannot find File {0}".format(self.dataPath))
        except Exception as e:
            print(e)
    
    def saveDS3dataTo(self, dst):
        self.path = "{0}/{1}/DarkSoulsIII".format(self.savePathNotAuto, dst)        
        try:
            shutil.copytree(self.dataPath, self.path)
        except FileNotFoundError:
            print("Cannot find File {0}".format(self.dataPath))
        except Exception as e:
            print(e)        

    def loadDS3Data(self, title):
        if title in self.savingList:
            self.path = "{0}/{1}/DarkSoulsIII".format(self.savePath, title)
        elif title in self.savingListNotAuto:
            self.path = "{0}/{1}/DarkSoulsIII".format(self.savePathNotAuto, title)
        prevSave = "./prev/DarkSoulsIII"
        try:
            shutil.rmtree(prevSave)
            shutil.move(self.dataPath, prevSave)
            shutil.copytree(self.path, self.dataPath)
        except Exception as e:
            print(e)

    # 递归删除备份存档，直到存档数小于想要保存的存档数: saveMaxFiles
    def checkSavingMax(self):
        self.savingListNotAuto = sorted(os.listdir('./savings-notauto'), reverse=True)
        self.savingList = sorted(os.listdir('./savings'), reverse=True)
        if len(self.savingList) > self.saveMaxFiles:
            oldestFile = self.savingList[-1]
            filepath = './savings/{0}'.format(oldestFile)
            try:
                shutil.rmtree(filepath)
            except Exception as e:
                print(e)
            self.checkSavingMax()
        
if __name__ == "__main__":
    tool = DS3Tool()
    #print(tool.checkDS3ProcessAlive())
    #tool.saveDS3Data()
    #tool.checkSavingMax()
    #tool.loadDS3Data("20200425173224")