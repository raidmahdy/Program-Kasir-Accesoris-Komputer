#Tugas Individu UTS Dasprog
#Nama: Raid Mahdy
#NIM: 3.34.20.4.17
#Kelas: IK1E

print("~~~~Program Kasir Toko Accessoris Komputer~~~~")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

total1=0
jenis1=""
banyak1=0


def ssd():
   global total1
   global banyak1
   global jenis1
   print ("\n~~~~Daftar SSD~~~~")
   print(" [1]. SSD 512GB - Rp1.000.000")
   print(" [2]. SSD 256GB - Rp500.000")
   print(" [3]. SSD 128GB - Rp300.000")
   print(" [0]. jika tidak")
   nomor=int(input("Masukan Pilihan: "))
   print("Jika tidak ketikan 0")
   banyak1= int(input("Banyak: "))
   
   if nomor==1:
       total1=banyak1*1000000
       print (banyak1," buah SSD 512GB = Rp = Rp", total1)
       jenis1=("SSD 512GB")
   elif nomor==2:
       total1=banyak1*500000
       print (banyak1," buah SSD 256GB = Rp", total1)
       jenis1=("SSD 256GB")
   elif nomor==3:
       total1=banyak1*300000
       print (banyak1, "buah SSD 128GB", total1)
       jenis1=("SSD 128GB")
   else:
      print("Pilihan tidak tersedia")
      

ssd()

total2=0
jenis2=""
porsi2=0


def ram():
   global total2
   global banyak2
   global jenis2
   print ("\n~~~~Daftar RAM~~~~")
   print(" [1]. RAM 16GB - Rp1.200.000")
   print(" [2]. RAM 8GB  - Rp800.000")
   print(" [3]. RAM 4GB  - Rp400.000")
   print(" [0]. jika tidak")
   nomor=int(input("Masukan Pilihan: "))
   print("Jika tidak ketikan 0")
   banyak2= int(input("Banyak: "))
   
   if nomor==1:
       total2=banyak2*1200000
       print (banyak2," buah RAM 16GB = Rp = Rp", total2)
       jenis2=("RAM 16GB")
   elif nomor==2:
       total2=banyak2*800000
       print (banyak2," buah RAM 8GB = Rp", total2)
       jenis2=("RAM 8GB")
   elif nomor==3:
       total2=banyak2*400000
       print (banyak2, "buah RAM 4GB", total2)
       jenis2=("RAM 4GB")
   else:
      print("Pilihan tidak tersedia")
      

ram()

total3=0
jenis3=""
banyak3=0


def hdd():
   global total3
   global banyak3
   global jenis3
   print ("\n~~~~Daftar HDD~~~~")
   print(" [1]. HDD 1TB - Rp700.000")
   print(" [2]. HDD 2TB - Rp1.200.000")
   print(" [3]. HDD 4TB - Rp1.800.000")
   print(" [0]. jika tidak")
   nomor=int(input("Masukan Pilihan: "))
   print("Jika tidak ketikan 0")
   banyak3= int(input("Banyak: "))
   
   if nomor==1:
       total3=banyak3*700000
       print (banyak3," buah HDD 1TB = Rp = Rp", total3)
       jenis3=("HDD 1TB")
   elif nomor==2:
       total3=banyak3*1200000
       print (banyak3," buah HDD 2TB = Rp", total3)
       jenis1=("HDD 2TB")
   elif nomor==3:
       total3=banyak3*1800000
       print (banyak3, "buah HDD 4TB", total3)
       jenis3=("HDD 4TB")
   else:
      print("Pilihan tidak tersedia")
      

hdd()


    
totalsemua=0
totalsemua=total1+total2+total3
print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp."))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n    ===========================")
print("===== S T R U K   B E L I =====")
print("    ===========================")
print (" Nama         :",pembeli)
print (" Beli         :",banyak1,jenis1,"-", total1)
print ("               ",banyak2,jenis2,"-", total2)
print ("               ",banyak3,jenis3,"-", total3)
print (" Tagihan      : Rp.",totalsemua)
print (" Uang         : Rp.",uang)
print (" Kembalian    : Rp.",kembalian)
print("  ===========================")
print("==========TERIMAKASIH==========")
