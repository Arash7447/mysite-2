from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
# from blog.models import Post, Comment
# from django.utils import timezone
# from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# from blog.forms import CommentForm
# from django.contrib import messages
from django.urls import reverse
# Create your views here.

def blog_view(request):
    return render(request, "blog/blog-sidebar.html")


def blog_single(request):
    return render(request, 'blog/blog-single.html')