from django.db import models


class Title(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр'
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг',
        null=True,
        default=None)
    description = models.TextField(
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['title']
