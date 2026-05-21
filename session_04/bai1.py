total_money = int(input("Nhập tổng tiền hóa đơn ban đầu: "))
if total_money >= 500000:
    discount = total_money * 0.10
else:
    discount = 0
total_money_payment = total_money - discount
print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")
print(f"Số tiền được giảm giá: {int(discount)} VND")
print(f"Tổng tiền khách phải trả: {int(total_money_payment)} VND")