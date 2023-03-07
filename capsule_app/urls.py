from django.urls import path
from capsule_app import views

urlpatterns = [
    path('', views.get_capsules,name="get_Capsules"),
    path('<int:id>/',views.capsule_detail,name ="capsule_Detail")
]
