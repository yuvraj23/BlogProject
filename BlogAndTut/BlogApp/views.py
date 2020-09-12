from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from BlogApp.models import BlogPost1,RequestForCode,ProblemStatement,Comment_Related_To_Problem,OffCampusRecruitment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from BlogApp.forms import CommentForm,Comment_Related_To_ProblemForm,SignUpForm
from django.contrib.auth.models import User
from taggit.models import Tag
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.

def PrivacyPolicy(request):
    return render(request,'Blog/privancy_policy.html')


def TermsAndConditions(request):
    return render(request,'Blog/terms_and_conditions.html')




def signup_view(request):
    form=SignUpForm()
    if request.method=="POST":
            form=SignUpForm(request.POST)
            if form.is_valid():
                user=form.save()
                user.set_password(user.password)
                user.save()
                return HttpResponseRedirect('/accounts/login/')
    return render(request,'Blog/signup.html',{'form':form})

def ViewProfile(request,id=0):
    MyDetail=User.objects.get(id=id)
    return render(request,'Blog/Profile.html',{'MyDetail':MyDetail})


@login_required
def problemSet(request):
    problemStatement_List=ProblemStatement.objects.all()
    return render(request,'Blog/allProblem.html',{'problemStatement_List':problemStatement_List})
@login_required
def BlogSet(request):
    post_list=BlogPost1.objects.all()
    return render(request,'Blog/allBlog.html',{'post_list':post_list})
@login_required
def JobSet(request):
    job_list=OffCampusRecruitment.objects.all()
    return render(request,'Blog/allJob.html',{'job_list':job_list})



def home(request,varblog=0,varPro=0):
    post_list=BlogPost1.objects.all()
    problemStatement_List=ProblemStatement.objects.all()
    offcampus=OffCampusRecruitment.objects.all()
    paginator1=Paginator(post_list,3)
    page_number1=request.GET.get('page')
    paginator2=Paginator(problemStatement_List,3)
    page_number2=request.GET.get('page')
    paginator3=Paginator(offcampus,3)
    page_number3=request.GET.get('page')





    try:
        offcampus=paginator3.page(page_number3)
    except PageNotAnInteger:
        offcampus=paginator3.page(1)
    except EmptyPage:
        offcampus=paginator3.page(paginator3.num_pages)

    try:
        post_list=paginator1.page(page_number1)
    except PageNotAnInteger:
        post_list=paginator1.page(1)
    except EmptyPage:
        post_list=paginator1.page(paginator2.num_pages)

    try:
        problemStatement_List=paginator2.page(page_number2)
    except PageNotAnInteger:
        problemStatement_List=paginator2.page(1)
    except EmptyPage:
        problemStatement_List=paginator2.page(paginator2.num_pages)


    return render(request,'Blog/home.html',{'post_list':post_list,'offcampus':offcampus,'problemStatement_List':problemStatement_List,'varblog':varblog,'varPro':varPro,
    })


def blog(request):
    return render(request,'Blog/blog-home.html')


def about(request):
    return render(request,'Blog/about.html')
@login_required
def OffCampusDrive(request,id=id):
    offcampus=get_object_or_404(OffCampusRecruitment,id=id)
    offcampus.totalView=int(offcampus.totalView)+1
    offcampus.save()
    tview=offcampus.totalView
    return render(request,'Blog/offcampus.html',{'offcampus':offcampus,'view':tview})





@login_required
def dashboard(request,year,month,day,post,lk=0,dis=0):
    post=get_object_or_404(BlogPost1,slug=post,status='published',publish__year=year,
    publish__month=month,publish__day=day,)
    total_view=post.TotalView
    if str(lk)=="0" and str(dis)=="0":
        total_view=post.TotalView+1
        post.TotalView=total_view

    if str(lk)=="0" and str(dis)=="0":
        if request.user in post.Likes.all():
            lk="1"
        elif request.user in post.Dis_Likes.all():
            dis="1"

    if request.user in post.Likes.all() and str(dis)=="1":
        post.Likes.remove(request.user)
        post.Dis_Likes.add(request.user)
    elif str(lk)=="1":
        post.Dis_Likes.add(request.user)

    if request.user in post.Dis_Likes.all() and str(lk)=="1":
        post.Dis_Likes.remove(request.user)
        post.Likes.add(request.user)
    elif str(dis)=="1":
        post.Dis_Likes.add(request.user)

    total_like=post.total_likes()
    total_dislike=post.total_dislikes()
    lst=["0","1"]

    post.save()
    if request.user.is_authenticated:
        comments=post.comments.filter(active=True)
        csubmit=False
        if request.method=='POST':
            form=CommentForm(request.POST)
            if form.is_valid():
                new_comment=form.save(commit=False)
                new_comment.post=post
                new_comment.name= request.user.username
                new_comment.email= request.user.email
                new_comment.save()
                csubmit=True
        else:
            form=CommentForm()
        return render(request,'Blog/dashboard.html',{'post':post,'form':form,'csubmit':csubmit,
        'comments':comments,'total_like':total_like,"total_dislike":total_dislike,
        'total_view':total_view,'dis':dis,'lk':lk,'lst':lst,})
    else:
        messages.success(request,'Login Required')
        return HttpResponseRedirect('/login/')
















"""def SignIn(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations! Account Create SuccessFully. Login To Read Our Blogs')
            form.save()
            return HttpResponseRedirect('/accounts/login')

    else:
        form=SignUpForm()
    return render(request,'Blog/signup.html',{'form':form})

def LogIn(request):
        form=LoginForm()
        if request.method == 'POST':
                form=LoginForm(request=request,data=request.POST)
                if form.is_valid():
                    uname=form.cleaned_data['username']
                    password=form.cleaned_data['password']
                    user=authenticate(username=uname,password=password)
                    if user is not None:
                        login(request,user)
                        post_list=BlogPost.objects.all()
                        problemStatement_List=ProblemStatement.objects.all()
                        paginator=Paginator(post_list,3)
                        page_number=request.GET.get('page')

                        try:
                            post_list=paginator.page(page_number)
                        except PageNotAnInteger:
                            post_list=paginator.page(1)
                        except EmptyPage:
                            post_list=paginator.page(paginator.num_pages)

                        try:
                            problemStatement_List=paginator.page(page_number)
                        except PageNotAnInteger:
                            problemStatement_List=paginator.page(1)
                        except EmptyPage:
                            problemStatement_List=paginator.page(paginator.num_pages)


                        return render(request,'Blog/home.html',{'post_list':post_list,'problemStatement_List':problemStatement_List})

                        #messages.success(request,'Logged in SuccessFully')

                    else:
                        messages.success(request,'Login Credentials Is Invalid')
                        return render(request,'Blog/login.html',{'form':form})


        else:
                return render(request,'Blog/login.html',{'form':form})


def LogOut(request):
    if not request.user.is_authenticated:
        return render(request,'Blog/login.html')

    elif request.user.is_authenticated:
        logout(request)
        messages.success(request,'LogOut SuccessFully')
        post_list=BlogPost.objects.all()
        problemStatement_List=ProblemStatement.objects.all()
        paginator=Paginator(post_list,3)
        page_number=request.GET.get('page')

        try:
            post_list=paginator.page(page_number)
        except PageNotAnInteger:
            post_list=paginator.page(1)
        except EmptyPage:
            post_list=paginator.page(paginator.num_pages)

        try:
            problemStatement_List=paginator.page(page_number)
        except PageNotAnInteger:
            problemStatement_List=paginator.page(1)
        except EmptyPage:
            problemStatement_List=paginator.page(paginator.num_pages)
        return render(request,'Blog/home.html',{'post_list':post_list,'problemStatement_List':problemStatement_List})

"""
@login_required
def Coding_Request(request):
        if request.method == 'POST':
            if request.POST.get('username') and request.POST.get('email') and request.POST.get('msg') and request.POST.get('Ps'):
                ProSat=RequestForCode()
                ProSat.user= request.user.username
                ProSat.email= request.user.email
                ProSat.Message= request.POST.get('msg')
                ProSat.ProblemStatement= request.POST.get('Ps')
                ProSat.save()
                html_content=render_to_string('Blog/email_file.html',{'title':ProSat.Message,'ProblemStatement':ProSat.ProblemStatement,'email':ProSat.email,'user':ProSat.user})
                text_content=strip_tags(html_content)


                if str(request.user.email) == str(ProSat.email):
                    email=EmailMultiAlternatives(
                    'Problem received by CodeHoolic',
                    text_content,
                    settings.EMAIL_HOST_USER,
                    ['coolcodersingh@gmail.com','imcodehoolic@gmail.com',request.user.email]
                    )

                else:
                    email=EmailMultiAlternatives(
                    'Problem received by CodeHoolic',
                    text_content,
                    settings.EMAIL_HOST_USER,
                    ['coolcodersingh@gmail.com','imcodehoolic@gmail.com',ProSat.email,request.user.email]
                    )







                #send_mail("jjjhs","ndjnndn",'ImCodeHoolic',['yuvraj776524@gmail.com'])
                email.attach_alternative(html_content,'text/html')
                email.send()
                send=True
                return render(request, 'Blog/about.html')

        else:
                return render(request,'Blog/home.html')

@login_required
def ShowProblemStatement(request,year,month,day,slug,lk=0,dis=0,ps=0):
    problemStatement_List=get_object_or_404(ProblemStatement,slug=slug,publish__year=year,
    publish__month=month,publish__day=day,)
    total_view=problemStatement_List.TotalViewForProbelm
    if str(lk)=="0" and str(dis)=="0":
        total_view=problemStatement_List.TotalViewForProbelm+1
        problemStatement_List.TotalViewForProbelm=total_view

    if str(lk)=="0" and str(dis)=="0":
        if request.user in problemStatement_List.LikesForProbelm.all():
            lk="1"
        elif request.user in problemStatement_List.Dis_LikesForProbelm.all():
            dis="1"

    if request.user in problemStatement_List.LikesForProbelm.all() and str(dis)=="1":
        problemStatement_List.LikesForProbelm.remove(request.user)
        problemStatement_List.Dis_LikesForProbelm.add(request.user)
    elif str(lk)=="1":
        problemStatement_List.Dis_LikesForProbelm.add(request.user)

    if request.user in problemStatement_List.Dis_LikesForProbelm.all() and str(lk)=="1":
        problemStatement_List.Dis_LikesForProbelm.remove(request.user)
        problemStatement_List.LikesForProbelm.add(request.user)
    elif str(dis)=="1":
        problemStatement_List.Dis_LikesForProbelm.add(request.user)

    total_like=problemStatement_List.total_likes_for_Problems()
    total_dislike=problemStatement_List.total_dislikes_fro_Problems()
    lst=["0","1"]
    problemStatement_List.save()
    if request.user.is_authenticated:
        comments=problemStatement_List.ProblemComment.filter(active=True)
        #reply_lst= comment_lst.Reply.filter(active=True)
        csubmit=False

        if request.method=='POST':
            form=Comment_Related_To_ProblemForm(request.POST)
            if form.is_valid():
                new_comment=form.save(commit=False)
                new_comment.question=problemStatement_List
                new_comment.name= request.user.username
                new_comment.email= request.user.email
                new_comment.save()
                form=CommentForm()
                csubmit=True
        else:
            form=CommentForm()
        return render(request,'Blog/ProblemStatement.html',{'problemStatement_List':problemStatement_List,'form':form,'csubmit':csubmit,
        'comments':comments,'total_like':total_like,"total_dislike":total_dislike,
        'total_view':total_view,'dis':dis,'lk':lk,'lst':lst,})
    else:
        messages.success(request,'Login Required')
        return HttpResponseRedirect('/login/')
