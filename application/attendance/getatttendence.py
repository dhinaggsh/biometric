from ..user_management.connection import getconnection
from datetime import datetime
from ..models import attendece

conn=None
#All attendence
def getattendance():
    global conn
    try:
        conn = getconnection()
        print("connection Suceess")
        attendance = conn.get_attendance()

        data = []
        for att in attendance:
        
            data.append({
                "user_id": att.user_id,
                "timestamp": str(att.timestamp),
            })
            
            from django.utils import timezone
            aware_dt = timezone.make_aware(att.timestamp)
            
            # Save to MySQL
            attendece.objects.get_or_create(
                user_id=att.user_id,
                timestamp=aware_dt,
                status=att.status
            )
        return data
    except Exception as error:
        print(error)

    # finally:
    #     conn.disconnect()


#Selected user Attendence
def user_attendance(user_id):
    try:
        conn = getconnection()
        print("connection Suceess")
        attendance = conn.get_attendance()

        data = []
        for att in attendance:
            if user_id == att.user_id:
                data.append({
                    "user_id": att.user_id,
                    "timestamp": str(att.timestamp)
                })
        print("data :", data)
        return data
    
    finally:
        conn.disconnect()

        