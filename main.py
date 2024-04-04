import os

names = []
infos = {}

running = True


while running:
    os.system("clear")

    print("""
1. Them thanh vien
2. Xoa thanh vien
3. Xem danh sach
4. Them thong tin nguoi dung
5. Xem thong tin nguoi dung
6. Tat chuong trinh
    """)

    mode = input("Chon che do: ")

    if mode == "1":
        name = input("Nhap ten thanh vien 9a1: ")
        names.append(name)

    
    if mode == "2":
        name = input("Nhap ten thanh vien 9a1: ")

        if name not in names:
            print("Deo co dau ma xoa!")
        else:
            names.remove(name)
    if mode == "3":
        print("Danh sach lop: ")

        if len(names) == 0:
            print("Trong lop chua co ai ca!")
        else:
            index = 0
            
            for element in names:
                index += 1
                print(f"{index}. {element}")

    if mode == "4":
        name = input("Nhap ten thanh vien 9a1: ")
        if name not in names:
            print("Thanh vien chua duoc them vao")
        else:
            thongtin = input(f"Nhap thong tin cua {name}:")
            infos[name] = thongtin

    if mode == "5":
        name = input("Nhap ten thanh vien 9a1: ")
        if name not in infos.keys():
            print("Thanh vien chua duoc them vao")
        else:   
            print(f"Thong tin cua {name}: ")
            print(infos[name])

    if mode == "6":    
        running = False

    print("-------------------")

    input("Nhan nut bat ki de tiep tuc: ")
        

print("Xong chuong trinh",'thang hoang ia dun')