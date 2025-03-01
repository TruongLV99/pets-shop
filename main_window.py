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
from utils.helpers import format_vnd
from datetime import datetime

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pages = self.stackedWidget
        self.pages.setCurrentIndex(1)
        self.pet_id = 0

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
        self.customer_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.pet_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.total_expense_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        self.btn_search.clicked.connect(self.search_pet)
        self.btn_search_pet.clicked.connect(self.show_pet_list)
        self.btn_search_customer.clicked.connect(self.show_customer_list)
        self.btn_filter_expense.clicked.connect(lambda: self.show_total_expense(2))
        self.btn_get_all_expense.clicked.connect(lambda: self.show_total_expense(1))
        self.btn_add_customer.clicked.connect(self.open_add_customer_dialog)

        self.btn_edit.clicked.connect(self.open_edit_pet_dialog)
        self.btn_cham_soc_suc_khoe.clicked.connect(self.open_add_health_dialog)
        self.btn_che_do_an_uong.clicked.connect(self.open_add_feeding_dialog)
        self.btn_hoat_dong.clicked.connect(self.open_add_exercise_dialog)
        
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

            self.expense_table.setRowCount(0)
            query = "SELECT * FROM expense WHERE pet_id = %s"
            expense = execute_query(query, (pet['id']))

            if expense:
                for index, item in enumerate(expense):
                    data = [index + 1, item['expense_type'], item['expense_date'].strftime("%d/%m/%Y") if item['expense_date'] else item['created_at'].strftime("%d/%m/%Y"), format_vnd(item['amount']), item['description']]
                    self.show_expense_list(data=data)

            query = "SELECT * FROM appointment WHERE pet_id = %s"
            appointment = execute_query(query, (pet['id']))

            self.appointment_table.setRowCount(0)
            if appointment:
                for index, item in enumerate(appointment):
                    data = [index + 1, item['appointment_date'].strftime("%d/%m/%Y") if item['appointment_date'] else '', (datetime.min + item['appointment_time']).time().strftime("%H:%M"), item['purpose']]
                    self.show_appointment_list(data=data)

            # query = "SELECT * FROM feeding WHERE pet_id = %s"
            # feeding = execute_query(query, (pet[0]))

            # query = "SELECT * FROM exercise WHERE pet_id = %s"
            # exercise = execute_query(query, (pet[0]))

            # query = "SELECT * FROM expense WHERE pet_id = %s"
            # expense = execute_query(query, (pet[0]))

            # query = "SELECT * FROM appointment WHERE pet_id = %s"
            # appointment = execute_query(query, (pet[0]))
        else: 
            QMessageBox.warning(self, "Search Failed", "Không tìm thấy thú cưng.")

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

                btn_widget = self.add_tn_edit_delete(index, id, 'health')
                
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

                btn_widget = self.add_tn_edit_delete(index, id, 'feeding')
                
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

                btn_widget = self.add_tn_edit_delete(index, id, 'exercise')
                
                self.exercise_table.setCellWidget(index, 4, btn_widget)

    def show_expense_list(self, data):
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

    def show_appointment_list(self, data):
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

    def open_edit_pet_dialog(self):
        if self.pet_id:
            query = "SELECT * FROM pets WHERE id = %s"
            pet = execute_query(query, (self.pet_id), False)

            if pet: 
                edit_pet_dialog = EditPetDialog(self, pet)
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
                # QMessageBox.information(self, "Thành công", "Cập nhật thú cưng thành công!")

    def update_pet(self, updated_data):
        if self.pet_id:
            query = "UPDATE pets SET name = %s, breed = %s, birth_date = %s, color = %s, weight = %s, height = %s, length = %s, special_features = %s WHERE id = %s"
            pet = execute_query(query, (updated_data['name'], updated_data['breed'], updated_data['birth_date'], updated_data['color'], updated_data['weight'], updated_data['height'], updated_data['length'], updated_data['special_features'], updated_data['id']))
            
            if pet:
                self.search_pet(updated_data['id'])
                # QMessageBox.information(self, "Thành công", "Cập nhật thú cưng thành công!")

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

    # Customer page
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
                add_btn.clicked.connect(lambda: self.open_add_pet_dialog(id))
                
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
                # edit_btn.clicked.connect(self.edit_row)
                
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

    def add_tn_edit_delete(self, index, id, table):
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
        # edit_btn.clicked.connect(self.edit_row)
        
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
    
    def delete_row(self, id, table):
        button = self.sender()
        row = button.property("row")
        
        confirm = QMessageBox.question(
            self, 
            "Xác nhận xóa", 
            f"Bạn có chắc chắn muốn xóa dòng {row + 1}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
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
    