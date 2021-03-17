from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['author','title','topic','content']

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'content':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent form-control'})
        }

# class CommentForm(forms.ModelForm):
#
#     class Meta:
#         model = Comment
#         fields = ['text']
#
#         widgets = {
#             'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
#         }
