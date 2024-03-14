from django.urls import path
from .views import GroupView, BooksView, BookTypeView, BooksEditView,  CategoryView, CategoryEditView, AuthorsView, AuthorsEditView, AddBookView, AddBookEditView, UserView


urlpatterns = [
    path('role/',GroupView.as_view),
    path('books/',BooksView.as_view()),
    path('book-type/',BookTypeView.as_view({'get':'list','post':'create'})),
    path('book-type/<int:pk>/',BookTypeView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('books/<int:pk>/',BooksEditView.as_view()),
    path('category/<int:pk>/',CategoryView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('category/<int:pk>/',CategoryEditView.as_view()),
    path('authors/<int:pk>/',AuthorsView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('authors/<int:pk>/',AuthorsEditView.as_view()),
     path('add-book/<int:pk>/',AddBookView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
     path('add-book/<int:pk>/',AddBookEditView.as_view()),
    path('register/',UserView.as_view({'post':'register'}),name='register'),
    path('login/',UserView.as_view({'post':'login'}),name='login'),




    



]