class RisovkaIProverka:
    def pokazat_pole(self, pole):
        print()
        print(self._znachenie_kletki(pole, 0), "|", self._znachenie_kletki(pole, 1), "|", self._znachenie_kletki(pole, 2))
        print("--+---+--")
        print(self._znachenie_kletki(pole, 3), "|", self._znachenie_kletki(pole, 4), "|", self._znachenie_kletki(pole, 5))
        print("--+---+--")
        print(self._znachenie_kletki(pole, 6), "|", self._znachenie_kletki(pole, 7), "|", self._znachenie_kletki(pole, 8))
        print()

    def _znachenie_kletki(self, pole, index):
        if pole[index] == " ":
            return str(index + 1)
        return pole[index]

    def est_pobeda(self, pole):
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
            if pole[a] == pole[b] == pole[c] and pole[a] != " ":
                return True
        return False

    def nichya(self, pole):
        for kletka in pole:
            if kletka == " ":
                return False
        return True