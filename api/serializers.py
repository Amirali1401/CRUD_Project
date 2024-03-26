from rest_witchcraft.serializers import ModelSerializer

from database import Book , session , sessionmaker , Category

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


    def create(self, validated_data):
        session = self.context['session']
        book  = Book(**validated_data)
        session.add(book)
        session.commit()
        return book





class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


    def create(self, validated_data):
        session = self.context['session']
        category  = Category(**validated_data)
        session.add(category)
        session.commit()
        return category
