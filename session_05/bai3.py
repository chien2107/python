room_count = int(input("Nhập số lượng phòng học: "))
if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")
else:
    for room in range(1, room_count + 1):
        print(f"\nPhòng học {room}")
        rows = int(input("Nhập số hàng ghế: "))
        seats = int(input("Nhập số ghế mỗi hàng: "))
        if rows <= 0 or seats <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue
        if rows > 10 or seats > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break
        print("Sơ đồ chỗ ngồi:")
        for i in range(rows):
            for j in range(seats):
                print("*", end=" ")
            print()