from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=254, primary_key=True)
    password = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)
    username = models.CharField(unique=True, max_length=15, default="user")


class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.title) + "/" + str(self.created_by)


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commented_by = models.CharField(max_length=50)
    body = models.TextField()
