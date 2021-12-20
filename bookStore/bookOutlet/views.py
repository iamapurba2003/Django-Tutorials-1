from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, "bookOutlet/index.html", {
        "books":books
    })


def bookDetail(request, slug):
    # try:
    #     books = Book.objects.get(pk=id)
    # except Exception:
    #     raise Http404
    
    # the below code also execute the same way as the above code block...
    
    books = get_object_or_404(Book, slug=slug)
    
    return render(request, "bookOutlet/bookDetail.html",{
        "bookTitle":books.title,
        "bookAuthor": books.author,
        "bookRating":books.rating,
        "bookBestSelling":books.isBestSelling
    })