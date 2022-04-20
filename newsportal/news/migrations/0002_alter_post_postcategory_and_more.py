# Generated by Django 4.0.4 on 2022-04-20 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postCategory',
            field=models.ManyToManyField(through='news.PostCategory', to='news.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='categotyThorugh',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='postThrough',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post', verbose_name='Новость(Статья)'),
        ),
    ]
