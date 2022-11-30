from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Notes
from .forms import Notesfrom

# Create your views here.
class NotesListView(ListView):
    model=Notes
    template_name='notes.html'
    
def update_Notes(request,id):
    note_id=Notes.objects.get(id=id)
    if request.method == 'POST':
        note_save=Notesfrom(request.POST,request.FILES,instance=note_id)
        if note_save.is_valid():
            note_save.save()
            return redirect('/notes')
    else:
        note_save=Notesfrom(instance=note_id)
    context={
        'form':note_save,
    }
    return render(request,'update.html',context)
        
def delete_notes(request,id):
    note_delete=Notes.objects.get(id=id)
    if request.method == 'POST':
        note_delete.delete()
        return redirect('/notes')
    return render(request,'delete.html')

class CreateNewNote(CreateView):
    model=Notes
    template_name="addnewnote.html"
    fields={
        'title',
        'notes',   
    }
    success_url=reverse_lazy("notes")
    
    
class SearchResultView(ListView):
    model=Notes
    context_object_name="notes"
    template_name="searchresult.html"
    
    def get_queryset(self):
        query=self.request.GET.get("q")
        return Notes.objects.filter(Q(title__icontains=query)|Q(notes__icontains=query))

class NoteDetials(DetailView):
    model=Notes
    context_object_name="note"
    template_name="detials.html"