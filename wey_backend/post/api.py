from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import api_view, authentication_classes, permission_classes

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def post_create(request):
    data = request.data
    print(data)

    return JsonResponse({'hello': 'Hepp'})