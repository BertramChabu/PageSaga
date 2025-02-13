# Generated by Django 5.1.6 on 2025-02-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('genre', models.CharField(choices=[('FIC', 'Fiction'), ('MNG', 'Manga'), ('MNW', 'Manhwa'), ('CMC', 'Comic'), ('FA', 'Fantasy')], default='FIC', max_length=3)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_covers/')),
                ('pdf_file', models.FileField(upload_to='pdf_books/')),
            ],
        ),
    ]
