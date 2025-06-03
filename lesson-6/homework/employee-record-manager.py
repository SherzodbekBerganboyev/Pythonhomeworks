
def main():
    def yangi_xodim():
        a = int(input("Xodim ID sini kiriting: "))
        b = input("Xodim ismini kiriting: ")
        c = input("Xodim ish nomini kiriting: ")
        d = int(input("Xodim maoshini kiriting: "))
        with open("employees.txt", "a") as file:
            file.write(f"{a},{b},{c},{d}\n")


    def barcha_xodim():
        with open("employees.txt", "r") as file:
            txt = file.read()
        print(f"{txt}\n*********************************")


    def id_orqali():
        id = input("ID: ")
        with open("employees.txt", "r") as file:
            lines = file.readlines()
        for line in lines:
            if line.startswith(id + ","):
                print(line.strip())
                break
        else:
            print("ID topilmadi")

    def xodim_malumotlari():
        id = input("Yangilamoqchi bo‘lgan xodim ID sini kiriting: ")
        a1 = input("Yangi Xodim ID sini kiriting: ")
        b1 = input("Yangi Xodim ismini kiriting: ")
        c1 = input("Yangi Xodim ish nomini kiriting: ")
        d1 = input("Yangi Xodim maoshini kiriting: ")

        with open("employees.txt", "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith(id + ","):
                lines[i] = f"{a1},{b1},{c1},{d1}\n"
                break
        else:
            print("ID topilmadi")
            return  # ID topilmasa, funktsiyani yakunlaymiz

        with open("employees.txt", "w") as file:
            file.writelines(lines)

        print("Ma'lumot yangilandi!")

    def xodim_yozuvini():
        id = input("ID: ")
        with open("employees.txt", "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if line.startswith(id + ","):
                    lines.pop(i)
                    break
            else:
                print("ID topilmadi")
                return  # ID topilmasa, funktsiyani yakunlaymiz
            with open("employees.txt", "w") as file:
                file.writelines(lines)



    while True:
        n = int(input("1. Yangi xodim qo‘shish\n2. Barcha xodimlarni ko‘rish\n3. ID orqali xodimni qidirish\n4. Xodim ma’lumotlarini yangilash\n5. Xodim yozuvini o‘chirish\n0. Chiqish\nBuyruqni kiriting: "))
        if n == 1:
            yangi_xodim()
        elif n == 2:
            barcha_xodim()
        elif n == 3:
            id_orqali()
        elif n == 4:
            xodim_malumotlari()
        elif n == 5:
            xodim_yozuvini()
        elif n == 0:
            print('jarayon yakunlandi')
            break
        else:
            print("menuga 1 , 2 , 3 , 4 , 5 , 0 degan buyruqlardan birini bering")
        continue
main()
