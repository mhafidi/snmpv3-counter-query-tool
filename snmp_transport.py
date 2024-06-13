from pysnmp.hlapi import *

class SNMPTransport:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port

    def get_transport_target(self):
        return UdpTransportTarget((self.ip, self.port))
