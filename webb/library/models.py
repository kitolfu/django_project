from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(
        max_length=20,
        help_text='введите название жанра',
        verbose_name='жанр',
        unique=True,
    )

class Book(models.Model):
    """Типичный класс модели, производный от класса Model."""

    # Поля
    price = models.IntegerField(
        verbose_name='цена',
        help_text='введите цену',
    )
    genre = models.ForeignKey(
        Genre,
        help_text='выберите жанр',
        related_name='books',
        verbose_name='жанр',
        on_delete=models.PROTECT,
    )
    my_field_name = models.CharField(max_length=20, help_text='Введите описание поля')
    # … 

    # Метаданные
    class Meta:
        # ordering = ['-my_field_name']
        verbose_name = "BetterName"



