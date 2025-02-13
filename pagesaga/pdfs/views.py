from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializer import BookSerializer
import requests
from django.shortcuts import render

# books view
@api_view(['GET'])
def getBooks(request):
    book = Book.objects.all()
    bdata =  BookSerializer(Book, many=True).data
    return Response(bdata)



def home(request):
    api_url ="http://127.0.0.1:8000/api/books/'"
    response  = requests.get(api_url)
    books = response.json() if response.status_code == 200 else []

    return render(request, "home.html", {"books": books})

