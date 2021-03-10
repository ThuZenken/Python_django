from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question>/results/',views.results, name="results"),
    path('<int:request>/vote/', views.vote, name = ""),
]