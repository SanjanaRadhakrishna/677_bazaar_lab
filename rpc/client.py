import xmlrpc.client



if __name__ == "__main__":
    proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")
    res = proxy.func1("Hello world")
    print(f"Result obtained from server is {res}")

    # RPC -> remote procedure call

    # HTTP -> resource based -> path, action, body