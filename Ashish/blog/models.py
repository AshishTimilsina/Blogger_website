from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    head0 = models.CharField(max_length=500, default="")
    para0 = models.CharField(max_length=50000, default="")
    head1 = models.CharField(max_length=500, default="")
    para1 = models.CharField(max_length=50000, default="")
    head3 = models.CharField(max_length=500, default="")
    para3 = models.CharField(max_length=50000, default="")
    head4 = models.CharField(max_length=500, default="")
    para4 = models.CharField(max_length=50000, default="")
    Pub_date = models.DateField()
    Thumbnail = models.ImageField(upload_to='blog/images', default="")


    def __str__(self):
     return self.title


class Contact(models.Model):
    traffic_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=40,default=0)
    desc=models.CharField(max_length=500)

    def __str__(self):
        return self.name +" - "+ self.email

class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timeStamp=models.DateTimeField(default=now)
    
    
