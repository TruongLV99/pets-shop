import locale
import bcrypt

# Cấu hình locale cho tiền tệ VNĐ
try:
    locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')
except locale.Error:
    pass  # Nếu hệ thống không hỗ trợ locale VN, sẽ dùng cách thủ công

# Hàm định dạng tiền VNĐ (bỏ số thập phân)
def format_vnd(amount):
    amount = round(amount)  # Làm tròn số tiền về số nguyên
    try:
        return locale.currency(amount, grouping=True, symbol="₫", international=False).split(",")[0] + "₫"
    except:
        return "{:,.0f}₫".format(amount).replace(",", ".")

# Hàm hash mật khẩu bằng bcrypt
def hash_password(password):
    salt = bcrypt.gensalt()  # Tạo salt ngẫu nhiên
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)  # Mã hóa mật khẩu
    return hashed.decode('utf-8')  # Chuyển từ byte về string để lưu vào DB