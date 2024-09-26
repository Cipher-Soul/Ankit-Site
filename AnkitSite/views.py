from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from .models import Project,Category

# Home page
def index(request):
    projects = Project.objects.all()[:2]
    data={
        'projects':projects,
        # 'filters':category,
    }
    return render(request,'main/index.html',data)

# Projects page
def project(request):
    projects = Project.objects.all().order_by('created_at')
    category = Category.objects.all()
    data={
        'projects':projects,
        'filters':category,
    }
    print(data)
    return render(request,'main/Project.html',data)

# blog page
def blogs(request):
    return render(request,'main/blog.html')

# Click counter
def project_click(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.click_count += 1
    project.save()
    # Redirect to the project link
    return redirect(project.project_link)