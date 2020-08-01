from django import forms



class EntryForm(forms.Form):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(
                            attrs={'class': 'form-control','id':'exampleFormControlInput1','name':'title'}),
                            )
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control','id':'exampleFormControlTextarea1','name':'content'}
    ))


    
class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100,
                                   widget= forms.TextInput(
                                    attrs={'class':'search','name':'q'}
                                    ))




