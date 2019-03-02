from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.urls import reverse_lazy
import django_tables2 as tables

from .models import Book, Author, BookAuthor, Borrower, Loan, Fine
from .forms import ImportFilesForm, BookForm

import logging
logger = logging.getLogger(__name__)

class HomeView(TemplateView):
    template_name = 'home.html'

class ImportFilesView(FormView):
    template_name = 'import_files.html'
    form_class = ImportFilesForm
    success_url = reverse_lazy('import_files_success')

    def form_valid(self, form, **kwargs):
        form.import_files()
        logger.critical('Importing')
        return super().form_valid(form)

    def form_invalid(self, form):
        logger.critical(form.errors)
        return super().form_invalid(form)

class BookView:
    #  class List(generic_table_view(Book)):
    #      pass

    class Table(tables.Table):
        isbn = tables.Column()
        title = tables.Column()
        authored_by = tables.ManyToManyColumn(linkify_item=True)
        status = tables.Column(linkify=True, default="Available",
                accessor="loans.objects.latest()",
                verbose_name="Status")

    class List(tables.SingleTableView):
        queryset = Book.objects.all()

        @staticmethod
        def get_table_class():
            return BookView.Table

    #  class List(ListView):
    #      model = Book

    class Detail(DetailView):
        model = Book

    class BaseModify(FormView):
        model = Book
        form_class = BookForm
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
