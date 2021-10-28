from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def books_for_date_view(request, pub_date):
    template = 'books/books_for_date.html'

    books = Book.objects.filter(pub_date=pub_date)
    dates = Book.objects.all().values_list('pub_date', flat=True).order_by().distinct()

    # мне лень было писать бинарный поиск
    if len(dates) > 0:
        for i, date in enumerate(dates):
            if date == pub_date:
                date_index = i
                break

    prev_date = None
    next_date = None
    if date_index > 0:
        prev_date = dates[date_index - 1]
    if date_index < len(dates) - 1:
        next_date = dates[date_index + 1]

    context = {
        'pub_date': pub_date,
        'books': books,
        'prev_date': prev_date,
        'next_date': next_date,
    }
    return render(request, template, context)
