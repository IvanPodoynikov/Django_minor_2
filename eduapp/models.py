from django.db import models

class Entry(models.Model):
    PROGRAM_CHOICES = [
        ('math', 'Математика'),
        ('sovbak', 'СовБак'),
    ]

    last_name = models.CharField(
        "Фамилия",
        max_length=100,
        default="",
        blank=True,
    )
    first_name = models.CharField(
        "Имя",
        max_length=100,
        default="",
        blank=True,
    )
    program = models.CharField(
        "Программа",
        max_length=10,
        choices=PROGRAM_CHOICES,
    )
    email = models.EmailField(
        "E-mail",
        default="",
        blank=True,
    )
    phone = models.CharField(
        "Телефон",
        max_length=20,
        default="",
        blank=True,
    )
    score = models.IntegerField(
        "Средний балл"
    )
    date = models.DateField(
        "Дата записи",
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} – {self.get_program_display()}"
