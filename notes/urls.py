from django.urls import path
from .views import NotesListView,update_Notes,delete_notes,CreateNewNote,SearchResultView,NoteDetials

urlpatterns=[
    path('',NotesListView.as_view(),name="notes"),
    path('update/<int:id>',update_Notes,name='update'),
    path('delete/<int:id>',delete_notes,name='delete'),
    path('new/',CreateNewNote.as_view(),name='addnew'),
    path('search/',SearchResultView.as_view(),name='search_result'),
    path('note/<int:pk>/',NoteDetials.as_view(),name='note_details'),
]