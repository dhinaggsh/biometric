import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .user_management.connection import getconnection
from zk import ZK
from .user_management.get import getemployees
from .user_management.create import create_user_device
from .user_management.delete import delete_user_device
from .user_management.update import update_user_device

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .attendance.getatttendence import *
# from .push_method.getatten import *


@csrf_exempt
def get_users(request):
    if request.method == "GET":
        try:
            data = getemployees()
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Only GET allowed"})


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            user_id = body.get('user_id')
            name = body.get('name')

            create_user_device(user_id, name)
            return JsonResponse({"msg": "User created"})
        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Only POST allowed"})


@csrf_exempt
def delete_user(request):
    if request.method == "DELETE":
        try:
            body = json.loads(request.body)
            user_id = body.get('user_id')

            delete_user_device(user_id)
            return JsonResponse({"msg": "User deleted"})
        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Only DELETE allowed"})


@csrf_exempt
def update_user(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            user_id = body.get('user_id')
            name = body.get('name')
            password = body.get('password') or ""

            update_user_device(user_id, name, password)
            return JsonResponse({"msg": "User updated"})
        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Only PUT allowed"})
    
    
# User Attendence
@csrf_exempt
def get_attendance(request):
    if request.method == 'GET':
        try:
            data1 = getattendance()
            return JsonResponse(data1, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Only GET allowed"})

@csrf_exempt
def selected_user_attendance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get("user_id")
            data1 = user_attendance(user_id=user_id)
            return JsonResponse(data1, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Only GET allowed"})


# Short Version
# Checks server connection
# @csrf_exempt
# def getrequest(request):
#     return HttpResponse("Ok")


# # sends data
# @csrf_exempt
# def cdata(request):
#     if request.method == "POST":
#         body = request.body.decode('utf-8').strip()
        
#         if body:
#             lines = body.splitlines()
#             for line in lines:
#                 parts = line.split()
#                 if len(parts) >= 3:
#                     user_id = parts[0]
#                     timestamp = parts[1] + " " + parts[2]
#                     status = parts[3] if len(parts) > 3 else "0"
                    
#                     process_data(user_id, timestamp, status)
                    
#     return HttpResponse("OK")


# @csrf_exempt
# def process_data(user_id, timestamp, status):
#         status_text = "Check-in" if status == "0" else "Check-out"
#         print(f"UserID: {user_id}, Time: {timestamp}, Status: {status_text}")

# @csrf_exempt
# def biometric_push(request):
#     data = request.POST or request.GET
#     user_id = data.get("PIN")       
#     timestamp = data.get("CheckTime")
#     status = data.get("Status")     

#     print(f"UserID: {user_id}, Time: {timestamp}, Status: {status}")

#     return JsonResponse({"success": True})




from datetime import datetime

def push_attendance(request):
    """
    Endpoint for device to push attendance logs
    """
    if request.method == 'POST':
        try:
            
            data = json.loads(request.body)

            user_id = data.get('user_id')
            name = data.get('name', '')
            timestamp_str = data.get('timestamp')
            status = data.get('status', 'IN')

            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')

            log = attendece.objects.create(
                user_id=user_id,
                name=name,
                timestamp=timestamp,
                status=status
            )

            # Example output
            response = {
                "success": True,
                "data": {
                    "id": log.id,
                    "user_id": log.user_id,
                    "name": log.name,
                    "timestamp": str(log.timestamp),
                    "status": log.status
                }
            }
            return JsonResponse(response)

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Only POST allowed"})
