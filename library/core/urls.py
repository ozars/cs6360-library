from django.urls import path
from .views import (
    HomeView, ImportFilesView, BookView, AuthorView, BorrowerView, LoanView,
    FineView
)

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),

    path('import/', ImportFilesView.as_view(), name='import_files'),
    path('import/ok', ImportFilesView.as_view(
        extra_context={'alert_msg': 'OK', 'alert_class': 'alert-success'}),
        name='import_files_success'),

    path('books/', BookView.List.as_view(), name='book_list'),
    path('books/<int:pk>', BookView.Detail.as_view(),
         name='book_detail'),
    path('books/create/', BookView.Create.as_view(),
         name='book_create'),
    path('books/update/<int:pk>', BookView.Update.as_view(),
         name='book_update'),

    path('authors/', AuthorView.List.as_view(), name='author_list'),
    path('authors/<int:pk>', AuthorView.Detail.as_view(),
         name='author_detail'),
    path('authors/create/', AuthorView.Create.as_view(),
         name='author_create'),
    path('authors/update/<int:pk>', AuthorView.Update.as_view(),
         name='author_update'),

    path('borrowers/', BorrowerView.List.as_view(), name='borrower_list'),
    path('borrowers/<int:pk>', BorrowerView.Detail.as_view(),
         name='borrower_detail'),
    path('borrowers/create/', BorrowerView.Create.as_view(),
         name='borrower_create'),
    path('borrowers/update/<int:pk>', BorrowerView.Update.as_view(),
         name='borrower_update'),

    path('loans/', LoanView.List.as_view(), name='loan_list'),
    path('loans/<int:pk>', LoanView.Detail.as_view(),
         name='loan_detail'),
    path('loans/create/', LoanView.Create.as_view(),
         name='loan_create'),
    path('loans/update/<int:pk>', LoanView.Update.as_view(),
         name='loan_update'),

    path('fines/', FineView.List.as_view(), name='fine_list'),
    path('fines/<int:pk>', FineView.Detail.as_view(),
         name='fine_detail'),
    #  path('fines/create/', FineView.Create.as_view(),
    #       name='fine_create'),
    #  path('fines/update/<int:pk>', FineView.Update.as_view(),
    #       name='fine_update'),
]
