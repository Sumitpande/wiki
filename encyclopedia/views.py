from django.shortcuts import render,redirect
from django.http import HttpResponse
import markdown 
import random
from django.contrib import messages

from . import util
from encyclopedia.forms import EntryForm,SearchForm


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def Entry(request, title):
    
    content = util.get_entry(title)


    return render(request,  "encyclopedia/wiki.html", {
        "content": content,
        "title": title,  
        "entries": util.list_entries()
    })






def newPage(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)
        
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            # entries = [x.lower() for x in util.list_entries()]
            if title in util.list_entries():
                
                return render(request,  "encyclopedia/Error.html", {
                    
                })
                
            else:
                util.save_entry(title,content)  
                return redirect('Entry',title=title)

                

    form = EntryForm()


    return render(request,  "encyclopedia/newPage.html",{
        'form': form
         
    })


def editPage(request,title):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        

        
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            util.save_entry(title,content)
            return redirect('Entry',title=title)

           
            

        
    content = util.get_entry(title)
    form = EntryForm(initial={
        'title': title,
        'content':content
    })

    

    return render(request,  "encyclopedia/editPage.html",{
        'title': title,
        'content':content,
        'form': form
         
    })





def Random(request):
    entries =  util.list_entries()
    title= random.choice(entries) 
    content = util.get_entry(title)
    return render(request,  "encyclopedia/wiki.html",{
        "content": content,
        "title": title,
        "entries": util.list_entries()   
    })


def search(request):     
    entries =  util.list_entries()   
    if request.method == 'POST':      
        title =  request.POST.get('q')  
        if title in entries:
            return render(request,  "encyclopedia/wiki.html",{
                "content": util.get_entry(title),
                "title": title, 
                "entries": util.list_entries()  
        
            })
        else:
            res = list(filter(lambda x: title in x, entries))   
            return render(request,  "encyclopedia/index.html",{
                'entries':res
            })
            
        