import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import Qt
from views.dialog.customer_detail import Ui_CustomerDetailDialog
from db.db_connection import execute_query
from utils.helpers import format_vnd
from datetime import datetime

class CustomerDetailDialog(QDialog, Ui_CustomerDetailDialog):
    def __init__(self, parent=None, customer_id=0):
        super().__init__()
        self.setupUi(self)

        self.parent = parent
        self.customer_id = customer_id

        self.customer_pet_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.customer_expense_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.customer_appointment_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.show_pet_list()
        self.show_expense_list()
        self.show_appointment_list()
        
    def show_pet_list(self):
        self.customer_pet_table.setRowCount(0)
        query = "SELECT * FROM pets WHERE customer_id = %s"
        pets = execute_query(query, (self.customer_id))

        if pets:
            for index, item in enumerate(pets):
                data = [index + 1, item['pet_no'], item['name'], item['breed'], item['birth_date'].strftime("%d/%m/%Y") if item['birth_date'] else '', item['color'], item['weight'], item['height'], item['length'], item['special_features']]
                """
                Show pet data in QTableWidget from database
                """
                new_row_count = self.customer_pet_table.rowCount() + 1
                self.customer_pet_table.setRowCount(new_row_count)
                self.customer_pet_table.verticalHeader().setVisible(False)

                for column, row_item in enumerate(data):
                    item = QTableWidgetItem(str(row_item))
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.customer_pet_table.setItem(new_row_count - 1, column, item)

    def show_expense_list(self):
        self.customer_expense_table.setRowCount(0)
        query = "SELECT * FROM expense WHERE customer_id = %s"
        expense = execute_query(query, (self.customer_id))

        if expense:
            for index, item in enumerate(expense):
                data = [index + 1, item['expense_type'], item['expense_date'].strftime("%d/%m/%Y") + ' ' + (datetime.min + item['expense_time']).time().strftime("%H:%M"), format_vnd(item['amount']), item['description']]

                """
                Show exercise data in QTableWidget from database
                """
                new_row_count = self.customer_expense_table.rowCount() + 1
                self.customer_expense_table.setRowCount(new_row_count)
                self.customer_expense_table.verticalHeader().setVisible(False)

                for column, row_item in enumerate(data):
                    item = QTableWidgetItem(str(row_item))
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled) 
                    self.customer_expense_table.setItem(new_row_count - 1, column, item)

    def show_appointment_list(self):
        self.customer_appointment_table.setRowCount(0)
        query = "SELECT * FROM appointment WHERE customer_id = %s"
        appointment = execute_query(query, (self.customer_id))

        if appointment:
            for index, item in enumerate(appointment):
                data = [index + 1, item['appointment_date'].strftime("%d/%m/%Y") + ' ' + (datetime.min + item['appointment_time']).time().strftime("%H:%M"), item['purpose']]

                """
                Show appointment data in QTableWidget from database
                """
                new_row_count = self.customer_appointment_table.rowCount() + 1
                self.customer_appointment_table.setRowCount(new_row_count)
                self.customer_appointment_table.verticalHeader().setVisible(False)

                for column, row_item in enumerate(data):
                    item = QTableWidgetItem(str(row_item))
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled) 
                    self.customer_appointment_table.setItem(new_row_count - 1, column, item)
