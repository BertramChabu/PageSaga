from django.db import models



class Genre(models.TextChoices):
    FICTION = "FIC", "Fiction"
    MANGA = "MNG", "Manga"
    MANHWA = "MNW", "Manhwa"
    COMIC = "CMC", "Comic"
    FANTASY = "FA", "Fantasy"

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    genre = models.CharField(
        max_length=3,
        choices=Genre.choices,
        default=Genre.FICTION
    )
    cover_image = models.ImageField(upload_to="book_covers/", blank=True, null=True)
    pdf_file = models.FileField(upload_to="pdf_books/")


    def __str__(self):
        return self.title

