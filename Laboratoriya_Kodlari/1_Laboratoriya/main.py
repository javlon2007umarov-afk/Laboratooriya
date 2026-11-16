# main.py - asosiy dastur: modullarni bog‘lab, testni boshqaradi

import savollar
import tekshirish
import natija


def test_otkazish():
    royxat = savollar.savollarni_olish()
    jami = len(royxat)
    tekshiruv_natijalari = []

    for raqam, savol in enumerate(royxat, start=1):
        savollar.savolni_korsatish(raqam, jami, savol)
        javob = savollar.javobni_kiritish(len(savol["variantlar"]))
        togri_mi = tekshirish.javobni_tekshirish(savol, javob)
        print(tekshirish.fikr_bildirish(savol, togri_mi))
        tekshiruv_natijalari.append(togri_mi)

    ball = natija.ball_hisoblash(tekshiruv_natijalari)
    natija.natijani_chiqarish(ball, jami)


if __name__ == "__main__":
    print("TEST DASTURI")
    test_otkazish()
