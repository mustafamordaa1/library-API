from rest_framework import serializers
from .models import Book, borrow
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username

        return data
        
class UserSerializer(serializers.ModelSerializer):
     class Meta:
     	model = User
     	fields = ['id','username', "first_name", "last_name", "email"]
  
class BookSerializer(serializers.ModelSerializer):
    isbn = serializers.CharField(max_length=512)
    class Meta:
        model = Book
        fields = ["id", 'title', 'isbn', 'author', 'year', 'rate', 'image']
        
class BorrowSerializer(serializers.ModelSerializer):
    #customer = serializers.RelatedField(source='User.id', read_only=True)
#    books = serializers.RelatedField(source='Book.title', read_only=True)
    #book = serializers.RelatedField(queryset=Book.objects.all())
#    book = BookSerializer(book, many= True)
    class Meta:
        model = borrow        
        fields = ("user", "book" ,"date", "expDate")
        read_only_fields = ()
    
    def to_representation(self, instance):
      #  self.fields["book"] = BookSerializer(read_only= True, many= True)
        self.fields['user'] =  UserSerializer(read_only=True)
        self.fields['book'] =  BookSerializer(many=True, read_only=True)
        return super(BorrowSerializer, self).to_representation(instance)
