from django.db import models


class Book(models.Model):
    book_name=models.CharField(max_length=150,unique=True)
    price=models.IntegerField()
    pages=models.IntegerField()
    author=models.CharField(max_length=120)


    def __str__(self):
        return self.book_name

# python manage.py makemigrations
# then
# python manage.py migrate
#python manage.py shell
# start doing prgms