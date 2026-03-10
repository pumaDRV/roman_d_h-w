class KrestikiNoliki:
    def __init__(self):
        self.pole = [" "] * 9
        self.tekushii_igrok = "X"

    def pokazat_pole(self):
        print()
        print(self._znachenie_kletki(0), "|", self._znachenie_kletki(1), "|", self._znachenie_kletki(2))
        print("--+---+--")
        print(self._znachenie_kletki(3), "|", self._znachenie_kletki(4), "|", self._znachenie_kletki(5))
        print("--+---+--")
        print(self._znachenie_kletki(6), "|", self._znachenie_kletki(7), "|", self._znachenie_kletki(8))
        print()

    def _znachenie_kletki(self, index):
        if self.pole[index] == " ":
            return str(index + 1)
        return self.pole[index]

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

    def est_pobeda(self):
        kombinacii = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

        for a, b, c in kombinacii:
            if self.pole[a] == self.pole[b] == self.pole[c] and self.pole[a] != " ":
                return True
        return False

    def nichya(self):
        for kletka in self.pole:
            if kletka == " ":
                return False
        return True

    def pomenyat_igroka(self):
        if self.tekushii_igrok == "X":
            self.tekushii_igrok = "O"
        else:
            self.tekushii_igrok = "X"

    def igrat(self):
        print("Крестики-нолики для двух игроков.")
        print("Вводи номер клетки от 1 до 9.")

        while True:
            self.pokazat_pole()
            self.sdelat_hod()

            if self.est_pobeda():
                self.pokazat_pole()
                print(f"Игрок {self.tekushii_igrok} победил!")
                break

            if self.nichya():
                self.pokazat_pole()
                print("Ничья!")
                break

            self.pomenyat_igroka()


def zapusk_igry():
    igra = KrestikiNoliki()
    igra.igrat()


zapusk_igry()