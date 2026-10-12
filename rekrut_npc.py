import csv
import os
from models import NPC
from tampil_npc import muat_data

DAFTAR_PERAN = ["Prajurit", "Penyihir", "Tabib"]
MAKS_PASUKAN = 5

def simpan_npc():
    print("\n=== REKRUT NPC BARU ===")
    daftar_npc = muat_data()
    if len(daftar_npc) >= MAKS_PASUKAN:
        print("\n[PERINGATAN] Guild penuh! Maksimal 5 NPC.\n")
        return
    nama = input("Nama                        : ").strip()
    peran = input("Peran (Prajurit/Penyihir/Tabib): ").strip()
    hp = input("HP                          : ").strip()
    atk = input("ATK                         : ").strip()
    if not nama or not peran or not hp or not atk:
        print("\n[PERINGATAN] Semua kolom harus diisi!\n")
        return
    if peran not in DAFTAR_PERAN:
        print("\n[PERINGATAN] Peran tidak dikenal!\n")
        return
    if not hp.isdigit() or not atk.isdigit():
        print("\n[PERINGATAN] HP dan ATK harus berupa angka!\n")
        return
    if int(hp) <= 0 or int(atk) <= 0:
        print("\n[PERINGATAN] HP dan ATK harus lebih dari 0!\n")
        return
    for npc in daftar_npc:
        if npc.nama.lower() == nama.lower():
            print("\n[PERINGATAN] Nama NPC sudah dipakai!\n")
            return
    npc_baru = NPC(nama, peran, int(hp), int(atk))
    file_exists = os.path.exists("npc.csv")
    with open("npc.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Nama", "Peran", "HP", "ATK", "Status"])
        writer.writerow(npc_baru.to_list())
    print("\n[BERHASIL] NPC berhasil direkrut.\n")

def main():
    while True:
        print("=== MENU REKRUT NPC ===")
        print("1. Rekrut NPC")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            simpan_npc()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    main()
