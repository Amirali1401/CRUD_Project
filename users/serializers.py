from rest_witchcraft.serializers import ModelSerializer

from database import Book , session , Category


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'



class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
