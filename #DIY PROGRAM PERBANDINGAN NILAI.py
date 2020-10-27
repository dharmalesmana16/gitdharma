import pyautogui as pya

global n
program_name ="Dharma Lesmana"

print(program_name.center(50, "="))
def program ():
    angka1 = int(input("Masukkan angka pertama = "))
    angka2 = int(input("Masukkan angka kedua = "))
    print("="*50)
    if angka1>angka2:
        print(angka1, "Lebih besar dari  ", angka2)
    elif angka1<angka2:
        print(angka1, "Lebih kecil dari ", angka2)
    elif angka1==angka2:
        print(angka1, "Sama besar dengan ", angka2)



def pilihan():
    global n
    n=print("Program sudah selesai dijalankan, apakah mau mengulang lagi ? (y/n)")

    n=input()


program()
pilihan()

while n=='y':
    program()
    pilihan()
if n=='n':
    pya.typewrite("Terimakasih telah menggunakan program ini\nsemoga kita selalu sehat", interval=0.05)