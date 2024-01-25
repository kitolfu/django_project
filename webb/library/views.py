from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from library.models import Book

def books(request):
    items = Book.objects.all()
    context = {'books':items}
    return render(request, 'index.html', context)

def book(request, pk):
    item = get_object_or_404(Book, pk=pk)
    context = {'book':item}
    return render(request, 'book.html', context)

def index(request):
    return HttpResponse(
        'Ты <i>не можешь</i> получить правильные <b>ответы</b>,<br> '
        'если у тебя нет правильных <s>вопросов</s> запросов.')
