from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
# function based view
# request: everything we receive from the user via the Internet
def post_list(request):
	# get posts from the model and ordr them according to published date
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


	# {}: a place in which we can add some things for the template to use
	# Here, we are passing QuerySet object , posts , 
	#which is a list of post model object

	return render(request, 'blog/post_list.html', {'posts': posts})


# view has given extra parameter, pk.
# The function has to catch it along with request 
# pk must have same name as defined in the urls 
def post_detail(request, pk):
	'''this function displays detailed post when clicked on the post list'''
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post })