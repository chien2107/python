import random
name = input("Nhập họ và tên bệnh nhân: ")
patient_id = f"BN{random.randint(1000, 9999)}"
room = input("Nhập khoa/phòng khám chỉ định: ")
print(f"Bệnh nhân: {name} - Mã BA: {patient_id} - Chuyển tới: {room}")