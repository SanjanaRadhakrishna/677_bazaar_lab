from xmlrpc.server import SimpleXMLRPCServer

from rpc.ops import Ops



if __name__ == "__main__":
    ops = Ops()
    print("Starting rpc server...")

    server = SimpleXMLRPCServer(("localhost", 9000), logRequests=True)
    server.register_instance(ops)

    print("Rpc server started!")
    server.serve_forever()
    # from socket import socket
    #
    # with socket() as s:
    #     s.bind(('', 0))
    #     print(s.getsockname()[1])