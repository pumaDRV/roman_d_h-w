from risovka import RisovkaIProverka

class KrestikiNoliki:
    def __init__(self):
        self.pole = [" "] * 9
        self.tekushii_igrok = "X"
        self.risovka = RisovkaIProverka()

    def sdelat_hod(self):
        while True:
            hod = input(f"Игрок {self.tekushii_igrok}, выбери клетку (1-9): ")

            if not hod.isdigit():
                print("Ошибка: введи число от 1 до 9.")
                continue

            index = int(hod) - 1

            if index < 0 or index > 8:
                print("Ошибка: номер клетки должен быть от 1 до 9.")
                continue

            if self.pole[index] != " ":
                print("Ошибка: эта клетка уже занята.")
                continue

            self.pole[index] = self.tekushii_igrok
            break

    def pomenyat_igroka(self):
        if self.tekushii_igrok == "X":
            self.tekushii_igrok = "O"
        else:
            self.tekushii_igrok = "X"

    def igrat(self):
        print("Крестики-нолики для двух игроков.")
        print("Вводи номер клетки от 1 до 9.")

        while True:
            self.risovka.pokazat_pole(self.pole)
            self.sdelat_hod()

            if self.risovka.est_pobeda(self.pole):
                self.risovka.pokazat_pole(self.pole)
                print(f"Игрок {self.tekushii_igrok} победил!")
                break

            if self.risovka.nichya(self.pole):
                self.risovka.pokazat_pole(self.pole)
                print("Ничья!")
                break

            self.pomenyat_igroka()


def zapusk_igry():
    igra = KrestikiNoliki()
    igra.igrat()


zapusk_igry()