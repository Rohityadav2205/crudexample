from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create/",views.create),
    path('emp/', views.emp),
    path('show/', views.show),
    path('edit/<int:id>', views.edit),
    path('update/', views.update),
    path('delete/<int:id>', views.destroy),

]
