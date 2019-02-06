from django.urls import path
from .views import HomeView, BookView, AuthorView

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
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
]
