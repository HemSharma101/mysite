from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

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


#This view creates a new model form to add new post 
def post_new(request):
	''' view function to create a model form to add new blog post'''
	if request.method == "POST":

		form = PostForm(request.POST)
		if form.is_valid():
			
			# don't save the post yet withour author and publushed date field
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save() # save the form and new blog post is created
			return redirect('post_detail', pk=post.pk) 
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form })


#view function to edit a post
def post_edit(request, pk):
	''' this method opens a blog in the editor and lets edit and save it '''
	post = get_object_or_404(Post, pk=pk)

	if request.method == "POST":
		#save the edited form
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		# open the form in editor 
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form':form})