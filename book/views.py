from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .models import Books, BookType, Category, Authors, User
from add_book.models import AddBook
from .serializers import BooksSerializer, BookTypeSerializer,CategorySerializer, AuthorsSerializer, AddBookSerializer, UserSerializer, GroupSerializer
from django.contrib.auth.models import Group
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authtoken.models import Token
from rest_framework import filters
from rest_framework.permissions import AllowAny



# Create your views here.
class GroupView(ModelViewSet):
    serislizer_class = GroupSerializer
    permession_classes = [AllowAny]


class BooksView(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    filters_fields = ['type']
    search_fields = ['name', 'description']


class BookTypeView(ModelViewSet):
    queryset = BookType.objects.all()
    serializer_class = BookTypeSerializer
    filters_fields = ['type']
    search_fields = ['name', 'description']


class BooksEditView(GenericAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

def get(self,request,pk):
    try:
        Books_obj = Books.objects.get(id=pk)
    except:
        return Response('Data not found!')
    serializer = BooksSerializer(Books_obj)
    return Response(serializer.data)

def put(self,request,pk):
    try:
        Books_obj = Books.objects.get(id=pk)
    except:
        return Response('Data not found!')
    serializer = BooksSerializer(Books_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    

def delete(self,request,pk):
    try:
        Books_obj = Books.objects.all(id=pk)
    except:
        return Response('Data not found!')
    Books_obj.delete()
    return Response('Data Deleted')



class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filters_fields = ['type']
    search_fields = ['name', 'description']

class CategoryEditView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def get(self,request,pk):
    try:
        Category_obj = Books.objects.get(id=pk)
    except:
        return Response('Data not found!')
    serializer = CategorySerializer(Category_obj)
    return Response(serializer.data)

def put(self,request,pk):
    try:
        Category_obj = Category.objects.get(id=pk)
    except:
        return Response('Data not found!')
    serializer = CategorySerializer(Category_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    

def delete(self,request,pk):
    try:
        Category_obj = Category.objects.all(id=pk)
    except:
        return Response('Data not found!')
    Category_obj.delete()
    return Response('Data Deleted')




class AuthorsView(ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    filters_fields = ['type']
    search_fields = ['name', 'description']


class AuthorsEditView(GenericAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer

def get(self,request,pk):
    try:
        Authors_obj = Authors.objects.get(id=pk)
    except:
        return Response('Data not found!')
    serializer = BooksSerializer(Authors_obj)
    return Response(serializer.data)

def put(self,request,pk):
    try:
        Authors_obj = Authors.objects.get(id=pk)
    except:
        return Response('Data not found!')
    serializer = AuthorsSerializer(Authors_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    

def delete(self,request,pk):
    try:
        Authors_obj = Authors.objects.all(id=pk)
    except:
        return Response('Data not found!')
    Authors_obj.delete()
    return Response('Data Deleted')




class AddBookView(ModelViewSet):
    queryset = AddBook.objects.all()
    serializer_class = AddBookSerializer
    filters_fields = ['type']
    search_fields = ['name', 'description']

class AddBookEditView(GenericAPIView):
    queryset = AddBook.objects.all()
    serializer_class = AddBookSerializer

def get(self,request,pk):
    try:
        AddBook_obj = AddBook.objects.get(id=pk)
    except:
        return Response('Data not found!')
    serializer = AddBookSerializer(AddBook_obj)
    return Response(serializer.data)

def put(self,request,pk):
    try:
        AddBook_obj = AddBook.objects.get(id=pk)
    except:
        return Response('Data not found!')
    serializer = AddBookSerializer(AddBook_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    

def delete(self,request,pk):
    try:
        AddBook_obj = AddBook.objects.all(id=pk)
    except:
        return Response('Data not found!')
    AddBook_obj.delete()
    return Response('Data Deleted')



class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


    def register(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            password = request.data.get('password')
            hash_password = make_password(password)
            a = serializer.save()
            a.password = hash_password
            a.save()
            return Response('User Created Sucessfull!')
        else:
            return Response(serializer.errors)
        

    def login(self,request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(username=email,password=password)

        if user == None:
            return Response('Invalid Credentials!')
        else:
            token,_ = Token.objects.get_or_create(user=user)
            return Response(token.key)

