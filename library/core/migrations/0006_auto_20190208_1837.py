# Generated by Django 2.2a1 on 2019-02-09 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190208_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='authored',
            field=models.ManyToManyField(auto_created=True, related_name='_author_authored_+', through='core.BookAuthor', to='core.Book', verbose_name='Books'),
        ),
        migrations.AlterField(
            model_name='book',
            name='authored_by',
            field=models.ManyToManyField(auto_created=True, related_name='_book_authored_by_+', through='core.BookAuthor', to='core.Author', verbose_name='Authors'),
        ),
    ]