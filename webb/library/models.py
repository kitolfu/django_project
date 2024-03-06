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

    class Meta:

        verbose_name = "Жанр"
        verbose_name_plural = 'Жанры'

class Author(models.Model):
    name = models.CharField(max_length=20,
        verbose_name='Имя',                     
        help_text='Введите имя автора')
    
    
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = 'Авторы'

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

    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = 'Книги'
        ordering = ['name', 'author', 'creation_date']



