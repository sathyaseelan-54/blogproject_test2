from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField()
    body = models.TextField()
    liked = models.ManyToManyField(User,default = None,blank = True,related_name = 'liked')
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


    @property
    def num_likes(self):
        return self.liked.all().count()



LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike')
)


class Like(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    value = models.CharField(choices = LIKE_CHOICES,default = 'Like',max_length = 15)

    def __str__(self):
        return str(self.post)