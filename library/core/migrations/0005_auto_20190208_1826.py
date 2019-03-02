# Generated by Django 2.2a1 on 2019-02-09 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190208_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookauthor',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.Author'),
        ),
        migrations.AlterField(
            model_name='bookauthor',
            name='book',
            field=models.ForeignKey(db_column='isbn', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.Book', to_field='isbn'),
        ),
    ]
