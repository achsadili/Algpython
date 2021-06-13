'''
program cek kelulusan 
created by ACH.SADILI 
           (20083000030)
           kelas 2A
           dibuat pada tgl 13/06/2021
'''
import os
clear = lambda : os.system('cls')
jwb = "y"
while jwb == "Y" or jwb == "y" :
    clear()
    print("PROGRAM CEK KELULUSAN")
    print("---------------------")
    print()
    a = input("Masukkan Nilai = ")
    n = int(a)
    if n < 0 or n > 100 :
        sts = "Inputan hanya boleh 0 sampai 100 saja"
    elif n > 60 :
        sts = "LULUS"
    else :
        sts = "TIDAK LULUS"
    print()
    print(sts)
    print()
    jwb = input("Cek lagi? (y/t) : ")
    if jwb == "t" or jwb == "T":
        break
