from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _

from snippets.forms import SnippetForm, CommentForm
from snippets.models import Snippet, Comment


def top(request):
    snippets = Snippet.objects.all()
    context = {"snippets": snippets}
    return render(request, "snippets/top.html", context)


@login_required
def snippet_new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            messages.add_message(request, messages.SUCCESS,
                                 _("Success to create a new snippet."))
            return redirect(snippet_detail, snippet_id=snippet.pk)
        else:
            messages.add_message(request, messages.ERROR,
                                 _("Failed to create a new snippet."))
    else:
        form = SnippetForm()
    return render(request, "snippets/snippet_new.html", {'form': form})


@login_required
def snippet_edit(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    if snippet.created_by_id != request.user.id:
        return HttpResponseForbidden(_("You cannot to edit this snippet."))

    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 _("Success to update the snippet."))
            return redirect('snippet_detail', snippet_id=snippet_id)
        else:
            messages.add_message(request, messages.ERROR,
                                 _("Failed to update the snippet."))
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/snippet_edit.html', {'form': form})


@login_required
def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    comments = Comment.objects.filter(commented_to=snippet_id).all()
    comment_form = CommentForm()

    return render(request, "snippets/snippet_detail.html", {
        'snippet': snippet,
        'comments': comments,
        'comment_form': comment_form,
    })


@login_required
def comment_new(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.commented_to = snippet
        comment.commented_by = request.user
        comment.save()
        messages.add_message(request, messages.SUCCESS,
                             _("Success to post a comment."))
    else:
        messages.add_message(request, messages.ERROR,
                             _("Failed to post a comment."))
    return redirect('snippet_detail', snippet_id=snippet_id)

