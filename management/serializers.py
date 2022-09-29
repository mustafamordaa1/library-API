from rest_framework import serializers
from books.models import Book, borrow

class BookSerializer(serializers.ModelSerializer):
    isbn = serializers.CharField(max_length=512)
    class Meta:
        model = Book
        fields = ["id", 'title', 'isbn', 'author', 'year', 'rate', 'image']
        
class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = borrow        
        fields = ("user", "book" ,"date", "expDate")
        read_only_fields = ()
    
    def to_representation(self, instance):
      #  self.fields["book"] = BookSerializer(read_only= True, many= True)
        self.fields['user'] =  UserSerializer(read_only=True)
        self.fields['book'] =  BookSerializer(many=True, read_only=True)
        return super(BorrowSerializer, self).to_representation(instance)