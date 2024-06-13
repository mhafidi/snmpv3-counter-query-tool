from pysnmp.hlapi import *
from snmp_v3_user import SNMPv3User
from snmp_transport import SNMPTransport

class SNMPQuery:
    def __init__(self, user_data: SNMPv3User, transport_target: SNMPTransport):
        self.snmp_engine = SnmpEngine()
        self.user_data = user_data
        self.transport_target = transport_target
        self.context_data = ContextData()

    def get(self, oid: str):
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(
                self.snmp_engine,
                self.user_data.get_user_data(),
                self.transport_target.get_transport_target(),
                self.context_data,
                ObjectType(ObjectIdentity(oid))
            )
        )
        if errorIndication:
            return f"Error: {errorIndication}"
        elif errorStatus:
            return f"Error Status: {errorStatus.prettyPrint()} at {errorIndex and varBinds[int(errorIndex) - 1] or '?'}"
        else:
            return '\n'.join([' = '.join([x.prettyPrint() for x in varBind]) for varBind in varBinds])
