from .connection import getconnection


conn=None
def getemployees():
    global conn
    try:
        conn = getconnection()
        users = conn.get_users()

        data = []
        for user in users:
            data.append({
                "user_id": user.user_id,
                "name": user.name,
                "card": user.card,
                "password": user.password
            })
        return data
    finally:
        conn.disconnect()
        
