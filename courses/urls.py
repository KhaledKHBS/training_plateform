from django.urls import path , include
from .views import CourseListView , upload_course_document
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from courses.api import CourseViewSet
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView)

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="api-courses")

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('about/', views.about, name='course_about'),
    path('catalog/', CourseListView.as_view(), name='course_catalog'),
    path('private-catalog/', views.PrivateCourseListView.as_view(), name='private_course_catalog'),
    path('restricted-catalog/', views.RestrictedCourseListView.as_view(), name='restricted_course_catalog'),
    path("create/", views.course_create,name="course_create"),
    path("create-class-based/", views.CourseCreateView.as_view(), name="course_create_cbv"),
    path("<int:pk>/edit/", views.CourseupdateView.as_view(), name="course_update_cbv"),
    path("<int:pk>/delete/", views.CourseDeleteView.as_view(), name="course_delete_cbv"),
    path("create-document/", views.upload_course_document, name="course_document_create_cbv"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("dashboard/",views.dashborad,name = "dashboard"),
    path("api/",include(router.urls)),
    path("api/schema/",SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/",SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
