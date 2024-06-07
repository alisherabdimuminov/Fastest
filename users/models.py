from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


BRANCH = (
    ("andijon", "Andijon viloyati filiali"),
    ("buxoro", "Buxoro viloyati filiali"),
    ("fargona", "Farg'ona viloyati filiali"),
    ("jizzax", "Jizzax viloyati filiali"),
    ("namangan", "Namangan viloyati filiali"),
    ("navoiy", "Navoiy viloyati filiali"),
    ("qashqadaryo", "Qashqadaryo viloyati filiali"),
    ("qoraqalpogiston", "Qoraqalpog'iston Respublikasi filiali"),
    ("samarqand", "Samarqand viloyati filiali"),
    ("sirdaryo", "Sirdaryo viloyati filiali"),
    ("surxondaryo", "Surxandaryo viloyati filiali"),
    ("toshkent_shahar", "Toshkent shahar filiali"),
    ("toshkent", "Toshkent viloyati filiali"),
    ("xorazm", "Xorazm viloyati filiali")
)


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name="Foydalanuvchi nomi")
    first_name = models.CharField(max_length=100, verbose_name="Ism")
    last_name = models.CharField(max_length=100, verbose_name="Familiya")
    middle_name = models.CharField(max_length=100, verbose_name="Otasini ismi")
    branch = models.CharField(max_length=100, verbose_name="Filial", choices=BRANCH)

    USERNAME_FIELD = "username"
    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"