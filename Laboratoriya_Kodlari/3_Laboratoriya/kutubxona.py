from dataclasses import dataclass
from bisect import bisect_left, bisect_right


@dataclass
class Kitob:
    id: int
    nom: str
    muallif: str
    yil: int


class Kutubxona:
    def __init__(self, kitoblar):
        self.kitoblar = list(kitoblar)   # asosiy massiv
        self.yil_boyicha = sorted(self.kitoblar, key=lambda k: k.yil)
        self.yillar = [k.yil for k in self.yil_boyicha]
        self.muallif_indeks = {}   # xesh-jadval
        for k in self.kitoblar:
            self.muallif_indeks.setdefault(k.muallif.lower(), []).append(k)

    # 1) Muallif bo'yicha: xesh-jadval, O(1); topilmasa qisman moslik, O(n)
    def muallif_qidir(self, muallif):
        q = muallif.lower().strip()
        if q in self.muallif_indeks:
            return self.muallif_indeks[q]
        return [k for k in self.kitoblar if q in k.muallif.lower()]

    # 2) Nom bo'yicha: chiziqli qidiruv, O(n)
    def nom_qidir(self, nom):
        q = nom.lower().strip()
        return [k for k in self.kitoblar if q in k.nom.lower()]

    # 3) Yil bo'yicha: ikkilik qidiruv, O(log n)
    def yil_qidir(self, yil):
        chap = bisect_left(self.yillar, yil)
        ong = bisect_right(self.yillar, yil)
        return self.yil_boyicha[chap:ong]

    # 4) Birlashtirilgan qidiruv (ixtiyoriy mezonlar)
    def qidir(self, muallif=None, nom=None, yil=None):
        natija = set(k.id for k in self.kitoblar)
        if muallif:
            natija &= {k.id for k in self.muallif_qidir(muallif)}
        if nom:
            natija &= {k.id for k in self.nom_qidir(nom)}
        if yil:
            natija &= {k.id for k in self.yil_qidir(yil)}
        return [k for k in self.kitoblar if k.id in natija]


def chiqar(sarlavha, royxat):
    print(f"--- {sarlavha} ---")
    if not royxat:
        print("Hech narsa topilmadi")
    for k in royxat:
        print(f"{k.id}. {k.nom} | {k.muallif} | {k.yil}")
    print()


if __name__ == "__main__":
    kutubxona = Kutubxona([
        Kitob(1, "O'tkan kunlar", "Abdulla Qodiriy", 1926),
        Kitob(2, "Mehrobdan chayon", "Abdulla Qodiriy", 1929),
        Kitob(3, "Algoritmlar", "Tomas Kormen", 2009),
        Kitob(4, "Dasturiy injiniring", "Yan Sommervill", 2015),
        Kitob(5, "Sof kod", "Robert Martin", 2009),
        Kitob(6, "Navoiy g'azallari", "Alisher Navoiy", 1985),
    ])
    natija = kutubxona.muallif_qidir("Abdulla Qodiriy")
    chiqar("Muallif: Abdulla Qodiriy", natija)
    chiqar("Nom: kod", kutubxona.nom_qidir("kod"))
    chiqar("Yil: 2009", kutubxona.yil_qidir(2009))
    chiqar("Birlashtirilgan: yil=2009, muallif=Martin",
           kutubxona.qidir(muallif="Martin", yil=2009))
    chiqar("Yil: 1900", kutubxona.yil_qidir(1900))
