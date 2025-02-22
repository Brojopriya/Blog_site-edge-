from django.shortcuts import render
from post.models import Post
from post.models import comment
from django.views.generic import TemplateView



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
    post_data= Post.objects.get(id=id)
    comments = comment.objects.filter(post_id=id).select_related("user")
    context={
        "post":post_data,
        "comments":comments,
    }
    return render(request,"post_page.html",context)