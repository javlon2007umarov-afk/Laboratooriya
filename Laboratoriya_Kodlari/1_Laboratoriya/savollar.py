# savollar.py - savollar moduli: savollar bazasi va ularni ekranga chiqarish

SAVOLLAR = [
    {
        "matn": "Dasturiy ta’minotning alohida, tugallangan qismi nima deb ataladi?",
        "variantlar": ["Operator", "Modul", "O‘zgaruvchi", "Kompilyator"],
        "togri": 2,
    },
    {
        "matn": "Tuzilmaviy dasturlashning asosiy boshqaruv tuzilmalari qaysi qatorda to‘g‘ri berilgan?",
        "variantlar": [
            "Ketma-ketlik, tarmoqlanish, takrorlanish",
            "Sinf, obyekt, merosxo‘rlik",
            "Massiv, ro‘yxat, daraxt",
            "Kirish, chiqish, saqlash",
        ],
        "togri": 1,
    },
    {
        "matn": "Modul ichidagi elementlarning o‘zaro mustahkam bog‘liqligi qanday ataladi?",
        "variantlar": [
            "Modullararo bog‘lanish (coupling)",
            "Modul ichki bog‘lanishi (cohesion)",
            "Rekursiya",
            "Inkapsulyatsiya",
        ],
        "togri": 2,
    },
    {
        "matn": "Modulli dasturlashning afzalligi qaysi?",
        "variantlar": [
            "Dastur hajmi doim kamayadi",
            "Modullarni alohida ishlab chiqish, sinash va qayta ishlatish mumkin",
            "Dasturni testlash shart bo‘lmaydi",
            "Barcha o‘zgaruvchilar global bo‘ladi",
        ],
        "togri": 2,
    },
    {
        "matn": "Yuqori sifatli modulli tuzilmada modullararo bog‘lanish qanday bo‘lishi kerak?",
        "variantlar": ["Iloji boricha kuchsiz", "Iloji boricha kuchli", "Mutlaqo bo‘lmasligi", "Ahamiyati yo‘q"],
        "togri": 1,
    },
]


def savollarni_olish():
    """Savollar ro‘yxatini qaytaradi."""
    return SAVOLLAR


def savolni_korsatish(raqam, jami, savol):
    """Bitta savolni variantlari bilan ekranga chiqaradi."""
    print(f"\nSavol {raqam}/{jami}: {savol['matn']}")
    for i, variant in enumerate(savol["variantlar"], start=1):
        print(f"  {i}) {variant}")


def javobni_kiritish(variantlar_soni):
    """Foydalanuvchidan javob raqamini oladi (to‘g‘ri kiritilguncha so‘raydi)."""
    while True:
        matn = input("Javobingiz (raqam): ").strip()
        if matn.isdigit() and 1 <= int(matn) <= variantlar_soni:
            return int(matn)
        print(f"Iltimos, 1 dan {variantlar_soni} gacha son kiriting.")
