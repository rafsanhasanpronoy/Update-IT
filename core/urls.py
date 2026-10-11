from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/signup/", views.signup, name="signup"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html", redirect_authenticated_user=True), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("about/", views.about, name="about"),
    path("admission/", views.admission, name="admission"),
    path("apply/", views.apply, name="apply"),
    path("apply/submitted/", views.apply_done, name="apply_done"),
    path("notices/", views.notices_list, name="notices"),
    path("gallery/", views.gallery_list, name="gallery"),
    path("achievements/", views.achievements_list, name="achievements"),
    path("faculty/", views.faculty_list, name="faculty"),
    path("classes/", views.classes_list, name="classes"),
    path("results/", views.student_results, name="results"),
    path("contact/", views.contact, name="contact"),
]