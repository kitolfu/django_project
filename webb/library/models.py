from django.db import models
from django.urls import reverse

class Genre(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(
        max_length=20,
        help_text='Введите название жанра',
        verbose_name='Жанр',
        unique=True,
    )

class Author(models.Model):
    name = models.CharField(max_length=20, help_text='Введите имя автора')
    def __str__(self):
        return self.name

class Book(models.Model):
    """Типичный класс модели, производный от класса Model."""

    # Поля
    name = models.CharField(
        verbose_name = 'Название',
        max_length=25
    )
    price = models.IntegerField(
        verbose_name='"Цена',
        help_text='Введите цену',
    )
    genre = models.ForeignKey(
        Genre,
        help_text='Выберите жанр',
        related_name='books',
        verbose_name='Жанр',
        on_delete=models.PROTECT,
    )
    author  = models.ForeignKey(
        Author,
        help_text='Выберите автора',
        verbose_name='Автор',
        on_delete=models.PROTECT,
    )
    creation_date = models.DateField(
        verbose_name='Дата',
    )  
    description = models.TextField(
        verbose_name='Описание',
        null=True,
    )
    pages_number = models.IntegerField(
        verbose_name='Страницы',
    )



    my_field_name = models.CharField(max_length=20, help_text='Введите описание поля')
    # … 

    # Метаданные
    class Meta:
        # ordering = ['-my_field_name']
        verbose_name = "Book"



