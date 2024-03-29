# Generated by Django 2.2.19 on 2024-03-11 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите имя автора', max_length=20, verbose_name='Имя')),
                ('born_date', models.DateField(help_text='Введите дату', verbose_name='Дата рожения')),
                ('book_type', models.CharField(help_text='введите тип произведений автора', max_length=20, verbose_name='Тип произведений')),
                ('additional_information', models.TextField(blank=True, help_text='введите дополнительную информацию об авторе', verbose_name='дополнительная информация')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название жанра', max_length=20, unique=True, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите имя автора', max_length=25, verbose_name='Название')),
                ('price', models.IntegerField(help_text='Введите цену', verbose_name='"Цена')),
                ('creation_date', models.DateField(help_text='Введите дату создания', verbose_name='Дата')),
                ('description', models.TextField(help_text='Введие описание книги', null=True, verbose_name='Описание')),
                ('pages_number', models.IntegerField(help_text='Введите количество страниц', verbose_name='Страницы')),
                ('author', models.ForeignKey(help_text='Выберите автора', on_delete=django.db.models.deletion.PROTECT, related_name='books', to='library.Author', verbose_name='Автор')),
                ('genre', models.ForeignKey(help_text='Введите название жанра', on_delete=django.db.models.deletion.PROTECT, related_name='books', to='library.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['name', 'author', 'creation_date'],
            },
        ),
    ]
