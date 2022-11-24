# ini adalah program python sederhana
nama = input("Masukkan nama anda:")
umur = input("Masukkan umur anda :")
kelas = input("Masukka kelas anda")

muhdi = {"name" : nama, "umur" : umur, "kelas" : kelas}

print("=" * 25)

print("\n1. perlihatkan nama user yang baru saja di input \n.2 mencetak umut user yang baru saja di input \n.3 mencetak kelas user yang baru saja di input")


operation = input("Masukkan angka opsi yang ingin anda ingin lakukan selanjutnya :")

if(operation == "1"):
    print("nama user yang di input barusan adalah :",muhdi["name"])
elif(operation == "2"):
    print("umur yang user baru saja masukkan adalah",muhdi["umur"])
elif(operation == "3"):
    print("kelas yang baru saja user masukkan adalah",muhdi["kelas"])
