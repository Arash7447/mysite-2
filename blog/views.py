from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
# Create your views here.



def blog_view(request, **kwargs) :
    posts = Post.objects.filter(status = 1, published_date__lte = timezone.now())
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    posts = Paginator (posts,3)
    try:
        page_number = request.GET.get ('page')
        posts = posts.get_page(page_number)

    except PageNotAnInteger:
        
        posts = posts.get_page(1)

    except EmptyPage:

        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, "blog/blog-sidebar.html", context)



def blog_single(request):
    return render(request, 'blog/blog-single.html')