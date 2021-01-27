import socket
import ast 

class Reader:
    def __init__(self):
        self.sock = None
        self._createConnection()

    def _createConnection(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        local_hostname = socket.gethostname()
        local_fqdn = socket.getfqdn()
        ip_address = socket.gethostbyname(local_hostname)
        print ("working on %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))
        server_address = (ip_address, 23456)
        print ('starting up on %s port %s' % server_address)
        self.sock.bind(server_address)
        self.sock.listen(1)

    def read_ipc(self):
        while True:
            print ("""\n
            ######################################
            #                                    #
            #      waiting for a connection      #
            #                                    #
            ######################################
            """)
            connection, _ = self.sock.accept()
            try:
                out = []
                while True:
                    data = connection.recv(64)
                    out.append(data.decode("ascii"))
                    if data:
                        pass
                    else:
                        json_values = ast.literal_eval("".join(out))
                        return json_values
            finally:
                connection.close()

reader = Reader()
while True:
    print(reader.read_ipc())