class NPC:
    def __init__(self, nama, peran, hp, atk, status="Siaga"):
        self.nama = nama
        self.peran = peran
        self.hp = hp
        self.atk = atk
        self.status = status

    def to_list(self):
        return [self.nama, self.peran, self.hp, self.atk, self.status]

    def __str__(self):
        return f"{self.nama} [{self.peran}] HP:{self.hp} ATK:{self.atk} - {self.status}"
