from zk import ZK

DEVICE_IP = '192.168.50.201'
DEVICE_PORT = 4370

# Device conection
def getconnection():
    zk = ZK(DEVICE_IP, port=DEVICE_PORT, timeout=5)
    conn = zk.connect()
    return conn
