from django import forms

from files.models import FileData


class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter first name", max_length=50)
    lastname = forms.CharField(label="Enter last name", max_length=10)
    email = forms.EmailField(label="Enter Email")
    file = forms.FileField()  # for creating file input


class FileForm(forms.ModelForm):
    # class Meta:
    #     model = FileData
    #     fields = ["firstname", "lastname", "email", "file"]
    # firstname = forms.CharField(label="Enter first name", max_length=50)
    # lastname = forms.CharField(label="Enter last name", max_length=10)
    # email = forms.EmailField(label="Enter Email")
    # file = forms.FileField()
    class Meta:
        model = FileData
        # fields = "__all__"
        fields = ['firstname', 'lastname', 'email', 'file']
