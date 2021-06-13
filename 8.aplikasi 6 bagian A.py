'''
cek total harga printer
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
    print("PROGRAM HITUNG TOTAL HARGA PRINTER EPSON T20")
    print("--------------------------------------------")
    
    hrgPrinter = 660000
    a = input("Masukkan Jumlah Printer = ")
    jmlhPrinter = int(a)
    

    totHrg = hrgPrinter * jmlhPrinter
    print()
    print ("Total Harga = Rp.",format(totHrg,",.2f"))

    
    print()
    jwb = input("Cek Lagi? (y/t) = ")
    if jwb == "t" or jwb == "T" :
        break
