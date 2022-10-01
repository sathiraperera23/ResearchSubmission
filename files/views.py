from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from files.forms import FileForm
from files.models import FileData

# Create your views here.


def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')


def fileupload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('uploadfile')

    else:
        form = FileForm()
    context = {'form': form}
    return render(request, 'fileupload.html', context)


def filedownload(request):
    file = FileData.objects.all()  # Collect all records from table
    return render(request, 'filedownload.html', {'file': file})
