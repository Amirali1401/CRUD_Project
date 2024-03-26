from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView , ListCreateAPIView
from rest_framework.viewsets import ModelViewSet , GenericViewSet
from rest_framework.generics import CreateAPIView , ListCreateAPIView , ListAPIView , RetrieveAPIView , GenericAPIView
from rest_framework.mixins import RetrieveModelMixin , CreateModelMixin , DestroyModelMixin , UpdateModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , IsAdminUser


from database import Book ,session , Category

from .serializers import BookSerializer , CategorySerializer



class BookViewSet(ListCreateAPIView , CreateModelMixin  , GenericViewSet):
    serializer_class = BookSerializer
    queryset = session.query(Book).all()

    def get_serializer_context(self):
        return {'request':self.request , 'session':session}




class DetailBookViewSet(APIView):

    def get(self , request , pk):
        book = session.query(Book).get( pk)
        serializer = BookSerializer(book)
        return Response(data = serializer.data)



    def delete(self , request , pk):
        book = session.query(Book).get(pk)
        session.delete(book)
        session.commit()
        return Response({'message':'you deleted this object'})



    def put(self , request , pk):
        book = session.query(Book).get(pk)
        serializer = BookSerializer(book , data = request.data )
        serializer.is_valid(raise_exception=True)
        book.id = serializer.validated_data['id']
        book.name = serializer.validated_data['name']
        session.commit()
        return Response(data = serializer.data)





class CategoryViewSet(ModelViewSet):
    queryset = session.query(Category).all()
    serializer_class = CategorySerializer

    def get_serializer_context(self):
        return {'request':self.request , 'session':session}





class DetailCategoryViewSet(APIView):

    def get(self , request , pk):
        category = session.query(Category).get(pk)
        serializer = CategorySerializer(category )
        return Response(data = serializer.data)


    def delete(self , request , pk):
        category = session.query(Category).get(pk)
        session.delete(category)
        session.commit()
        return Response({'message':'you deleted this object'})


    def put(self , request , pk):
        category = session.query(Category).get(pk)
        serializer = CategorySerializer(category , data = request.data)
        serializer.is_valid(raise_exception=True)
        category.id  = serializer.validated_data['id']
        category.name = serializer.validated_data['name']
        session.commit()
        return Response(data = serializer.data)







