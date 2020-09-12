from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

# Create your models here.

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class BlogPost1(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_post')
    body= RichTextField(blank=True,null=True)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    TotalView=models.IntegerField(default=0)
    Likes=models.ManyToManyField(User,default=[0],blank=True,related_name='liked')
    Dis_Likes=models.ManyToManyField(User,default=[0],blank=True,related_name='unliked')
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects=CustomManager()
    tags=TaggableManager()


    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.Likes.count()

    def total_dislikes(self):
        return self.Dis_Likes.count()



    def get_absolute_url(self):
        lk=0
        dis=0
        return reverse('dashboard_url',args=[self.publish.year,self.publish.strftime('%m'),
        self.publish.strftime('%d'),self.slug,lk,dis])

    def get_url(self):
        lk=1
        dis=0
        return reverse('dashboard_url',args=[self.publish.year,self.publish.strftime('%m'),
        self.publish.strftime('%d'),self.slug,lk,dis])
    def get_url_dis(self):
        lk=0
        dis=1
        return reverse('dashboard_url',args=[self.publish.year,self.publish.strftime('%m'),
        self.publish.strftime('%d'),self.slug,lk,dis])




#Model releated to comment
class Comment(models.Model):
    post=models.ForeignKey(BlogPost1,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=256)
    email=models.EmailField()
    body=models.TextField("")
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)


    class Meta:
        ordering=('-created',)

    def __str__(self):
        return 'Commented by {} on {} '.format(self.name,self.post)


LIKES_CHOICES=(
('Like','Like'),
('Unlike','Unlike'),
)






class RequestForCode(models.Model):
    user=models.CharField(max_length=255)
    email=models.EmailField()
    Message=models.CharField(max_length=255)
    ProblemStatement=models.TextField()


class ProblemStatement(models.Model):
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    coder=models.ForeignKey(User,on_delete=models.CASCADE,related_name='problems')
    problemDescription= RichTextField(blank=True,null=True)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    TotalViewForProbelm=models.IntegerField(default=0)
    LikesForProbelm=models.ManyToManyField(User,default=[0],blank=True,related_name='liked_for_probelms')
    Dis_LikesForProbelm=models.ManyToManyField(User,default=[0],blank=True,related_name='unliked_for_probelms')




    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    def total_likes_for_Problems(self):
        return self.LikesForProbelm.count()

    def total_dislikes_fro_Problems(self):
        return self.Dis_LikesForProbelm.count()


    def get_problem_url1(self):
        lk=0
        dis=0
        ps=0
        return reverse('viewAllProbelms',args=[self.publish.year,self.publish.strftime('%m'),
        self.publish.strftime('%d'),self.slug,lk,dis,ps])

    def get_url_likes2(self):
        lk=1
        dis=0
        ps=0
        return reverse('viewAllProbelms',args=[self.publish.year,self.publish.strftime('%m'),
        self.publish.strftime('%d'),self.slug,lk,dis,ps])
    def get_url_dis2(self):
        lk=0
        dis=1
        ps=0
        return reverse('viewAllProbelms',args=[self.publish.year,self.publish.strftime('%m'),
        self.publish.strftime('%d'),self.slug,lk,dis,ps])


class Comment_Related_To_Problem(models.Model):
    question=models.ForeignKey(ProblemStatement,on_delete=models.CASCADE,related_name='ProblemComment')
    name=models.CharField(max_length=256)
    email=models.EmailField()
    reply=models.ForeignKey('Comment_Related_To_Problem',on_delete=models.CASCADE,null=True,related_name='replies')
    body=models.TextField("")
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)


    class Meta:
        ordering=('-created',)

    def __str__(self):
        return 'Commented by {} on {} '.format(self.name,self.question)



class DiscussionForum(models.Model):
    replyto=models.ForeignKey(Comment_Related_To_Problem,on_delete=models.CASCADE,related_name='Reply')
    replyer_name=models.ForeignKey(User,on_delete=models.CASCADE,related_name='replyer')
    reply=models.TextField("")
    reply_created=models.DateTimeField(auto_now=True)
    reply_updated=models.DateTimeField(auto_now=True)
    reply_active=models.BooleanField(default=True)


    class Meta:
        ordering=('-reply_created',)

    def __str__(self):
        return 'Reply by {} on {} '.format(self.replyer_name,self.replyto)


class OffCampusRecruitment(models.Model):
    title=models.CharField(max_length=500)
    adminName=models.CharField(default='Yuvraj',max_length=20)
    job_created=models.DateTimeField(auto_now=True)
    job_updated=models.DateTimeField(auto_now=True)
    description= RichTextField(blank=True,null=True)
    open=models.BooleanField(default=True)
    totalView=models.IntegerField(default=0)
