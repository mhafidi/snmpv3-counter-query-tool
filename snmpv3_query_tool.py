import argparse
from snmp_v3_user import SNMPv3User
from snmp_transport import SNMPTransport
from snmp_query import SNMPQuery

class SNMPv3QueryTool:
    def __init__(self):
        self.args = self.parse_args()

    def parse_args(self):
        parser = argparse.ArgumentParser(description="SNMPv3 GET Script")
        parser.add_argument('--username', required=True, help='SNMPv3 username')
        parser.add_argument('--authkey', required=True, help='SNMPv3 authentication key')
        parser.add_argument('--privkey', required=True, help='SNMPv3 privacy key')
        parser.add_argument('--authprotocol', required=True, choices=['SHA', 'MD5'], help='SNMPv3 authentication protocol (SHA or MD5)')
        parser.add_argument('--privprotocol', required=True, choices=['AES', 'DES'], help='SNMPv3 privacy protocol (AES or DES)')
        parser.add_argument('--ip', required=True, help='SNMP agent IP address')
        parser.add_argument('--port', type=int, default=161, help='SNMP agent port (default: 161)')
        parser.add_argument('--oid', required=True, help='OID to query (e.g., 1.3.6.1.2.1.1.1.0)')
        return parser.parse_args()

    def run(self):
        user = SNMPv3User(
            username=self.args.username,
            auth_key=self.args.authkey,
            priv_key=self.args.privkey,
            auth_protocol=self.args.authprotocol,
            priv_protocol=self.args.privprotocol
        )
        transport = SNMPTransport(ip=self.args.ip, port=self.args.port)
        query = SNMPQuery(user, transport)
        result = query.get(self.args.oid)
        print(result)
