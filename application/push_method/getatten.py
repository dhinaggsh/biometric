from datetime import datetime
import xml.etree.ElementTree as ET
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import attendece
from django.utils import timezone


# Short Version
# Checks server connection
@csrf_exempt
def getrequest(request):
    try:     
        return HttpResponse("Ok")
    except Exception as e:
        print("get_request error:",e)
        raise

# sends data
@csrf_exempt
def cdata(request):
    if request.method == "POST":
        body = request.body.decode('utf-8').strip()
        print(body)
        if body:
            lines = body.splitlines()
            for line in lines:
                parts = line.split()
                if len(parts) >= 3:
                    user_id = parts[0]
                    timestamp = parts[1] + " " + parts[2]
                    status = parts[3] if len(parts) > 3 else "0"
                    # status_text = "Check-in" if status == "0" else "Check-out"
                    # print(f"UserID: {user_id}, Time: {timestamp}, Status: {status_text}, done")
                    process_data(user_id, timestamp, status)
                                
    return HttpResponse("OK")


@csrf_exempt
def process_data(user_id, timestamp, status):
        status_text = "Check-in" if status == "0" else "Check-out"
        print(f"UserID: {user_id}, Time: {timestamp}, Status: {status_text}")
                            


@csrf_exempt
def biometric_push(request):
    if request.method == "POST" or request.method == "GET":
        data = request.POST if request.method == "POST" else request.GET

        user_id = data.get("PIN")
        timestamp = data.get("CheckTime")
        status = data.get("Status")

        print(f"Saved: {user_id} {timestamp} {status}")

        return JsonResponse({"success": True})

    return JsonResponse({"error": "Invalid request"})


# https://wei-noctambulous-concurringly.ngrok-free.dev