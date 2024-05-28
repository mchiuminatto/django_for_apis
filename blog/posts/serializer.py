from rest_framework.serializers import Serializer
from .models import Post


class PostSerializer(Serializer):

    class Meta:

        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at"
        )
        model=Post

