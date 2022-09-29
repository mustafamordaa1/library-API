from django.shortcuts import render
from .serializers import BookSerializer, BorrowSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from books.models import Book, borrow
from rest_framework.authentication import  BasicAuthentication

# Create your views here.

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def add_books(request):
	       
	if request.method == 'POST':
	       serializer = BookSerializer(data=request.data)
	       if serializer.is_valid():
	           serializer.save()
	           return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def edit_book(request, id, format=None):

    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def borrowed_book(request):
	      
		if request.method == 'GET':
		      borrows =  borrow.objects.all()
		      serializer = BorrowSerializer(borrows, many=True)
		      return Response(serializer.data)
	       
