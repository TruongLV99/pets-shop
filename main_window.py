import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget, QHeaderView
from PyQt6.QtCore import Qt
from views.main_window_ui import Ui_MainWindow
from db.db_connection import execute_query
from views.dialog.add_pet_dialog import AddPetDialog
from views.dialog.edit_pet_dialog import EditPetDialog
from views.dialog.add_health_dialog import AddHealthDialog
from views.dialog.add_feeding_dialog import AddFeedingDialog
from views.dialog.add_exercise_dialog import AddExerciseDialog
from views.dialog.add_customer_dialog import AddCustomerDialog
from views.dialog.add_expense_dialog import AddExpenseDialog
from views.dialog.add_appointment_dialog import AddAppointmentDialog
from views.dialog.customer_detail_dialog import CustomerDetailDialog
from views.dialog.edit_customer_dialog import EditCustomerDialog
from views.dialog.edit_feeding_dialog import EditFeedingDialog
from views.dialog.edit_exercise_dialog import EditExerciseDialog
from views.dialog.edit_health_dialog import EditHealthDialog
from views.dialog.edit_expense_dialog import EditExpenseDialog
from views.dialog.edit_appointment_dialog import EditAppointmentDialog
from utils.helpers import format_vnd
from datetime import datetime
from functools import partial
from PyQt6.QtCore import QDate

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pages = self.stackedWidget
        self.pages.setCurrentIndex(1)
        self.pet_id = 0
        self.customer_id = 0

        # change window
        self.btn_menu_1.toggled.connect(
            lambda: self.do_change_page(self.btn_menu_1))
        self.btn_menu_2.toggled.connect(
            lambda: self.do_change_page(self.btn_menu_2))
        self.btn_menu_3.toggled.connect(
            lambda: self.do_change_page(self.btn_menu_3))
        self.btn_menu_4.toggled.connect(
            lambda: self.do_change_page(self.btn_menu_4))
        
        self.health_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.feeding_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.exercise_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.expense_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.appointment_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.customer_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.pet_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.total_expense_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        self.btn_search.clicked.connect(self.search_pet)
        self.btn_search_pet.clicked.connect(self.show_pet_list)
        self.btn_search_customer.clicked.connect(self.show_customer_list)
        self.btn_filter_expense.clicked.connect(lambda: self.show_total_expense(2))
        self.btn_get_all_expense.clicked.connect(lambda: self.show_total_expense(1))
        self.btn_add_customer.clicked.connect(self.open_add_customer_dialog)

        self.btn_edit.clicked.connect(lambda: self.open_edit_pet_dialog(self.pet_id))
        self.btn_cham_soc_suc_khoe.clicked.connect(self.open_add_health_dialog)
        self.btn_che_do_an_uong.clicked.connect(self.open_add_feeding_dialog)
        self.btn_hoat_dong.clicked.connect(self.open_add_exercise_dialog)
        self.btn_chi_phi.clicked.connect(self.open_add_expense_dialog)
        self.btn_lich_hen.clicked.connect(self.open_add_appointment_dialog)

        self.logoutBtn.clicked.connect(self.logout)
        
    def do_change_page(self, btn):
        """
        function for change page
        """
        btn_text = btn.text().strip()
        if btn_text == self.btn_menu_1.text().strip():
            self.pages.setCurrentIndex(1)
            # self.on_showSearchBtn_clicked()
        elif btn_text == self.btn_menu_2.text().strip():
            self.pages.setCurrentIndex(2)
            self.show_customer_list()
        elif btn_text == self.btn_menu_3.text().strip():
            self.pages.setCurrentIndex(0)
            self.show_pet_list()
        elif btn_text == self.btn_menu_4.text().strip():
            self.pages.setCurrentIndex(3)
            self.show_total_expense(1)

    # Search pet
    def search_pet(self, id=None):
        if id:
            query = "SELECT * FROM pets WHERE id = %s"
            pet = execute_query(query, (id), False)
        else:
            keyword = self.keyword_search.text()
            query = "SELECT pets.*, customers.name as customer_name, customers.phone_number FROM pets LEFT JOIN customers ON pets.customer_id = customers.id WHERE pets.pet_no = %s"
            pet = execute_query(query, (keyword), False)

        if pet:
            self.pet_id = pet['id']
            self.customer_id = pet['customer_id']
            if not id:
                self.lbl_ten_kh.setText(pet['customer_name'])
                self.lbl_sdt.setText(pet['phone_number'])
            self.lbl_ma_so.setText(pet['pet_no'])
            self.lbl_ten.setText(pet['name'])
            self.lbl_giong_loai.setText(pet['breed'])
            self.lbl_ngay_sinh.setText(pet['birth_date'].strftime("%d/%m/%Y"))
            self.lbl_mau_sac.setText(pet['color'])
            self.lbl_can_nang.setText(pet['weight'])
            self.lbl_chieu_dai.setText(pet['length'])
            self.lbl_chieu_cao.setText(pet['height'])
            self.lbl_mo_ta.setText(pet['special_features'])

            if id:
                return

            self.show_health_list()

            self.show_feeding_list()

            self.show_exercise_list()

            self.show_expense_list()

            self.show_appointment_list()
        else:
            self.dialog_success("Không tìm thấy thú cưng!")

    def show_health_list(self):
        self.health_table.setRowCount(0)
        query = "SELECT * FROM health WHERE pet_id = %s"
        health = execute_query(query, (self.pet_id))

        if health:
            for index, item in enumerate(health):
                data = [index + 1, item['vaccine_name'], item['vaccination_date'].strftime("%d/%m/%Y"), item['health_check_date'].strftime("%d/%m/%Y"), item['health_condition']]
                id = item['id']

                """
                Show health data in QTableWidget from database
                """
                new_row_count = self.health_table.rowCount() + 1
                self.health_table.setRowCount(new_row_count)
                self.health_table.verticalHeader().setVisible(False)

                for column, row_item in enumerate(data):
                    item = QTableWidgetItem(str(row_item))
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled) 
                    self.health_table.setItem(new_row_count - 1, column, item)

                btn_widget = self.add_btn_edit_delete(index, id, 'health')
                
                self.health_table.setCellWidget(index, 5, btn_widget)

    def show_feeding_list(self):
        self.feeding_table.setRowCount(0)
        query = "SELECT * FROM feeding WHERE pet_id = %s"
        feeding = execute_query(query, (self.pet_id))

        if feeding:
            for index, item in enumerate(feeding):
                data = [index + 1, item['food_type'], item['feeding_date'].strftime("%d/%m/%Y"), item['quantity']]
                id = item['id']

                """
                Show feeding data in QTableWidget from database
                """
                new_row_count = self.feeding_table.rowCount() + 1
                self.feeding_table.setRowCount(new_row_count)
                self.feeding_table.verticalHeader().setVisible(False)

                for column, row_item in enumerate(data):
                    item = QTableWidgetItem(str(row_item))
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled) 
                    self.feeding_table.setItem(new_row_count - 1, column, item)

                btn_widget = self.add_btn_edit_delete(index, id, 'feeding')
                
                self.feeding_table.setCellWidget(index, 4, btn_widget)

    def show_exercise_list(self):
        self.exercise_table.setRowCount(0)
        query = "SELECT * FROM exercise WHERE pet_id = %s"
        exercise = execute_query(query, (self.pet_id))

        if exercise:
            for index, item in enumerate(exercise):
                data = [index + 1, item['activity_type'], item['exercise_date'].strftime("%d/%m/%Y"), item['duration']]
                id = item['id']

                """
                Show exercise data in QTableWidget from database
                """
                new_row_count = self.exercise_table.rowCount() + 1
                self.exercise_table.setRowCount(new_row_count)
                self.exercise_table.verticalHeader().setVisible(False)

                for column, row_item in enumerate(data):
                    item = QTableWidgetItem(str(row_item))
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled) 
                    self.exercise_table.setItem(new_row_count - 1, column, item)

                btn_widget = self.add_btn_edit_delete(index, id, 'exercise')
                
                self.exercise_table.setCellWidget(index, 4, btn_widget)

    def show_expense_list(self):
        self.expense_table.setRowCount(0)
        query = "SELECT * FROM expense WHERE pet_id = %s"
        expense = execute_query(query, (self.pet_id))

        if expense:
            for index, item in enumerate(expense):
                data = [index + 1, item['expense_type'], item['expense_date'].strftime("%d/%m/%Y") + ' ' + (datetime.min + item['expense_time']).time().strftime("%H:%M"), format_vnd(item['amount']), item['description']]
                id = item['id']

                """
                Show exercise data in QTableWidget from database
                """
                new_row_count = self.expense_table.rowCount() + 1
                self.expense_table.setRowCount(new_row_count)
                self.expense_table.verticalHeader().setVisible(False)

                for column, row_item in enumerate(data):
                    item = QTableWidgetItem(str(row_item))
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled) 
                    self.expense_table.setItem(new_row_count - 1, column, item)

                btn_widget = self.add_btn_edit_delete(index, id, 'expense')
                
                self.expense_table.setCellWidget(index, 5, btn_widget)

    def show_appointment_list(self):
        self.appointment_table.setRowCount(0)
        query = "SELECT * FROM appointment WHERE pet_id = %s"
        appointment = execute_query(query, (self.pet_id))

        if appointment:
            for index, item in enumerate(appointment):
                data = [index + 1, item['appointment_date'].strftime("%d/%m/%Y") + ' ' + (datetime.min + item['appointment_time']).time().strftime("%H:%M"), item['purpose']]
                id = item['id']

                """
                Show appointment data in QTableWidget from database
                """
                new_row_count = self.appointment_table.rowCount() + 1
                self.appointment_table.setRowCount(new_row_count)
                self.appointment_table.verticalHeader().setVisible(False)

                for column, row_item in enumerate(data):
                    item = QTableWidgetItem(str(row_item))
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled) 
                    self.appointment_table.setItem(new_row_count - 1, column, item)

                btn_widget = self.add_btn_edit_delete(index, id, 'appointment')
                
                self.appointment_table.setCellWidget(index, 3, btn_widget)

    def show_pet_list(self):
        self.pet_table.setRowCount(0)
        keyword = self.keyword_search_pet.text()
        query = "SELECT pets.*, customers.name as customer_name, customers.phone_number FROM pets LEFT JOIN customers ON pets.customer_id = customers.id"
        params = []

        if keyword:
            query += " WHERE pets.pet_no LIKE %s OR pets.name LIKE %s OR pets.breed LIKE %s OR pets.color LIKE %s"
            params.extend([f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"])

        pets = execute_query(query, tuple(params))

        if pets:
            for index, item in enumerate(pets):
                data = [index + 1, item['customer_name'], item['phone_number'], item['pet_no'], item['name'], item['breed'], item['birth_date'].strftime("%d/%m/%Y") if item['birth_date'] else '', item['color'], item['weight'], item['height'], item['length'], item['special_features']]
                id = item['id']

                """
                Show pet data in QTableWidget from database
                """
                new_row_count = self.pet_table.rowCount() + 1
                self.pet_table.setRowCount(new_row_count)
                self.pet_table.verticalHeader().setVisible(False)

                for column, row_item in enumerate(data):
                    item = QTableWidgetItem(str(row_item))
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.pet_table.setItem(new_row_count - 1, column, item)

                btn_widget = self.add_btn_edit_delete(index, id, 'pets')
                
                self.pet_table.setCellWidget(index, 12, btn_widget)

    def show_total_expense(self, type = 1):
        self.total_expense_table.setRowCount(0)
        query = "SELECT * FROM expense"
        params = []
        total = 0

        if type == 2:
            date_from = self.date_from.date().toPyDate()
            date_to = self.date_to.date().toPyDate()
            query += " WHERE expense_date BETWEEN %s AND %s"
            params.extend([date_from, date_to])
            
        expense = execute_query(query, tuple(params))

        if expense:
            for index, item in enumerate(expense):
                total += item['amount']
                data = [index + 1, item['expense_type'], item['expense_date'].strftime("%d/%m/%Y") if item['expense_date'] else item['created_at'].strftime("%d/%m/%Y"), format_vnd(item['amount']), item['description']]
                """
                Show pet data in QTableWidget from database
                """
                new_row_count = self.total_expense_table.rowCount() + 1
                self.total_expense_table.setRowCount(new_row_count)
                self.total_expense_table.verticalHeader().setVisible(False)

                for column, row_item in enumerate(data):
                    item = QTableWidgetItem(str(row_item))
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.total_expense_table.setItem(new_row_count - 1, column, item)

        self.lbl_tong_doanh_thu.setText('Tổng: ' + format_vnd(total))

    def open_add_pet_dialog(self, customer_id):
        edit_pet_dialog = AddPetDialog(self, customer_id)
        result = edit_pet_dialog.exec()

        if result == AddPetDialog.accepted:
            pass  

    def open_edit_pet_dialog(self, id, reloadList = False):
        if id:
            query = "SELECT * FROM pets WHERE id = %s"
            pet = execute_query(query, (id), False)

            if pet: 
                edit_pet_dialog = EditPetDialog(self, pet, reloadList)
                result = edit_pet_dialog.exec()

                if result == EditPetDialog.accepted:
                    pass

    def add_pet(self, add_data):
            query = "INSERT INTO pets (customer_id, name, breed, birth_date, color, weight, height, length, special_features) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            pet_id = execute_query(query, (add_data['customer_id'], add_data['name'], add_data['breed'], add_data['birth_date'], add_data['color'], add_data['weight'], add_data['height'], add_data['length'], add_data['special_features']))

            if pet_id:
                pet_no = f"P{pet_id:06d}"
                query_update = "UPDATE pets SET pet_no = %s WHERE id = %s"
                execute_query(query_update, (pet_no, pet_id))
                self.dialog_success("Thêm thú cưng thành công!")

    def update_pet(self, updated_data, reloadList = False):
        if self.pet_id or reloadList:
            query = "UPDATE pets SET name = %s, breed = %s, birth_date = %s, color = %s, weight = %s, height = %s, length = %s, special_features = %s WHERE id = %s"
            pet = execute_query(query, (updated_data['name'], updated_data['breed'], updated_data['birth_date'], updated_data['color'], updated_data['weight'], updated_data['height'], updated_data['length'], updated_data['special_features'], updated_data['id']))

            if pet:
                if reloadList:
                    self.show_pet_list()
                else:
                    self.search_pet(updated_data['id'])

                self.dialog_success("Cập nhật thú cưng thành công!")

    def open_add_health_dialog(self):
        if self.pet_id:
            add_health_dialog = AddHealthDialog(self)
            result = add_health_dialog.exec()

            if result == AddHealthDialog.accepted:
                pass

    def add_health(self, add_data):
        if self.pet_id:
            query = "INSERT INTO health (pet_id, vaccine_name, vaccination_date, health_check_date, health_condition) VALUES (%s, %s, %s, %s, %s)"
            health = execute_query(query, (self.pet_id, add_data['vaccine_name'], add_data['vaccination_date'], add_data['health_check_date'], add_data['health_condition']))
            
            if health:
                self.show_health_list()
                self.dialog_success("Thêm chăm sóc sức khỏe thành công!")

    def open_add_feeding_dialog(self):
        if self.pet_id:
            add_feeding_dialog = AddFeedingDialog(self)
            result = add_feeding_dialog.exec()

            if result == AddFeedingDialog.accepted:
                pass

    def add_feeding(self, add_data):
        if self.pet_id:
            query = "INSERT INTO feeding (pet_id, food_type, feeding_date, feeding_time, quantity) VALUES (%s, %s, %s, %s, %s)"
            feeding = execute_query(query, (self.pet_id, add_data['food_type'], add_data['feeding_date'], add_data['feeding_time'], add_data['quantity']))
            
            if feeding:
                self.show_feeding_list()
                self.dialog_success("Thêm chế độ ăn uống thành công!")

    def open_add_exercise_dialog(self):
        if self.pet_id:
            add_exercise_dialog = AddExerciseDialog(self)
            result = add_exercise_dialog.exec()

            if result == AddExerciseDialog.accepted:
                pass

    def add_exercise(self, add_data):
        if self.pet_id:
            query = "INSERT INTO exercise (pet_id, activity_type, exercise_date, exercise_time, duration) VALUES (%s, %s, %s, %s, %s)"
            exercise = execute_query(query, (self.pet_id, add_data['activity_type'], add_data['exercise_date'], add_data['exercise_time'], add_data['duration']))
            
            if exercise:
                self.show_exercise_list()
                self.dialog_success("Thêm hoạt động thành công!")

    def open_add_expense_dialog(self):
        if self.pet_id:
            add_expense_dialog = AddExpenseDialog(self)
            result = add_expense_dialog.exec()

            if result == AddExpenseDialog.accepted:
                pass

    def add_expense(self, add_data):
        if self.pet_id:
            query = "INSERT INTO expense (customer_id, pet_id, expense_type, expense_date, expense_time, amount, description) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            exercise = execute_query(query, (self.customer_id, self.pet_id, add_data['expense_type'], add_data['expense_date'], add_data['expense_time'], add_data['amount'], add_data['description']))
            
            if exercise:
                self.show_expense_list()
                self.dialog_success("Thêm chi phí thành công!")

    def open_add_appointment_dialog(self):
        if self.pet_id:
            add_appointment_dialog = AddAppointmentDialog(self)
            result = add_appointment_dialog.exec()

            if result == AddAppointmentDialog.accepted:
                pass

    def add_appointment(self, add_data):
        if self.pet_id:
            query = "INSERT INTO appointment (customer_id, pet_id, appointment_date, appointment_time, purpose) VALUES (%s, %s, %s, %s, %s)"
            exercise = execute_query(query, (self.customer_id, self.pet_id, add_data['appointment_date'], add_data['appointment_time'], add_data['purpose']))
            
            if exercise:
                self.show_appointment_list()
                self.dialog_success("Thêm lịch hẹn thành công!")

    # Customer
    def show_customer_list(self):
        self.customer_table.setRowCount(0)
        keyword = self.keyword_search_customer.text()
        query = "SELECT * FROM customers"
        params = []

        if keyword:
            query += " WHERE name LIKE %s OR phone_number LIKE %s"
            params.extend([f"%{keyword}%", f"%{keyword}%"])

        customers = execute_query(query, tuple(params))

        if customers:
            for index, item in enumerate(customers):
                data = [index + 1, item['name'], item['phone_number']]
                id = item['id']
                """
                Show customer data in QTableWidget from database
                """
                new_row_count = self.customer_table.rowCount() + 1
                self.customer_table.setRowCount(new_row_count)
                self.customer_table.verticalHeader().setVisible(False)

                for column, row_item in enumerate(data):
                    item = QTableWidgetItem(str(row_item))
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.customer_table.setItem(new_row_count - 1, column, item)

                btn_widget = QWidget()
                btn_layout = QHBoxLayout(btn_widget)
                btn_layout.setContentsMargins(0, 0, 0, 0)

                add_btn = QPushButton("Thêm thú cưng")
                add_btn.setProperty("row", index)
                add_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #2ecc71; 
                        color: white; 
                        border-radius: 5px;
                        padding: 0 10px;
                        font-weight: bold;
                        margin: 5px;
                        font-size: 12px;
                        height: 25px;
                        line-height: 25px;
                    }
                """)
                add_btn.clicked.connect(partial(self.open_add_pet_dialog, id))

                detail_btn = QPushButton("Chi tết")
                detail_btn.setProperty("row", index)
                detail_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #0a31d1; 
                        color: white; 
                        border-radius: 5px;
                        padding: 0 10px;
                        font-weight: bold;
                        margin: 5px;
                        font-size: 12px;
                        height: 25px;
                        line-height: 25px;
                    }
                """)
                detail_btn.clicked.connect(partial(self.open_customer_detail_dialog, id))
                
                edit_btn = QPushButton("Sửa")
                edit_btn.setProperty("row", index)
                edit_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #337aff; 
                        color: white; 
                        border-radius: 5px;
                        padding: 0 10px;
                        font-weight: bold;
                        margin: 5px;
                        font-size: 12px;
                        height: 25px;
                        line-height: 25px;
                    }
                """)
                edit_btn.clicked.connect(partial(self.open_edit_customer_dialog, id))
                
                delete_btn = QPushButton("Xóa")
                delete_btn.setProperty("row", index)
                delete_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #f44336; 
                        color: white; 
                        border-radius: 5px;
                        padding: 0 10px;
                        font-weight: bold;
                        margin: 5px;
                        font-size: 12px;
                        height: 25px;
                        line-height: 25px;
                    }
                """)
                delete_btn.clicked.connect(lambda: self.delete_row(id, 'customers'))
                
                btn_layout.addWidget(add_btn)
                btn_layout.addWidget(detail_btn)
                btn_layout.addWidget(edit_btn)
                btn_layout.addWidget(delete_btn)
                
                self.customer_table.setCellWidget(index, 3, btn_widget)

    def open_add_customer_dialog(self):
        add_customer_dialog = AddCustomerDialog(self)
        result = add_customer_dialog.exec()

        if result == AddCustomerDialog.accepted:
            pass

    def add_customer(self, add_data):
        query = "INSERT INTO customers (name, phone_number) VALUES (%s, %s)"
        customer = execute_query(query, (add_data['name'], add_data['phone_number']))

        if customer:
            self.show_customer_list()
            self.dialog_success("Thêm khách hàng thành công!")

    def open_customer_detail_dialog(self, customer_id):
        customer_detail_dialog = CustomerDetailDialog(self, customer_id)
        result = customer_detail_dialog.exec()

        if result == AddCustomerDialog.accepted:
            pass

    def open_edit_customer_dialog(self, id):
        query = "SELECT * FROM customers WHERE id = %s"
        customer = execute_query(query, (id), False)

        if customer: 
            add_customer_dialog = EditCustomerDialog(self, customer)
            result = add_customer_dialog.exec()

            if result == EditCustomerDialog.accepted:
                pass

    def update_customer(self, updated_data):
        query = "UPDATE customers SET name = %s, phone_number = %s where id = %s"
        customer = execute_query(query, (updated_data['name'], updated_data['phone_number'], updated_data['id']))
        
        if customer:
            self.show_customer_list()
            self.dialog_success("Cập nhật khách hàng thành công!")

    # End customer

    def add_btn_edit_delete(self, index, id, table):
        btn_widget = QWidget()
        btn_layout = QHBoxLayout(btn_widget)
        btn_layout.setContentsMargins(0, 0, 0, 0)
        
        edit_btn = QPushButton("Sửa")
        edit_btn.setProperty("row", index)
        edit_btn.setStyleSheet("""
            QPushButton {
                background-color: #337aff; 
                color: white; 
                border-radius: 5px;
                padding: 0 10px;
                font-weight: bold;
                margin: 5px;
                font-size: 12px;
                height: 25px;
                line-height: 25px;
            }
        """)
        edit_btn.clicked.connect(partial(self.edit_row, id, table))
        
        delete_btn = QPushButton("Xóa")
        delete_btn.setProperty("row", index)
        delete_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336; 
                color: white; 
                border-radius: 5px;
                padding: 0 10px;
                font-weight: bold;
                margin: 5px;
                font-size: 12px;
                height: 25px;
                line-height: 25px;
            }
        """)
        delete_btn.clicked.connect(lambda: self.delete_row(id, table))
        
        btn_layout.addWidget(edit_btn)
        btn_layout.addWidget(delete_btn)

        return btn_widget
    
    def edit_row(self, id, table):
            if table == "pets":
                self.open_edit_pet_dialog(id, True)
            elif table == "health":
                self.open_edit_health_dialog(id)
            elif table == "feeding":
                self.open_edit_feeding_dialog(id)
            elif table == "exercise":
                self.open_edit_exercise_dialog(id)
            elif table == "expense":
                self.open_edit_expense_dialog(id)
            elif table == "appointment":
                self.open_edit_appointment_dialog(id)
    
    def delete_row(self, id, table):
        button = self.sender()
        row = button.property("row")

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Xác nhận")
        msg_box.setIcon(QMessageBox.Icon.Question) 
        msg_box.setText(f"Bạn có chắc chắn muốn xóa dòng {row + 1}?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        msg_box.setStyleSheet("QPushButton { background-color: none; color: white; }")
        confirm = msg_box.exec() 
        
        if confirm == QMessageBox.StandardButton.Yes:
            query = f"Delete FROM {table} where id = %s"
            execute_query(query, (id))

            if table == "customers":
                self.show_customer_list()
            elif table == "health":
                self.show_health_list()
            elif table == "feeding":
                self.show_feeding_list()
            elif table == "exercise":
                self.show_exercise_list()
            elif table == "expense":
                self.show_expense_list()
            elif table == "appointment":
                self.show_appointment_list()
            elif table == "pets":
                self.show_pet_list()

    def dialog_success(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Thông báo")
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText(message)
        msg_box.setStyleSheet("QPushButton { background-color: none; color: white; }")
        msg_box.exec()


    # update infor
    def open_edit_health_dialog(self, id):
        if id:
            query = "SELECT * FROM health WHERE id = %s"
            health = execute_query(query, (id), False)

            if health: 
                edit_health_dialog = EditHealthDialog(self, health)
                result = edit_health_dialog.exec()

                if result == EditHealthDialog.accepted:
                    pass

    def update_health(self, updated_data):
        if self.pet_id:
            query = "UPDATE health SET vaccine_name = %s, vaccination_date = %s, health_check_date = %s, health_condition = %s WHERE id = %s"
            health = execute_query(query, (updated_data['vaccine_name'], updated_data['vaccination_date'], updated_data['health_check_date'], updated_data['health_condition'], updated_data['id']))

            if health:
                self.show_health_list()
                self.dialog_success("Cập nhật chăm sóc sức khỏe thành công!")

    def open_edit_feeding_dialog(self, id):
        if id:
            query = "SELECT * FROM feeding WHERE id = %s"
            feeding = execute_query(query, (id), False)

            if feeding: 
                edit_feeding_dialog = EditFeedingDialog(self, feeding)
                result = edit_feeding_dialog.exec()

                if result == EditFeedingDialog.accepted:
                    pass

    def update_feeding(self, updated_data):
        if self.pet_id:
            query = "UPDATE feeding SET feeding_date = %s, feeding_time = %s, food_type = %s, quantity = %s WHERE id = %s"
            feeding = execute_query(query, (updated_data['feeding_date'], updated_data['feeding_time'], updated_data['food_type'], updated_data['quantity'], updated_data['id']))

            if feeding:
                self.show_feeding_list()
                self.dialog_success("Cập nhật chế độ ăn uống thành công!")

    def open_edit_exercise_dialog(self, id):
        if id:
            query = "SELECT * FROM exercise WHERE id = %s"
            exercise = execute_query(query, (id), False)

            if exercise: 
                edit_exercise_dialog = EditExerciseDialog(self, exercise)
                result = edit_exercise_dialog.exec()

                if result == EditExerciseDialog.accepted:
                    pass

    def update_exercise(self, updated_data):
        if self.pet_id:
            query = "UPDATE exercise SET exercise_date = %s, exercise_time = %s, activity_type = %s, duration = %s WHERE id = %s"
            feeding = execute_query(query, (updated_data['exercise_date'], updated_data['exercise_time'], updated_data['activity_type'], updated_data['duration'], updated_data['id']))

            if feeding:
                self.show_exercise_list()
                self.dialog_success("Cập nhật hoạt động thành công!")


    def open_edit_expense_dialog(self, id):
        if id:
            query = "SELECT * FROM expense WHERE id = %s"
            expense = execute_query(query, (id), False)

            if expense: 
                edit_expense_dialog = EditExpenseDialog(self, expense)
                result = edit_expense_dialog.exec()

                if result == EditExpenseDialog.accepted:
                    pass

    def update_expense(self, updated_data):
        if self.pet_id:
            query = "UPDATE expense SET expense_type = %s, expense_date = %s, expense_time = %s, amount = %s, description = %s WHERE id = %s"
            expense = execute_query(query, (updated_data['expense_type'], updated_data['expense_date'], updated_data['expense_time'], updated_data['amount'], updated_data['description'], updated_data['id']))

            if expense:
                self.show_expense_list()
                self.dialog_success("Cập nhật chi phí thành công!")

    def open_edit_appointment_dialog(self, id):
        if id:
            query = "SELECT * FROM appointment WHERE id = %s"
            appointment = execute_query(query, (id), False)

            if appointment: 
                edit_appointment_dialog = EditAppointmentDialog(self, appointment)
                result = edit_appointment_dialog.exec()

                if result == EditAppointmentDialog.accepted:
                    pass

    def update_appointment(self, updated_data):
        if self.pet_id:
            query = "UPDATE appointment SET appointment_date = %s, appointment_time = %s, purpose = %s WHERE id = %s"
            appointment = execute_query(query, (updated_data['appointment_date'], updated_data['appointment_time'], updated_data['purpose'], updated_data['id']))

            if appointment:
                self.show_appointment_list()
                self.dialog_success("Cập nhật lịch hẹn thành công!")

    def logout(self):
        from login_window import LoginWindow
        self.log_window = LoginWindow()
        self.log_window.show()
        self.close()
    