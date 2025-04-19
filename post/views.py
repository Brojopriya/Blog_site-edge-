from django.shortcuts import render, redirect, get_object_or_404
from post.models import Post
from post.models import comment
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from post.forms import CommentForm 


class PostListTemplate(TemplateView):
    template_name= "post-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_data = Post.objects.all()
        context["data"]=post_data
        return context

# Create your views here.

def post_list_view(request):
    post_data = Post.objects.all()  # Fetch all posts
    context = {
        'data': post_data  # Pass the post data to the template
    }
    

    return render(request, "post-list.html", context)


def portfolio_view(request):
    portfolio_data= Post.objects.all().order_by('-id')[:3]

    context={
        "data":portfolio_data
    }
    return render(request,"portfolio.html",context)

def post_page_view(request,id):
    print("This massage" , request.method)

    post_data=get_object_or_404(Post,id=id)
    # try:
    #     post_data= Post.objects.get(id=id)
    #     print(post_data)
    # except ObjectDoesNotExist:
    #     raise Http404("page not found")



    comments = comment.objects.filter(post_id=id).select_related("user")
    context={
        "post":post_data,
        "comments":comments,
    }
    return render(request,"post_page.html",context)


def add_comment(request, id):
     post = get_object_or_404(Post, id=id)
     if request.method == "POST":
         text = request.POST.get("text")
         if text:
             comment.objects.create(post=post, user=request.user, text=text)
     return redirect('one-post', id=post.id)  