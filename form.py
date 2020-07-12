from django import forms

class newbookform(forms.Form):
    title=forms.CharField(label='title',max_length=100);
    price=forms.FloatField(label='price')
    author=forms.CharField(label='author')#length will be taken automatically
    publisher=forms.CharField(label='publisher')
    pdf=forms.FileField(
        label='pdf',
        help_text='max. 42 megabytes'
    )

class searchform(forms.Form):
    title=forms.CharField(label='title',max_length=100)


#by this form will be craeting automatically