from django.shortcuts import render
from post.models import Post


# Create your views here.

def post_list_view(request):


    post_data = Post.objects.all()
    context={
        "data":post_data
    }

    return render (request,"post-list.html",contex