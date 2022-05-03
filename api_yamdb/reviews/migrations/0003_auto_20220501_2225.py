# Generated by Django 2.2.16 on 2022-05-01 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='reviews.Genre')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='title', to='reviews.Title')),
            ],
        ),
        migrations.AddField(
            model_name='title',
            name='genres',
            field=models.ManyToManyField(through='reviews.GenreTitle', to='reviews.Genre', verbose_name='Жанр'),
        ),
        migrations.AddConstraint(
            model_name='genretitle',
            constraint=models.UniqueConstraint(fields=('title', 'genre'), name='unique_title_genre'),
        ),
    ]