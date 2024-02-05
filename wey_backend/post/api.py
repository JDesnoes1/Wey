from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PostSerializer
from .forms import PostForm
from .models import Post
from rest_framework.decorators import api_view, authentication_classes, permission_classes

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def post_create(request):
    form = PostForm(request.data)

    if form.is_valid():
        
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()

        # Pour faire en faire en sorte que le poste apparaisse directement sur la page
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data, safe=False)
    
    else:
        return JsonResponse({'error': 'Le formulaire est pas valide'})



    return JsonResponse({'hello': 'Hepp'})