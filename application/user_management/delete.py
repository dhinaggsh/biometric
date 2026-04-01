from .connection import getconnection

def delete_user_device(user_id):
    conn = getconnection()
    try:
        conn.delete_user(user_id=user_id)
        return True
    finally:
        conn.disconnect()