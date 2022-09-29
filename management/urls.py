from . import views
from django.urls import path

urlpatterns = [
	path('books/', views.add_books, name="listBooks"),
	path('books/<int:id>', views.edit_book, name="datails"),
	path('borrow/', views.borrowed_book),
	
]
