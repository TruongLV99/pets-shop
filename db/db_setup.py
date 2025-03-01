import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pymysql import MySQLError
from db.db_connection import get_db_connection

# Hàm đọc file SQL và thực thi các câu lệnh
def execute_sql_from_file(file_path):
    try:
        # Kết nối đến MySQL sử dụng PyMySQL
        connection = get_db_connection()
        if connection is None:
            return

        # Đọc câu lệnh SQL từ file
        sql_file_path = os.path.join(os.getcwd(), file_path)
        with open(sql_file_path, 'r') as sql_file:
            sql_query = sql_file.read()

        # Thực thi câu lệnh SQL từ tệp
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            connection.commit()  # Lưu thay đổi vào cơ sở dữ liệu

        print("Các bảng đã được tạo thành công từ file SQL!")

        # Đóng kết nối
        connection.close()
    except MySQLError as e:
        connection.close()
        print(f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    # Đường dẫn đến file chứa câu lệnh SQL
    file_path = "db/migrations.sql"
    execute_sql_from_file(file_path)