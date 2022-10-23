from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateTimeField('birth date')
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_published = models.DateTimeField('date published')
    def __str__(self):
        return f"{str(self.title), str(self.author)}"
