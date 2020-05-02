#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os, time
try:
    from PyQt5.QtCore import Qt, QEvent, QTimer
    from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, \
        QPushButton, QLineEdit, QFormLayout, QComboBox, QMessageBox, QInputDialog, \
        QHBoxLayout, QVBoxLayout, QTextEdit
    from PyQt5.QtGui import QIntValidator
except ModuleNotFoundError:
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyQt5")
    from PyQt5.QtCore import Qt, QEvent, QTimer
    from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, \
        QPushButton, QLineEdit, QFormLayout, QComboBox, QMessageBox, QInputDialog, \
        QHBoxLayout, QVBoxLayout, QTextEdit
    from PyQt5.QtGui import QIntValidator    

from ds3Tools import *
from qsses import *

class APP(QWidget):
    def __init__(self):
        self.minute = 60*1000
        self.qss = QSS()
        self.dstool = DS3Tool()
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置主窗口名称为body 方便使用qss改变样式
        self.setObjectName("body")
        self.setStyleSheet(self.qss.body)

        self.vbox = QVBoxLayout()
        self.vbox.setSpacing(20)

        self.hbox = QHBoxLayout()
        self.hbox.setSpacing(20)

        # 开始存档按钮
        self.startForm = QFormLayout()

        self.intervalLabel = QLabel("存储间隔(mins): ", self)
        self.intervalLabel.setStyleSheet(self.qss.label_h4)
        self.interval = QLineEdit()
        self.interval.setText(str(self.dstool.saveInterval))
        self.interval.setFixedSize(70, 30)
        self.interval.setStyleSheet(self.qss.input)
        self.interval.setValidator(QIntValidator(0, 65535))
        self.interval.setMaxLength(3)
        self.startForm.addRow(self.intervalLabel, self.interval)

        self.saveMaxLabel = QLabel("最大存档数: ", self)
        self.saveMaxLabel.setStyleSheet(self.qss.label_h4)
        self.saveMax = QLineEdit()
        self.saveMax.setText(str(self.dstool.saveMaxFiles))
        self.saveMax.setFixedSize(70, 30)
        self.saveMax.setStyleSheet(self.qss.input)
        self.saveMax.setValidator(QIntValidator(0, 65535))
        self.saveMax.setMaxLength(3)
        self.startForm.addRow(self.saveMaxLabel, self.saveMax)

        self.startBackup = self.initPushButtons("start")
        self.startForm.addRow(self.startBackup)
        self.infoLabel = QLabel("press start", self)
        self.infoLabel.setStyleSheet(self.qss.label_h6)
        self.startForm.addRow(self.infoLabel)

        self.hbox.addLayout(self.startForm)

        # 存档列表
        self.backupForm = QFormLayout()
        self.savesLabel = QLabel("存档列表", self)
        self.savesLabel.setStyleSheet(self.qss.label_h4)
        self.saves = QComboBox(self)
        self.saves.setFixedSize(300, 30)
        self.saves.setStyleSheet(self.qss.comboBox)
        self.saves.addItems(self.dstool.savingList)
        self.saves.addItems(self.dstool.savingListNotAuto)
        self.backupForm.addRow(self.savesLabel, self.saves)
        # 载入存档按钮
        self.loadbtn = self.initPushButtons("load")
        self.backupForm.addRow(self.loadbtn)

        # 手动存档
        self.posSaveLabel = QLabel("手动存档", self)
        self.posSaveLabel.setStyleSheet(self.qss.label_h4)
        self.posSaveBtn = self.initPushButtons("save")
        self.backupForm.addRow(self.posSaveLabel, self.posSaveBtn)
        self.hbox.addLayout(self.backupForm)

        self.vbox.addLayout(self.hbox)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        VersionText = self.qss.log_normal + "<p>DarkSoulsIII Auto Saver -version 0.0.3 Ready</p>"
        self.log.setHtml(VersionText)
        self.log.setFixedHeight(300)
        self.vbox.addWidget(self.log)

        # 初始化计时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeoutEvent)

        

        self.setLayout(self.vbox)
        self.setGeometry(300, 100, 600, 400)
        self.setWindowTitle("DarkSoulsIII Autosaver")
        self.show()

    # 鼠标划过按钮时下方Label产生提示信息
    def eventFilter(self, obj, event):
        btnEventlist = [
            QEvent.HoverEnter,
            QEvent.HoverLeave,
            QEvent.MouseButtonPress,
            QEvent.MouseButtonRelease
            ]
        if event.type() in btnEventlist:
            if obj.isEnabled():
                if event.type() == QEvent.HoverEnter:
                    name = obj.text()
                    obj.setStyleSheet(self.qss.btn_Hover)
                    btnMsg = {
                        "start": "开始自动存储",
                        "load": "载入存档",
                        "save": "存储当前进度",
                        "pause": "暂停"
                    }
                    if name in btnMsg:
                        self.infoLabel.setText(btnMsg[name])
                        self.infoLabel.setStyleSheet(self.qss.label_h6)
                    # if name == ??:
                    return True
                elif event.type() == QEvent.HoverLeave:
                    obj.setStyleSheet(self.qss.btn)
                elif event.type() == QEvent.MouseButtonPress:
                    obj.setStyleSheet(self.qss.btn_Press)
                elif event.type() == QEvent.MouseButtonRelease:
                    obj.setStyleSheet(self.qss.btn)

        return False

    # 单击ESC退出
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    # 处理单击按钮事件
    def buttonClicked(self):
        # 获取此次单击来源是哪个按钮
        sender = self.sender()
        senderName = sender.text()
        # if senderName == ??:
        if senderName == "start":
            if self.dstool.checkDS3ProcessAlive():
                self.addLog("DarkSoulsIII is Running, Start autosaving", "good")
                self.interval.setReadOnly(True)
                self.saveMax.setReadOnly(True)
                self.dstool.saveInterval = int(self.interval.text())
                self.dstool.saveMaxFiles = int(self.saveMax.text())
                self.addLog("Saving Interval: {0}mins, Max Savings: {1}".format(
                    self.dstool.saveInterval,
                    self.dstool.saveMaxFiles
                    ),"good")
                self.timeoutEvent()
                self.timer.start(self.dstool.saveInterval*self.minute)
                self.startBackup.setText("pause")
            else:
                self.addLog("DarkSoulsIII is not Running", "warning")
        elif senderName == "load":
            savingName = self.saves.currentText()
            rep = QMessageBox.question(
                self,
                '确认',
                '加载的存档为{0}, 是否确认?'.format(savingName),
                QMessageBox.Yes|QMessageBox.No,
                QMessageBox.Yes)
            if rep == QMessageBox.Yes:
                self.addLog("Saving: {0} has loaded".format(savingName), "good")
                self.dstool.loadDS3Data(savingName)

        elif senderName == "pause":
            self.timer.stop()
            self.interval.setReadOnly(False)
            self.saveMax.setReadOnly(False)
            self.addLog("Auto Saving Paused", "warning")
            self.startBackup.setText("start")
        
        elif senderName == "save":
            title, okPressed = QInputDialog.getText(self, "输入要保存的标题","存档标题:", QLineEdit.Normal, "")
            if okPressed and title in self.dstool.savingListNotAuto:
                QMessageBox.warning(
                    self,
                    "存在同名存档",
                    "存档名重复，存档失败！",
                    QMessageBox.Yes,
                    QMessageBox.Yes
                    )
                self.addLog("Manual Save failed!", "error")      
            elif okPressed and title != '':
                timeLabel = time.strftime("%m%d-%H%M%S ", time.localtime())
                title = timeLabel + title
                self.dstool.saveDS3dataTo(title)
                self.dstool.checkSavingMax()
                self.saves.clear()
                self.saves.addItems(self.dstool.savingList)
                self.saves.addItems(self.dstool.savingListNotAuto)
                self.addLog("Manual Save OK! Saving name: {0}".format(title), "good")
            elif okPressed and title == '':
                QMessageBox.warning(
                    self,
                    "输入不得为空！",
                    "输入为空，存档失败！",
                    QMessageBox.Yes,
                    QMessageBox.Yes
                    )
                self.addLog("Manual Save failed!", "error")
            

    # 设置按钮属性 应用此函数进行PushButton的初始化
    def initPushButtons(self, name: str):
        btn = QPushButton(name, self)
        btn.clicked.connect(self.buttonClicked)
        btn.installEventFilter(self)
        btn.setStyleSheet(self.qss.btn)
        return btn

    # 处理计时到时事件
    def timeoutEvent(self):
        self.addLog("Data Saved.", "normal")
        self.dstool.saveDS3Data()
        self.dstool.checkSavingMax()
        self.saves.clear()
        self.saves.addItems(self.dstool.savingList)
        self.saves.addItems(self.dstool.savingListNotAuto)
        
    def addLog(self, text, textType):
        timeLabel = time.strftime("[%H:%M:%S] ", time.localtime())
        log_text = "<p>{0}{1}</p>".format(timeLabel, text)
        types = {
            "normal": self.qss.log_normal +log_text,
            "good": self.qss.log_good + log_text,
            "warning": self.qss.log_warning + log_text,
            "error": self.qss.log_error + log_text,
        }
        if textType not in types:
            errMsg = "Unknown textType in Function addLog"
            self.log.append("<p><font color='#ff0000'>{0}{1}</font></p>".format(timeLabel, errMsg))
        else:
            self.log.append(types[textType])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = APP()
    sys.exit(app.exec_())
