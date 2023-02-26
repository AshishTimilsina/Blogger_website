from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from urllib3 import HTTPResponse
from . models import Post,Contact,BlogComment

# HTML PAGES
def index(request):
    # TO fetch data from database for index.html page
    myposts=Post.objects.all()
    return render(request,'blog/index.html',{'myposts':myposts})

def Blogpost(request,id):
    # To fetch data from database for blogpost.html
    post=Post.objects.filter(post_id=id)[0]
    comments=BlogComment.objects.filter(post=post)
    context={'post':post,'comments':comments,'user':request.user}
    
    return render(request,'blog/blogpost.html',context)

def about(request):
    return render(request,'blog/about.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        if len(name)<2 or len(email)<7 or len(phone)<13 or len(desc)<5:
            messages.error(request,"Please Fill The Form Correctly.")
        else:    
            contact=Contact(name=name,email=email,phone=phone,desc=desc)
            contact.save()
            messages.success(request,"Form has been submitted successfully.")
    return render(request,'blog/contact.html')


def search(request):
    query=request.GET.get('query','')
    if len(query)>70:
        allposts=Post.objects.none()
    else:
        allpostsTitle=Post.objects.filter(title__icontains=query)
        allpostshead0=Post.objects.filter(head0__icontains=query)
        allpostspara0=Post.objects.filter(para0__icontains=query)
        allpostshead1=Post.objects.filter(head1__icontains=query)
        allpostspara1=Post.objects.filter(para1__icontains=query)
        allpostshead3=Post.objects.filter(head3__icontains=query)
        allpostspara3=Post.objects.filter(para3__icontains=query)
        allpostshead4=Post.objects.filter(head4__icontains=query)
        allpostspara4=Post.objects.filter(para4__icontains=query)
        allposts=allpostsTitle.union(allpostshead0,allpostshead1,allpostshead3,allpostshead4,allpostspara0,allpostspara1,allpostspara3,allpostspara4)
    if allposts.count()==0:
        messages.warning(request,"No Search Result Found")
    params={'allposts':allposts,'query':query}
    return render(request,'blog/search.html',params)

# AUTHENTICATION API'S
def handlesignup(request):
    # creating user 
    if request.method=="POST":
        email=request.POST.get('email','')
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        passwrd=request.POST.get('passwrd','')
        passwrd2=request.POST.get('passwrd2','')
        username=request.POST.get('username','')
        
        # checking for error in input
        if(passwrd != passwrd2):
            messages.error(request,"Please enter correct password.")
            return redirect('/')
        # create the user
        try:
            myuser=User.objects.create_user(username,email,passwrd2)            
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            messages.success(request, "Your Id has been created successfully.")
            return redirect('/')
        except:
            return HttpResponse("Error while Submitting information..Please Try Again!")
    else:
        return HttpResponse("404 error Not Found!")
    

def handleLogin(request):
    if request.method=="POST":
        loginemail=request.POST.get('loginemail','')
        loginpass=request.POST.get('loginpass','')
        
        user=authenticate(email=loginemail,passwrd2=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request,"Invalid Username or Password.")
            return redirect("/")
    return HttpResponse("404 error not found!")



def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

def postcomment(request):
    if request.method =="POST":
        comment=request.POST.get('comment','')
        user=request.user
        postsno=request.POST.get('postsno','')
        post=Post.objects.get(sno=postsno)
        comment=BlogComment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request,'Your Comment has been posted Successfully')
    
    return redirect('/blog/blogpost/{{post_id}}')
            
           
        
    

