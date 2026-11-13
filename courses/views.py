from django.shortcuts import render , redirect
from .models import Course
from django.views.generic import DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import CourseForm , CourseDocumentForm
from django.views.generic import CreateView , UpdateView
from django.contrib.auth.decorators import login_required , permission_required
from django.urls import reverse_lazy   

class CourseDeleteView(PermissionRequiredMixin, DeleteView):
    model = Course
    template_name = "courses/course_confirm_delete.html"
    permission_required = "courses.delete_course"
    login_url = "/admin/login/"
    success_url = reverse_lazy("course_list")


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"
    success_url = reverse_lazy("course_list")
    permission_required = "courses.add_course"
    login_url = "/admin/login/"  # provisoire

class CourseupdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"
    success_url = reverse_lazy("course_list")
    permission_required = "courses.change_course"
    login_url = "/admin/login/"  # provisoire

def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm()
    return render(request, "courses/course_form.html",
                  {"form": form})


class CourseListView(ListView):
    model = Course
    template_name = "courses/catalog.html"
    context_object_name = "courses"
    paginate_by = 3

    def get_queryset(self):
        return Course.objects.select_related(
            "instructor"
        ).order_by("title")
    
class PrivateCourseListView(
    LoginRequiredMixin, CourseListView
):
    login_url = "/admin/login/"  # provisoire

class RestrictedCourseListView(
    PermissionRequiredMixin, CourseListView
):
    permission_required = "courses.vie  w_course"
    login_url = "/admin/login/"  # provisoire



def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/list.html", {
        "page_title": "Nos formations",
        "courses": courses
    })


def about(request):
    context = {
        'page_title': 'À propos de nous',
        'trainer': 'Ahmed',
        'description': 'Nous proposons des formations de qualité en développement web.',
    }
    return render(request, 'courses/about.html', context)

def upload_course_document(request):
    if request.method == "POST":
        form = CourseDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseDocumentForm()
    return render(request, "courses/upload_document.html", {"form": form})

@login_required
def dashborad(request):
    return render(request , "courses/dashboard.html")