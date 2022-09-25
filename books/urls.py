from . import views
#from .views import RegisterView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
	path('books/', views.list_books, name="listBooks"),
	path('books/<int:id>', views.book_detail, name="datails"),
	path('borrow/', views.borrow_book),
	path('borrow/<int:id>', views.user_books),
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.create_auth)#RegisterView.as_view())
]
