from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Post,Like
from django.urls import reverse_lazy




class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    fields = ('comment','liked')

class BlogCreateView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ['title','image','body']


def Like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id = post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like,created = Like.objects.get-or_create(user = user,post_id = post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        Like.save()

    return render('post:post-list')
