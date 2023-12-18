# file_share/views.py
from django.shortcuts import render, redirect
from .models import UserProfile, File
from .forms import UserProfileForm, FileForm
from .forms import UserProfileForm, FileForm, ShareFileForm
from django.http import FileResponse
from django.db.models import ObjectDoesNotExist
from django.http import Http404
from django.contrib import messages


def register_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['ID']
            username = form.cleaned_data['username']
            user_profile, created = UserProfile.objects.get_or_create(token=token)
            return redirect('file_share:share_file', user_id=user_profile.id)
    else:
        form = UserProfileForm()

    return render(request, 'register_user.html', {'form': form})

def share_file(request, user_id):
    try:
        user_profile = UserProfile.objects.get(id=user_id)
    except ObjectDoesNotExist:
        raise Http404("No registered user found with the provided ID.")

    if request.method == 'POST':
        form = ShareFileForm(request.POST, request.FILES)
        if form.is_valid():
            token_to_share_with = form.cleaned_data['user_to_share_with']
            file = form.cleaned_data['file']

            try:
                user_to_share_with = UserProfile.objects.get(token=token_to_share_with)
            except UserProfile.DoesNotExist:
                messages.error(request, "No registered user found with the provided token.")
                return redirect('file_share:share_file', user_id=user_id)

            shared_file = File.objects.create(owner=user_to_share_with, file=file)
            user_profile.shared_files.add(user_to_share_with)
            user_to_share_with.shared_files.add(user_profile)

            messages.success(request, "File shared successfully!")
            return redirect('file_share:share_file', user_id=user_id)
    else:
        form = ShareFileForm()

    files = File.objects.filter(owner=user_profile)
    return render(request, 'share_file.html', {'form': form, 'files': files})
def download_shared_file(request, file_id):
    shared_file = File.objects.get(id=file_id)
    file_path = shared_file.file.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True)
from django.shortcuts import render
def home(request):
    return render(request, 'file_share/register_user.html')
