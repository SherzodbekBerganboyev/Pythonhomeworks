text=input("biror gapni kiriting:")
tekshir=any(i.isdigit() for i in text)
if tekshir:
    print("gapda raqam ishlatilgan")
else:
    print("gapda raqam ishlatilmagan")

