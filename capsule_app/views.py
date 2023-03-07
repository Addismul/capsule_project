from django.shortcuts import render
from capsule_app.models import Capsule
import requests

# Create your views here.

def get_capsules(request):
    all_capsules = {}
    url = 'https://api.spacexdata.com/v5/launches'
    response = requests.get(url)
    data = response.json()
#    capsules =data['capsules']
    
    for i in data:
        capsule_data =Capsule(
            slug=i['id'],
            name = i['name'],
            details = i['details'],
            static_fire_date_utc=i['static_fire_date_utc'],
            static_fire_date_unix=i['static_fire_date_unix'],
            date_precision=i['date_precision'],
            launch_library_id=i['launch_library_id'],
            tbd=i['tbd'],
            auto_update=i['auto_update']
        )
        
        capsule_data.save()
        all_capsules =Capsule.objects.all()
        
    return render(request, 'capsule.html',{"all_capsules":all_capsules})       

def capsule_detail(request,id):
    capsule = Capsule.objects.get(id=id)
    print(capsule)
    return render (
        request,
        'capsule_detail.html',
        {'capsule':capsule}
    )