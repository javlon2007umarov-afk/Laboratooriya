from dataclasses import dataclass


@dataclass
class Student:
    student_id: int
    full_name: str
    birth_date: str
    address: str
    phone: str
    group: str
    gpa: float
    contract_paid: bool


# Stamp coupling: butun Student uzatilgan, faqat gpa kerak
def calculate_scholarship_old(student: Student) -> float:
    if student.gpa >= 4.5:
        return 1_200_000
    elif student.gpa >= 4.0:
        return 900_000
    elif student.gpa >= 3.5:
        return 600_000
    return 0


# Stamp coupling: butun Student uzatilgan, faqat full_name kerak
def make_greeting_old(student: Student) -> str:
    return f"Salom, {student.full_name}!"


# Data coupling: faqat zarur maydonlar uzatilgan
def calculate_scholarship(gpa: float) -> float:
    if gpa >= 4.5:
        return 1_200_000
    elif gpa >= 4.0:
        return 900_000
    elif gpa >= 3.5:
        return 600_000
    return 0


def make_greeting(full_name: str) -> str:
    return f"Salom, {full_name}!"


if __name__ == "__main__":
    s = Student(1, "Karimov Aziz", "2004-05-12", "Toshkent",
                "+998901234567", "AT-21", 4.3, True)
    print(calculate_scholarship_old(s), make_greeting_old(s))
    print(calculate_scholarship(s.gpa), make_greeting(s.full_name))
