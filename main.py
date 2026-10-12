import subprocess

def buka_rekrut_npc():
    subprocess.run(["python", "rekrut_npc.py"])

def buka_tampil_npc():
    subprocess.run(["python", "tampil_npc.py"])

def menu_utama():
    while True:
        print("\n" + "=" * 40)
        print(" GUILD PETUALANG NPC ".center(40, "="))
        print("=" * 40)
        print("1. Rekrut NPC")
        print("2. Lihat & Analisis Pasukan")
        print("0. Keluar")
        print("=" * 40)
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            buka_rekrut_npc()
        elif pilihan == "2":
            buka_tampil_npc()
        elif pilihan == "0":
            print("Sampai jumpa, Petualang.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu_utama()
