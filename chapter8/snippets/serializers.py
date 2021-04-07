from rest_framework import serializers
from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'description', 'created_by', 'created_at', 'updated_at')
