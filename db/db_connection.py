import pymysql
import pymysql.cursors
from config import DB_CONFIG
from pymysql.cursors import DictCursor

def get_db_connection():
    """
    Hàm này dùng để tạo kết nối đến cơ sở dữ liệu MySQL
    """
    try:
        connection = pymysql.connect(**DB_CONFIG, cursorclass=DictCursor)
        return connection
    except pymysql.MySQLError as e:
        print(f"Lỗi kết nối cơ sở dữ liệu: {e}")
        return None


def execute_query(query, params=None, getAll=True):
    """
    Hàm này dùng để thực thi các truy vấn SQL như SELECT, INSERT, UPDATE, DELETE.
    
    :param query: Truy vấn SQL cần thực thi
    :param params: Các tham số cho truy vấn (nếu có)
    :return: Dữ liệu trả về nếu có, hoặc None nếu là truy vấn không trả về dữ liệu
    """
    connection = None
    try:
        connection = get_db_connection()
        if connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                # Nếu là truy vấn SELECT, trả về kết quả
                if query.strip().lower().startswith('select'):
                    if getAll:
                        result = cursor.fetchall()
                    else:
                        result = cursor.fetchone()
                    return result
                else:
                    # Nếu là các truy vấn INSERT, UPDATE, DELETE, commit thay đổi
                    connection.commit()

                    if query.strip().lower().startswith('insert'):
                        cursor.execute("SELECT LAST_INSERT_ID()")
                        return cursor.fetchone()['LAST_INSERT_ID()']
                    else:
                        return cursor.rowcount
    except pymysql.MySQLError as e:
        print(f"Lỗi thực thi truy vấn: {e}")
        return None
    finally:
        if connection:
            connection.close()