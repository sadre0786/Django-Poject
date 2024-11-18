from django.shortcuts import render,get_object_or_404,redirect
from .models import Tweet
from .froms import TweetForms,UserRegistraionForms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def home(request):
    return render(request,'index.html')


def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html',{'tweets':tweets})


@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForms(request.POST,request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')        
    else:
        form = TweetForms()
    
    return render(request,'tweet_create.html',{'form':form})


@login_required
def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Tweet,id = tweet_id, user = request.user)
    if request.method == 'POST':
        form = TweetForms(request.POST,request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForms(instance=tweet)
    
    return render(request,'tweet_create.html',{'form':form})


@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet,id = tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})


def register(request):
    if request.method == "POST":
        form = UserRegistraionForms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form = UserRegistraionForms()

    return render(request,'registration/registration.html',{'form':form})



def search(request):
    query = request.GET.get('query', '')  # Use get() to avoid KeyError
    tweets = Tweet.objects.filter(text__icontains=query)
    return render(request, 'search.html', {'tweets':tweets})





