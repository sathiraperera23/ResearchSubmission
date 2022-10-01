from django.shortcuts import redirect, render, get_object_or_404
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


def approval(request, id):
    files = get_object_or_404(FileData, id=id)
    files = FileData.objects.update(approval=1)
    # return render(request, 'filedownload.html', {'files': files})
    return redirect('downloadfile')


def delete(request, id):
    data = get_object_or_404(FileData, id=id)
    data.delete()
    return redirect('downloadfile')