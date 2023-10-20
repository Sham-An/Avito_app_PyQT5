import os
import pathlib
import sys
#from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
#from PyQt5.QtCore import QUrl
from PyQt5.QtCore import *
from urllib.parse import urlparse, parse_qs
# from view_task_form_QT5_GPT import Ui_MainWindow  # изменено
# from view_task_form_QT5_GPT_tmp import Ui_MainWindow  # изменено
from view_task_form_QT5_WIN import Ui_TaskEDIT  # Ui_MainWindow  # изменено
import psycopg2
from config_PySide import params
from urllib.parse import urlparse, parse_qs
from Lib.GetHeadersPath import start_main
import app_get_headers as head_get


class Parts_union():
    pass


class MainWindow(QtWidgets.QMainWindow, Ui_TaskEDIT):  # Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Get_Task.clicked.connect(self.get_task)
        ##############################################################
        # # Привязка обработчика событий на смену строки в таблице
        # selection_model = self.tableView.selectionModel()
        # selection_model.currentChanged.connect(self.on_selection_change)
        ###############################################################
        # Настраиваем соединение с базой данных
        self.conn = psycopg2.connect(**params)
        self.cursor = self.conn.cursor()

        # Настраиваем модель таблицы
        self.model = QStandardItemModel(self.View_Task)  # tableView)
        self.View_Task.setModel(self.model)
        # self.tableView.setModel(self.model)

        # Привязка обработчика событий на смену строки в таблице
        selection_model = self.View_Task.selectionModel()
        selection_model.currentChanged.connect(self.on_selection_change)
        self.get_task()

    def check_task(self):
        # Выполняем запрос к базе данных
        query_all_task = "SELECT * FROM aparser_task"
        self.cursor.execute(query_all_task)
        # Получаем данные и имена столбцов и заполняем модель таблицы
        rows = self.cursor.fetchall()
        head_list = head_get.AvitoScraperHead()
        for row in rows:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! check', row[2])
            url2 = str(row[2])
            head_list.get_url(url2)

        #     data = [str(col) for col in row]
        #     self.model.appendRow([QStandardItem(d) for d in data])
        # self.View_Task.resizeColumnsToContents()
        # self.View_Task.setColumnWidth(0, 3)
        # self.View_Task.setColumnWidth(1, 50)
        # self.View_Task.setColumnWidth(2, 400)
        # self.View_Task.setColumnWidth(3, 0)
        # self.View_Task.setColumnHidden(3, True)
        # self.View_Task.setColumnHidden(4, True)
        # self.View_Task.setColumnWidth(4, 0)
        # self.View_Task.setColumnWidth(5, 0)

    def get_task(self):

        self.check_task()
        # Выполняем запрос к базе данных
        query_all_task = "SELECT * FROM aparser_task"
        self.cursor.execute(query_all_task)

        # Получаем данные и имена столбцов и заполняем модель таблицы
        rows = self.cursor.fetchall()
        column_names = [desc[0] for desc in self.cursor.description]
        self.model.clear()
        self.model.setColumnCount(len(column_names))
        self.model.setHorizontalHeaderLabels(column_names)
        #print(row)
        for row in rows:
            #print(row[2])
            data = [str(col) for col in row]
            self.model.appendRow([QStandardItem(d) for d in data])
        self.View_Task.resizeColumnsToContents()
        # self.View_Task.setColumnWidth(0, 3)
        # self.View_Task.setColumnWidth(1, 50)
        self.View_Task.setColumnWidth(2, 400)
        # self.View_Task.setColumnWidth(3, 0)
        self.View_Task.setColumnHidden(3, True)
        self.View_Task.setColumnHidden(4, True)
        # self.View_Task.setColumnWidth(4, 0)
        # self.View_Task.setColumnWidth(5, 0)

    def on_selection_change(self, current, previous):
        # Получаем URL из текущей строки таблицы
        # url_col = self.model.columnCount() - 1
        column = 2
        if current.row() != previous.row():
            # print('2 url new')

            url = current.sibling(current.row(), column).data()
            if isinstance(url, QUrl):
                url_str = url.toUrl()
            else:
                url_str = str(url)
            parsed_url = urlparse(url_str)
            url_parse = 'android-app://com.avito.android/ru.avito/1/items?categoryId=14&locationId=651110&priceMax=7000&priceMin=2000&query=%D1%81%D0%BA%D1%83%D1%82%D0%B5%D1%80'
            parsed_url_head = urlparse(url_parse)
            print('current.row()' , current.row(), current.column())

            print(parsed_url_head )
            print(f'parsed_url_head.query = {parsed_url_head.query}')
            query_dict_head = parse_qs(parsed_url_head.query)
            print(f'query_dict_head = {query_dict_head} \n {query_dict_head["locationId"][0]}')

            self.lineEdit.setText(url)
            self.Path_scheme.setText(parsed_url.scheme)
            self.Path_host.setText(parsed_url.netloc)
            # url_parse = setText(parsed_url.path)
            self.Path_parts.setText(parsed_url.path)
            url_parse = self.Path_parts.text()
            # print(url_parse)
            path_os = os.path.normpath(url_parse)
            split_path = path_os.split(os.sep)
            print("parsed_url ", len(split_path), " @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # print(len(split_path))
            # print(split_path)
            # head_tail = os.path.split(url_parse)
            # self.Path_local.setText(split_path[1])
            if len(split_path) == 2:
                self.Path_local.setText(split_path[1])
                # self.Path_cat1.setText(split_path[2])
                # self.Path_local.setText(split_path[1])
                # print(split_path[1],'22222222222222222222222222222222')
            elif len(split_path) == 3:
                self.Path_local.setText(split_path[1])
                self.Path_cat1.setText(split_path[2])
                # self.Path_cat2.setText(split_path[3])
                # print('33333333333333333333333333333333')
            elif len(split_path) > 3:
                self.Path_local.setText(split_path[1])
                self.Path_cat1.setText(split_path[2])
                self.Path_cat2.setText(split_path[3])
                # print('4444444444444444444444444444444444')

            # self.Path_cat1.setText(split_path[2])
            # self.Path_cat2.setText(split_path[3])
            self.list_Query.clear()
            print(parsed_url)
            query_dict = parse_qs(parsed_url.query)
            print(f'parsed_url.query = {parsed_url.query}')
            for param in query_dict:
                print(param)
                self.list_Query.addItem("{}: {}".format(param, query_dict[param][0]))
            self.Task_view_text.setText(url)  # str(current.row()))#(parsed_url.fragment)
            #View_Task
            column_index = 7#current.column()
        #self.View_Task.item(current.row(), column_index)
        #self.setData("Новые данные")

        #def setData(self, index, tasks, role):  # <--- # +++
        #     if role == Qt.EditRole:
        #         row = index.row()
        #         # column = index.column()
        #         self.tasks[row] = tasks[row]
        #         return True
        #     return False

    def closeEvent(self, event):
        # Закрываем соединение с базой данных
        self.cursor.close()
        self.conn.close()
        event.accept()


if __name__ == "__main__":
    #start_main()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

#################################################################################
# Вы можете скрыть колонку в QTableView с помощью метода setColumnHidden(). Этот метод принимает индекс столбца и состояние видимости (True для скрытия колонки и False для отображения колонки).CopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopy

# Например, чтобы скрыть вторую колонку, добавьте следующий код после установки модели таблицы:
#
# self.View_Task.setColumnHidden(1, True)
# CopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopy
# Замените 1 на индекс столбца, который нужно скрыть. Если вы хотите сделать колонку видимой снова, то вызовите setColumnHidden() с состоянием видимости False.CopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopy
#
# Также вы можете изменять ширину колонок на ноль, чтобы сделать их невидимыми. Вы можете использовать метод setColumnWidth() и передавать 0 в качестве значения ширины колонки:CopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopy
#
# self.View_Task.setColumnWidth(1, 0)
# CopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopy
# Этот код делает вторую колонку невидимой, так как ее ширина равна нулю. Обратите внимание, что можно использовать любое значение ширины колонки больше нуля, чтобы отобразить ее снова.
#
# User Avatar
# В чем различия этих методов?
# GPT Avatar
# Метод setColumnWidth() устанавливает фиксированную ширину колонок и не позволяет им расширяться или сужаться автоматически в зависимости от содержимого ячеек. Таким образом, если содержимое ячеек не помещается в заданную ширину колонки, то текст может быть обрезан или скрыт.CopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopy
#
# Метод setColumnHidden() делает колонку невидимой, так что она не отображается в таблице.
# Этот метод может быть полезен, если вы хотите временно скрыть какой-то столбец,
# но сделать его видимым снова позже.
#
# В общем случае, выбор метода зависит от вашей конкретной задачи.
# Если вы хотите, чтобы таблица автоматически адаптировалась к содержимому ячеек,
# следует запретить использование метода setColumnWidth()
# и дать таблице регулировать ширину колонок самостоятельно.
# Если вы хотите скрыть какую-то информацию или временно убрать какую-то информацию,
# используйте метод setColumnHidden().
#
# User Avatar
# чтобы таблица автоматически адаптировалась к содержимому ячеек какой метод?
# GPT Avatar
# Чтобы таблица автоматически адаптировалась к содержимому ячеек, можно использовать метод resizeColumnsToContents() объекта QTableView. Этот метод позволяет автоматически настроить ширину столбцов в соответствии с содержимым ячеек.CopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopyCopy
#
# Например, чтобы задать автоадаптивную ширину для всех колонок, можно использовать следующий код:
#
# self.View_Task.resizeColumnsToContents()
#
# Этот код измеряет содержимое каждой ячейки таблицы и настраивает ширину соответствующей колонки в соответствии с этими данными. Обратите внимание, что это может привести к изменению ширины колонок, несмотря на то, что вы могли установить их ширину ранее.
#
# User Avatar
# запретить использование метода setColumnWidth() как? Просто не использовать этот метод?
# GPT Avatar
# Да, если вы не хотите использовать метод setColumnWidth(), то вы можете не вызывать его в вашем коде. Тогда ширина колонок будет автоматически регулироваться в зависимости от содержимого ячеек, если только вы не установили для них фиксированную ширину, например, с помощью метода setFixedSize().CopyCopyCopyCopy
#
# Если вы уже использовали метод setColumnWidth() для задания ширины колонок, то вы можете отменить его действие, вызвав метод QHeaderView.reset() на экземпляре QHeaderView.CopyCopyCopyCopyCopy
#
# Например:
#
# self.View_Task.horizontalHeader().reset()
# CopyCopy
# Этот код сбросит все параметры ширины колонок и включит автоматическую
# адаптацию колонок в зависимости от содержимого ячеек.
#
#
#
