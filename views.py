from django.http import JsonResponse
from django.core import serializers
from fsftn.models import Event,User
import json

def event(request,event_id=None):
    if request.method == "POST":
        data = json.loads(request.body)
        data_list = ["Workshop","Seminar","Hands-on","Lecture"]
        event_type = data["event"]
        flag = 0
        for i in data_list:
            if i == event_type:
                flag = 1
        if flag == 1:    
            event = Event.objects.create(name=data["name"],college=data["college"],email=data["email"],phone=data["phone"],date=data["date"],lat=data["lat"],lon=data["lon"],event=data["event"],duration=data["duration"])   
            event.save()
            return JsonResponse({"success":True},status=200)
        else:
            return JsonResponse({"success":False},status=404)
            
    elif request.method == "GET":
        id = event_id
        if id == None:
            events = serializers.serialize("json",Event.objects.all())
            return JsonResponse({"events":events},status=200)
        else :
            events = serializers.serialize("json",[Event.objects.get(id=id)])
            return JsonResponse({"events": events},status=201)
    elif request.method == "PUT":
        id = event_id
        data = json.loads(request.body)
        event = Event.objects.get(id=id)
        event.name = data["name"]
        event.college=data["college"]
        event.email=data["email"]
        event.phone=data["phone"]
        event.date=data["date"]
        event.lat=data["lat"]
        event.lon=data["lon"]
        event.event=data["event"]
        event.duration=data["duration"]
        event.save()
        return JsonResponse({"success":True},status=200)
    elif request.method == "DELETE":
        id = event_id
        event = Event.objects.get(id=id)
        event.delete()
        return JsonResponse({"success":True},status=204)
        
        
def createuser(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.create(username=data["username"],password=data["password"])
        user.save()
        return JsonResponse({"success":True},status=200)
    
