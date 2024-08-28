from django.shortcuts import render

from uploadapp.forms import UploadForm

# Create your views here.
def upload_image(request):
    if request.method =='POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
    else:
        form = UploadForm()
    return render(request,'uploadapp/add_image.html',{'form':form})