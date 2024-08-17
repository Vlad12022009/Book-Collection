from django.shortcuts import render, redirect
from .forms import BookForm
from .models import AuthorsModel, BookModel
# Create your views here.

def index(request):
    authors = AuthorsModel.objects.all()
    books = BookModel.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = BookForm(None)

    context = {
        'books': books,
        'form': form
    }
    return render(request, 'index.html', context=context)

def book(request, book):
    obj = BookModel.objects.get(bookContent=f'Book/{book}')
    with open(f'Book/{book}', 'r', encoding="utf-8") as f:
        context = {
            'obj': obj,
            'text': f.read()
        }
        return render(request, 'book.html', context=context)
    return redirect('/')