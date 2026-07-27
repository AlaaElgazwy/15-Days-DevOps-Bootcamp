from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.shortcuts import get_object_or_404
from .services.ai_service import extract_action_items as ai_extract_action_items


def home(request):

    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)

            # مؤقتًا لا يوجد تسجيل دخول
            note.user_id = 1

            note.save()

            return redirect("home")

    else:
        form = NoteForm()

    notes = Note.objects.all().order_by("-created_at")

    context = {
        "form": form,
        "notes": notes,
    }

    return render(request, "notes/index.html", context)

def delete_note(request, id):
    note = get_object_or_404(Note, id=id)

    note.delete()

    return redirect("home")

def edit_note(request, id):
    note = get_object_or_404(Note, id=id)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = NoteForm(instance=note)

    context = {
        "form": form,
        "notes": Note.objects.all().order_by("-created_at"),
        "editing": True,
        "note_id": note.id,
    }

    return render(request, "notes/index.html", context)

def extract_action_items(request, id):

    print("Extract button clicked!")
    note = get_object_or_404(Note, id=id)

    try:
        action_items = ai_extract_action_items(note.content)

        note.action_items = action_items
        note.save()

    except Exception as e:
        note.action_items = f"AI Error:\n{str(e)}"
        note.save()

    return redirect("home")