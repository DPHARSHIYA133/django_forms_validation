from django import forms
from app.models import *

def check_for_h(value):
    if value[0]=='h' or value[0]=='H':
        raise forms.ValidationError('starting with h')
class TopicForm(forms.Form):
    topic_name=forms.CharField(validators=[check_for_h])
class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField() 
    reemail=forms.EmailField()
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reemail']
        if e!=re:
            raise forms.ValidationError('emails not matched!')

class AccessrecordForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    date=forms.DateField()
    author=forms.CharField()
