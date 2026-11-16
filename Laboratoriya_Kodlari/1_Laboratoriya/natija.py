# natija.py - natijalarni hisoblash moduli

def ball_hisoblash(tekshiruv_natijalari):
    """To‘g‘ri javoblar sonini hisoblaydi."""
    return sum(1 for x in tekshiruv_natijalari if x)


def foiz_hisoblash(ball, jami):
    """To‘g‘ri javoblar foizini hisoblaydi."""
    if jami == 0:
        return 0.0
    return ball * 100 / jami


def baho_aniqlash(foiz):
    """Foiz bo‘yicha 5 ballik tizimda bahoni aniqlaydi."""
    if foiz >= 86:
        return "5 (a’lo)"
    if foiz >= 71:
        return "4 (yaxshi)"
    if foiz >= 55:
        return "3 (qoniqarli)"
    return "2 (qoniqarsiz)"


def natijani_chiqarish(ball, jami):
    """Yakuniy natijani ekranga chiqaradi."""
    foiz = foiz_hisoblash(ball, jami)
    print("\n===== NATIJA =====")
    print(f"To‘g‘ri javoblar: {ball} / {jami}")
    print(f"Foiz: {foiz:.1f}%")
    print(f"Baho: {baho_aniqlash(foiz)}")
