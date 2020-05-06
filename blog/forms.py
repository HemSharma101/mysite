# form for Post model
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
	''' ModelForm for the Post model'''
	class Meta:
		'''this class defines fields of the model form '''

		model = Post
		fields = ('title', 'text',)


