from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse

from datetime import date, timedelta

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    isbn = models.CharField(unique=True,
            validators=[RegexValidator(regex=r'^\d{10}$',
                message='ISBN must consist of ten digits.', code='nomatch')],
            max_length=10)
    title = models.CharField(max_length=256)
    authored_by = models.ManyToManyField('Author', through='BookAuthor',
                                         through_fields=('book', 'author'))

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'BOOK'

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author-view", kwargs={'author_id': self.author_id})

    class Meta:
        db_table = 'AUTHORS'

class BookAuthor(models.Model):
    author = models.ForeignKey(Author, to_field='author_id',
                               on_delete=models.CASCADE)
    book = models.ForeignKey(Book, to_field='isbn', db_column='isbn',
                             on_delete=models.CASCADE)

    class Meta:
        db_table = 'BOOK_AUTHORS'

class Borrower(models.Model):
    card_id = models.AutoField(primary_key=True)
    ssn = models.CharField(max_length=9, unique=True)
    bname = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)

    def __str__(self):
        return self.bname

    class Meta:
        db_table = 'BORROWER'

def _default_due_date():
    return date.today() + timedelta(days=14)

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             to_field='isbn', db_column='isbn',
                             related_name='loans')
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE,
                                 to_field='card_id', db_column='card_id',
                                 related_name='loans')
    date_out = models.DateField(default=date.today)
    due_date = models.DateField(default=_default_due_date)
    date_in = models.DateField(null=True)

    class Meta:
        db_table = 'BOOK_LOANS'

class Fine(models.Model):
    loan = models.OneToOneField(Loan, on_delete=models.CASCADE,
                                to_field='loan_id', related_name='fine',
                                primary_key=True)
    fine_amt = models.DecimalField(max_digits=7, decimal_places=2)
    paid = models.BooleanField(default=False)

    class Meta:
        db_table = 'FINES'