from django import forms
from itertools import islice
from .models import Book, Author, Borrower, BookAuthor
import csv
import io

import logging
logger = logging.getLogger(__name__)

class ImportFilesForm(forms.Form):
    books_file = forms.FileField()
    borrowers_file = forms.FileField()

    def import_files(self):
        books = {}
        authors = set()
        borrowers = []

        Book.objects.all().delete()
        Author.objects.all().delete()
        Borrower.objects.all().delete()

        with self.cleaned_data.get('books_file').open('r') as bf:
            it = iter(bf)
            next(it)
            for row in it:
                row = list(map(str.strip, row.decode('utf-8').split("\t")))
                isbn, title, authored_by  = row[0], row[2], row[3].split(',')
                books[isbn] = {'title': title, 'authored_by': authored_by}
                authors.update(authored_by)
        Author.objects.bulk_create(Author(name=a) for a in authors)
        Book.objects.bulk_create(
                Book(isbn=k, title=v['title']) for k, v in books.items())
        authors = {a.name: a for a in Author.objects.all()}
        BookAuthor.objects.bulk_create(
            BookAuthor(book=b, author=authors[a])
                for b in Book.objects.all()
                    for a in books[b.isbn]['authored_by'])

        with self.cleaned_data.get('borrowers_file').open('r') as bf:
            it = iter(bf)
            next(it)
            for row in it:
                row = list(map(str.strip, row.decode('utf-8').split(",", 5)))
                bid, ssn, bname, last = (
                    row[0], row[1].replace('-', ''), row[2]+' '+row[3], row[5]
                )
                address, phone = last.rsplit(',', 1)
                borrowers.append(Borrower(card_id=bid, ssn=ssn, bname=bname,
                    address=address, phone=phone))
        Borrower.objects.bulk_create(borrowers)

class BookForm(forms.ModelForm):
    authored_by = forms.ModelMultipleChoiceField(queryset=Author.objects.all().order_by('name'))
    class Meta:
        model = Book
        fields = ['isbn', 'title', 'authored_by']
