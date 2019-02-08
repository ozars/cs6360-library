from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.urls import reverse_lazy

from .models import Book, Author, BookAuthor, Borrower, Loan, Fine

class HomeView(TemplateView):
    template_name = 'home.html'

class BookView:
    class List(ListView):
        model = Book

    class Detail(DetailView):
        model = Book

    class BaseModify(FormView):
        model = Book
        fields = ['isbn', 'title', 'authored_by']
        success_url = reverse_lazy('book_list')
        def form_valid(self, form):
            return super().form_valid(form)

    class Create(BaseModify, CreateView):
        pass

    class Update(BaseModify, UpdateView):
        pass

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

class BorrowerView:
    class List(ListView):
        model = Borrower

    class Detail(DetailView):
        model = Borrower

    class Create(CreateView):
        model = Borrower
        fields = ['ssn', 'bname', 'address', 'phone']
        success_url = reverse_lazy('borrower_list')

    class Update(UpdateView):
        model = Borrower
        fields = ['ssn', 'bname', 'address', 'phone']
        success_url = reverse_lazy('borrower_list')

class LoanView:
    class List(ListView):
        model = Loan

    class Detail(DetailView):
        model = Loan

    class Create(CreateView):
        model = Loan
        fields = ['loan_id', 'book', 'borrower', 'date_out', 'due_date']
        success_url = reverse_lazy('loan_list')

    class Update(UpdateView):
        model = Borrower
        fields = ['loan_id', 'book', 'borrower', 'date_out', 'due_date',
                  'date_in']
        success_url = reverse_lazy('loan_list')

class FineView:
    class List(ListView):
        model = Fine

    class Detail(DetailView):
        model = Fine
