# tekshirish.py - javoblarni tekshirish moduli

def javobni_tekshirish(savol, javob):
    """Foydalanuvchi javobi to‘g‘ri bo‘lsa True, aks holda False qaytaradi."""
    return javob == savol["togri"]


def fikr_bildirish(savol, togri_mi):
    """Javobga qarab izoh matnini qaytaradi."""
    if togri_mi:
        return "To‘g‘ri!"
    togri_matn = savol["variantlar"][savol["togri"] - 1]
    return f"Noto‘g‘ri. To‘g‘ri javob: {savol['togri']}) {togri_matn}"
