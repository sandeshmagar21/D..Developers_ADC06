from django.shortcuts import render
from .models import memberShipPlan
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def get_gymClassDetail(request):
    if request.method == "GET":
        obj=memberShipPlan.objects.all()
        obj2=list(obj.values("trainerName","classesName","price","time"))
        obj3_dic={"PremiumMemberClassDetail":obj2}
        return JsonResponse(obj3_dic)

    elif request.method == "POST":
        print(request.body)
        obj4=json.loads(request.body)
        memberShipPlan.objects.create(trainerName=obj4['TrainerName'],
        classesName=obj4['ClassesNames'],
        price=obj4['Price'],
        time=obj4['Duration'])
        return JsonResponse({"MESSAGE":"Great, You data is successfully inserted in the database"})

@csrf_exempt
def Up_Del_viw_by_ID(request,Id):
        obj5=memberShipPlan.objects.get(id=Id)
        if request.method == "GET":
            return JsonResponse({
            "trainerName":obj5.trainerName,
            "classesName":obj5.classesName,
            "price":obj5.price,
            "time":obj5.time})
        
        elif request.method == "DELETE":      
            obj5.delete()
            return JsonResponse({"MESSAGE":"Your request by ID is successfully Deleted"})             
        
        elif request.method == "PUT":
            update=json.loads(request.body) 
        obj5.trainerName=update['TrainerName']
        obj5.classesName=update['ClassesNames'] 
        obj5.price=update['Price']
        obj5.time=update['Duration']
        obj5.save()
        return JsonResponse({"MESSAGE":"Your request by ID is successfully Updated"})







