from django import forms

from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'



class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
       # fields='__all_'
        #fields=['topic_name','name','url']
        #exclude=['url']
        #widgets={'topic_name':forms.RadioSelect}
        labels={'name':'N'}
