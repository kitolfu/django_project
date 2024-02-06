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
    name = models.CharField(max_length=20,
        verbose_name='Имя',                     
        help_text='Введите имя автора')
    
    
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(
        verbose_name = 'Название',
        max_length=25,
        help_text='Введите имя автора'
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
        help_text='Введите название жанра'
    )
    author  = models.ForeignKey(
        Author,
        help_text='Выберите автора',
        verbose_name='Автор',
        on_delete=models.PROTECT,
        related_name='books'
    )
    creation_date = models.DateField(
        verbose_name='Дата',
        help_text='Введите дату создания'
    )  
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        help_text='Введие описание книги'
    )
    pages_number = models.IntegerField(
        verbose_name='Страницы',
        help_text='Введите количество страниц'
    )

    
    # Метаданные
    class Meta:
        verbose_name = "Book"
        ordering = ['name', 'author', 'creation_date']



