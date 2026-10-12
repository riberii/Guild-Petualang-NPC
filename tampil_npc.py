import csv
import os
from models import NPC

def muat_data():
    daftar_npc = []
    if not os.path.exists("npc.csv"):
        print("File npc.csv tidak ditemukan.")
        return daftar_npc
    with open("npc.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # Lewati header
        for row in reader:
            npc = NPC(
                nama=row[0],
                peran=row[1],
                hp=int(row[2]),
                atk=int(row[3]),
                status=row[4]
            )
            daftar_npc.append(npc)
    return daftar_npc

def tampilkan_pasukan():
    daftar_npc = muat_data()
    if not daftar_npc:
        print("Belum ada NPC di guild.")
        return
    print("\n=== DAFTAR PASUKAN GUILD ===\n")
    print(f"{'Nama':15}{'Peran':12}{'HP':8}{'ATK':8}{'Status'}")
    print("-" * 52)
    for npc in daftar_npc:
        print(
            f"{npc.nama:15}"
            f"{npc.peran:12}"
            f"{npc.hp:<8}"
            f"{npc.atk:<8}"
            f"{npc.status}"
        )
    print("-" * 52)
    print(f"Total NPC: {len(daftar_npc)}")

def analisis_pasukan():
    daftar_npc = muat_data()
    if not daftar_npc:
        print("Tidak ada data untuk dianalisis.")
        return
    total_hp = 0
    total_atk = 0
    jumlah_prajurit = 0
    jumlah_penyihir = 0
    jumlah_tabib = 0
    terkuat = daftar_npc[0]
    for npc in daftar_npc:
        total_hp += npc.hp
        total_atk += npc.atk
        if npc.peran == "Prajurit":
            jumlah_prajurit += 1
        elif npc.peran == "Penyihir":
            jumlah_penyihir += 1
        elif npc.peran == "Tabib":
            jumlah_tabib += 1
        if npc.atk > terkuat.atk:
            terkuat = npc
    rata_hp = total_hp / len(daftar_npc)
    print("\n=== ANALISIS PASUKAN ===")
    print(f"Total HP        : {total_hp}")
    print(f"Total ATK       : {total_atk}")
    print(f"Rata-rata HP    : {rata_hp:.1f}")
    print(f"Prajurit        : {jumlah_prajurit}")
    print(f"Penyihir        : {jumlah_penyihir}")
    print(f"Tabib           : {jumlah_tabib}")
    print(f"NPC Terkuat     : {terkuat.nama} (ATK {terkuat.atk})")

def main():
    while True:
        print("\n=== MENU PASUKAN ===")
        print("1. Tampilkan Pasukan")
        print("2. Analisis Pasukan")
        print("0. Keluar")
        pilihan = input("Pilih: ")
        if pilihan == "1":
            tampilkan_pasukan()
        elif pilihan == "2":
            analisis_pasukan()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
