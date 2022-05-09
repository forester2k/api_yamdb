import csv

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title

User = get_user_model()

MODELS = {
    'category': Category,
    'comment': Comment,
    'genre': Genre,
    'genretitle': GenreTitle,
    'title': Title,
    'review': Review,
    'user': User,
}


class Command(BaseCommand):
    help = 'Import data from csv to database'

    def add_arguments(self, parser):
        parser.add_argument('model')
        parser.add_argument('csv_file')

    def handle(self, *args, **kwargs):
        try:
            model = MODELS[kwargs['model']]
            csv_file = kwargs['csv_file']
            with open(csv_file, 'rt', encoding='utf-8') as file:
                rows = csv.reader(file, dialect='excel')
                header = next(rows)
                for row in rows:
                    print('    ', *row)
                    _dict = {key: value for key, value in zip(header, row)}
                    model.objects.create(**_dict)
        except Exception as error:
            raise CommandError(error)
