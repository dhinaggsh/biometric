from .connection import getconnection

def create_user_device(user_id, name):
    conn = getconnection()
    try:
        conn.set_user(
            uid=int(user_id),
            name=name,
            privilege=0,
            password='',
            group_id='',
            user_id=user_id
        )
        return True
    finally:
        conn.disconnect()