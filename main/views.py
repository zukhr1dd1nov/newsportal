from django.contrib import messages
from django.shortcuts import render , redirect
from main.forms import PostForm
from django.utils.translation import gettext_lazy as _
from .models import Post , Category

# Create your views here.

def main_index(request):
    posts = Post.objects.order_by('-added_at')[:8]
    categories = Category.objects.order_by('id').all()
    return render(request , "main/index.html" , {
        "posts" : posts,
        "categories" : categories
    })

def main_posts(request , cid):
    posts = Post.objects.filter(category_id=cid).order_by('-added_at')[:8]
    categories = Category.objects.order_by('id').all()
    return render(request , "main/index.html" , {
        "posts" : posts,
        "categories" : categories
    })

def main_post_read(request,pid):
    post = Post.objects.get(id=pid)

    return render(request, 'main/read.html' , {
        'post' : post
    })


def main_post_add(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()

            messages.success(request,_("Maqola muvafaqqiyatli qo'shildi."))

            return redirect('main_index')

    return render(request, 'main/post.html' , {
        'form':form
    })