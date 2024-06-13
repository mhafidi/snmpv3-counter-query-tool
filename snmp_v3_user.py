from pysnmp.hlapi import *

class SNMPv3User:
    def __init__(self, username: str, auth_key: str, priv_key: str, auth_protocol: str, priv_protocol: str):
        self.username = username
        self.auth_key = auth_key
        self.priv_key = priv_key
        self.auth_protocol = auth_protocol
        self.priv_protocol = priv_protocol

    def get_user_data(self):
        auth_protocols = {
            'SHA': usmHMACSHAAuthProtocol,
            'MD5': usmHMACMD5AuthProtocol
        }
        priv_protocols = {
            'AES': usmAesCfb128Protocol,
            'DES': usmDESPrivProtocol
        }
        return UsmUserData(
            userName=self.username,
            authKey=self.auth_key,
            privKey=self.priv_key,
            authProtocol=auth_protocols[self.auth_protocol],
            privProtocol=priv_protocols[self.priv_protocol]
        )
