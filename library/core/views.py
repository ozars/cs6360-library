from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Book, Author, BookAuthor, Borrower, Loan, Fine

class HomeView(TemplateView):
    template_name = 'home.html'

class BookView:
    class List(ListView):
        model = Book

    class Detail(DetailView):
        model = Book

    class Create(CreateView):
        model = Book
        fields = ['isbn', 'title', 'authored_by']
        success_url = reverse_lazy('book_list')

    class Update(UpdateView):
        model = Book
        fields = ['isbn', 'title', 'authored_by']
        success_url = reverse_lazy('book_list')

class AuthorView:
    class List(ListView):
        model = Author

    class Detail(DetailView):
        model = Author

    class Create(CreateView):
        model = Author
        fields = ['name']
        success_url = reverse_lazy('author_list')

    class Update(UpdateView):
        model = Author
        fields = ['name']
        success_url = reverse_lazy('author_list')
