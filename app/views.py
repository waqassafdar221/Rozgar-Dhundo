from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader

from app.models import JobPost

# Create your views here.


job_title = [
    "First Job",
    "Second Job"
]
job_description=[
    "First Job description",
    "Second Job Description"
]
# def hello(request):
#     return HttpResponse('Hello WOrld')

class TempClass:
    x=100

def hello(request):
    # template = loader.get_template('app\hello.html')
    list = [
        "Alpha",
        "Beta"
    ]
    temp = TempClass()
    is_authenticated = False
    

    context = {"age":17,"name":"Waqas", "first_list":list,"temp_object":temp,"is_authenticated" :is_authenticated}
    # return HttpResponse(template.render(context, request))
    return render(request,'app/hello.html', context)

def job_list(request):
    # list_of_job = '<ul>'
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail_url=reverse('jobs_detail',args=(job_id,))
    #     list_of_job += f"<li><a href='{detail_url}'>{j}</a></li>"
    # list_of_job += "</ul>"
    # return HttpResponse(list_of_job)
    jobs = JobPost.objects.all()

    context={"jobs":jobs}
    return render(request,'app/index.html',context)

def job_detail(request,id):

    # print(type(id))
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # # return HttpResponse(f'Job Detail Page {id}')
        # return HttpResponse(return_html)
        # context ={"job_title":job_title[id],"job_description": job_description[id]}
        job = JobPost.objects.get(id=id)
        context ={"job":job,}
        return render(request,"app/job_detail.html",context)
    except:
        return HttpResponseNotFound('No Job Found')