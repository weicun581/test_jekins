# -*- coding: utf-8 -*-
"""
 ******************************************************************************
 *
 * COPYRIGHT:
 *   Copyright (c)  2016-2090   Realsil Technology.    All rights reserved.
 *
 *   This is unpublished proprietary source code of ******* Technology.
 *   The copyright notice above does not evidence any actual or intended *   publication of such source code.
 *
 * DESCRIPTION:
 *    Generate picture Related.
 * HISTORY:
 *   2018.3.19          Jimmy.wei           Create
 *
******************************************************************************
"""
import ui.ui_main
import sys, os, time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
# from PyQt5.QtWebEngineWidgets import *
# from PyQt5.QtWebChannel import QWebChannel

class MyForm(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = ui.ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.move(400, 200)
        self.setWindowTitle("Useful Tool (Author: Jimmy_wei @2018/8/20 10:00)")
        self.ui.lineEdit_1_1.returnPressed.connect(self.total_response)
        self.ui.lineEdit_1_3.returnPressed.connect(self.total_response)
        self.ui.lineEdit_1_5.returnPressed.connect(self.total_response)
        self.ui.lineEdit_1_7.returnPressed.connect(self.total_response)
        self.ui.lineEdit_1_9.returnPressed.connect(self.total_response)

        self.ui.lineEdit_1_2.returnPressed.connect(self.total_response)
        self.ui.lineEdit_1_4.returnPressed.connect(self.total_response)
        self.ui.lineEdit_1_6.returnPressed.connect(self.total_response)
        self.ui.lineEdit_1_8.returnPressed.connect(self.total_response)
        self.ui.lineEdit_1_10.returnPressed.connect(self.total_response)        
        # if self.ui.checkBox.isChecked():
        # QMessageBox.critical(None, "Critical", "总数据未导入！")
        # QMessageBox.information(None, "Information", "所有地区代号信息已经全部加载完毕")


    def total_response(self):
    	sender = self.sender()
    	try:
            if sender.objectName() == "lineEdit_1_1":
                value = int(self.ui.lineEdit_1_1.text(),16)
                self.ui.lineEdit_1_2.setText("%d"%value)
            elif sender.objectName() == "lineEdit_1_3":
                value = int(self.ui.lineEdit_1_3.text(),16)
                self.ui.lineEdit_1_4.setText("%d"%value)
            elif sender.objectName() == "lineEdit_1_5":
                value = int(self.ui.lineEdit_1_5.text(),16)
                self.ui.lineEdit_1_6.setText("%d"%value)
            elif sender.objectName() == "lineEdit_1_7":
                value = int(self.ui.lineEdit_1_7.text(),16)
                self.ui.lineEdit_1_8.setText("%d"%value)
            elif sender.objectName() == "lineEdit_1_9":
                value = int(self.ui.lineEdit_1_9.text(),16)
                self.ui.lineEdit_1_10.setText("%d"%value)

            elif sender.objectName() == "lineEdit_1_2":
                value = hex(int(self.ui.lineEdit_1_2.text()))
                self.ui.lineEdit_1_1.setText("%s"%value)	    
            elif sender.objectName() == "lineEdit_1_4":
                value = hex(int(self.ui.lineEdit_1_4.text()))
                self.ui.lineEdit_1_3.setText("%s"%value)
            elif sender.objectName() == "lineEdit_1_6":
                value = hex(int(self.ui.lineEdit_1_6.text()))
                self.ui.lineEdit_1_5.setText("%s"%value)
            elif sender.objectName() == "lineEdit_1_8":
                value = hex(int(self.ui.lineEdit_1_8.text()))
                self.ui.lineEdit_1_7.setText("%s"%value)                     
            elif sender.objectName() == "lineEdit_1_10":
                value = hex(int(self.ui.lineEdit_1_10.text()))
                self.ui.lineEdit_1_9.setText("%s"%value)








    	except Exception as e:
            QMessageBox.critical(None, "Critical", "信息输入格式有误！！！")

    # def start_new_thread(self):
    #     # self.str_get_folder = QFileDialog.getOpenFileName(None, "Open file dialog","/","*.csv")[0] 
    #     # self.ui.lineEdit.setText(str(self.str_get_folder))
    #     # ---for test:---
    #     self.str_get_folder = "aaaaa"
    #     self.get_thread1 = thread1(self.str_get_folder) 
    #     # QObject.connect(self.get_thread1, SIGNAL("show_state(int)"), self.show_state)  # -对线程中出现的函数进行定义，并对传入值的类型进行定义！
    #     self.get_thread1.sendData.connect(self.show_state)
    #     self.get_thread1.start()  # 开始线程！
    #     # self.get_thread0.terminate()        

    # def show_state(self,index=-2):
    #     if index == 0:
    #         self.ui.lineEdit_info.setText("数据导入进行中~")
    #         self.ui.lineEdit_info.setStyleSheet("background-color: yellow")
    #     elif index == 1:
    #         self.ui.lineEdit_info.setText("数据导入完成！")
    #         self.ui.lineEdit_info.setStyleSheet("background-color: green")
    #     elif index == -1:
    #         self.ui.lineEdit_info.setText("数据导入失败！！！")
    #         self.ui.lineEdit_info.setStyleSheet("background-color: red")

    # def stop_new_thread(self):
    #     if self.get_thread1:
    #         self.get_thread1.flag_exit=1


class thread1(QThread):
    sendData = pyqtSignal(int)
    def __init__(self,data_path=""):
        QThread.__init__(self)
        self.path = data_path
        self.flag_exit = 0

    def __del__(self):
        self.wait()

    def run(self):
        self.sendData.emit(0)
        try:
            for i in range(1000000):
                if i % 2 ==0:
                    self.sendData.emit(0)
                else:
                    self.sendData.emit(1)
                if self.flag_exit == 1:
                    break
                time.sleep(0.3)
        except Exception as e:
            print("%s---%s" % (sys._getframe().f_lineno,e))
            self.sendData.emit(-1)


# -----------------------code input----------------------------------------
def mycodestart():
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    # import sys, threading
    # sys.setrecursionlimit(100000)
    # # mycodestart()
    # threading.stack_size(200000000)
    # thread = threading.Thread(target=mycodestart)
    # thread.start()
    mycodestart()
# --------------------------------------------------------------------------