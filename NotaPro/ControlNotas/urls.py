from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("classes", views.classes, name="classes"),
    path("partial", views.partial, name="partial"),
    path("create_evaluation", views.create_evaluation, name="create_evaluation"),
    path("all_evaluation", views.all_evaluation, name="all_evaluation"),
    path("evaluation_detail", views.evaluation_detail, name="evaluation_detail"),
    path("create_semester", views.create_semester, name="create_semester"),
    path("create_classes", views.create_classes, name="create_classes"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)  