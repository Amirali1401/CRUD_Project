from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from database import User , session ,Book ,  Category

from .serializers import BookSerializer , CategorySerializer



#
# class CategoryViewSet(ModelViewSet):
#     queryset = session.query(Category).all()
#     serializer_class = CategorySerializer
#
#
#
# class BookView(APIView):
#
#       def get(self , request):
#           book = session.query(Book).all()
#           serializer = BookSerializer(book , many=True )
#           return  Response(data = serializer.data)
#
#
#
#       def post(self , request):
#           serializer = BookSerializer(Book , data = request.POST)
#           serializer.is_valid(raise_exception=True)
#           serializer.save()
#           return Response({'message':'you created a book object'})
#
#
#
# class CategoryView(APIView):
#
#     def get(self, request):
#         category = session.query(Category).all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(data=serializer.data)
#
#
#
#     def post(self, request):
#         serializer = CategorySerializer(Category, data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'message': 'you created a category object'})


#
#
# class DetailViewBook(APIView):
#
#     def get(self, request, pk):
#         book = session.query(Book).filter_by(id=pk).first()
#         serializer = BookSerializer(book)
#         return Response(data=serializer.data)
#
#
#
#     def put(self, request, pk):
#         book = session.query(Book).filter_by(id=pk).first()
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data)
#
#
#     def delete(self, request, pk):
#         book = session.query(Book).filter_by(id=pk).first()
#         session.delete(book)
#         session.commit()
#         return Response({'message': 'you deleted an object!!!'})



