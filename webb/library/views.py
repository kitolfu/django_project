from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from library.models import Book, Author

def index(request):
    items = Book.objects.all()
    context = {'books': items}
    return render(request, 'books/index.html', context)

def authors_list(request):
    items = Author.objects.all()
    context = {'authors': items}
    return render(request, 'books/authors.html', context)

def book_detail(request, book_id):
    item = get_object_or_404(Book,pk=book_id)
    context = {'book':item}
    return render(request,'books/book_detail.html',context)