import os
import socket
import requestUtil
import json
from LoadData import LoadData
from LlmBackbone import LlmBackbone

HOST = ""
PORT = 8000

data = LoadData()
dropdown_prep = data.get_demographics()
out_data = sorted(list(data.get_demographics()))
out_data = {demo:list(data.get_dropdowns(demo)) for demo in out_data}
out_data = {demo:out_data[demo] for demo in out_data if len(out_data[demo]) > 1}

backbone = LlmBackbone(data)

class ServerCore:
    
    def __init__(self):
                
        # Create a TCP/IP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the address and port
        server_socket.bind((HOST, PORT))
    
        # Listen for incoming connections
        server_socket.listen()

        print(f"Listening on {HOST}:{PORT}...")

        while True:
            # Wait for a connection
            client_socket, client_address = server_socket.accept()

            # Receive data from the client
            request = client_socket.recv(1024).decode()

            # Handle the request
            response = self.handle_request(request, client_socket)

            # Send the response to the client
            if response is not None:
                client_socket.sendall(response)

            # Close the client socket

    

    def handle_get(self,request):
        print("Get!")
        fpath = "public_health_messaging/frontend/server_front.html"
        try:
            (request_method, path, request_version, headers) = requestUtil.parse_request(request)
        except:
            f = open(fpath,"r")
            body = f.read()
            f.close()
            response = requestUtil.build_response(200, body)
            return response       
        if path != "/" and os.path.exists(os.path.join("public_health_messaging/frontend",path[1:])):
            fpath = os.path.join("public_health_messaging/frontend",path[1:])
            
        f = open(fpath,"r")
        body = f.read()
        f.close()
        response = requestUtil.build_response(200, body)
        return response

    def handle_post(self, request, client_socket):
        request_body = requestUtil.parse_POST_body(request)
        
        if request_body["title"] == "dropdowns":
            
            out_json = {"Contents":out_data}
            
            body = json.dumps(out_json)
        
            response = requestUtil.build_response(200, body, content_type = "application/json")
            return response
        elif request_body["title"] == "prompt":
            resp=backbone.run(str(request_body["text"]),None)
            print(resp)
            out_json = {"content":resp}
            
            body = json.dumps(out_json)
        
            response = requestUtil.build_response(200, body, content_type = "application/json")
            return response
            
    def handle_request(self, request, client_socket):
        # Parse the request
        
        (request_method, path, request_version, headers) = requestUtil.parse_request(request)
        # Check the request method
        if request_method == "GET":
            response = self.handle_get(request)
        elif request_method == "POST":
            response = self.handle_post(request, client_socket)
        else:
            # If the request is not a GET request, return a 405 Method Not Allowed error
            #print(headers)
            body = "<html><body><h1>Method Not Allowed</h1></body></html>"
            response = requestUtil.build_response(405, body)

        if response is not None:
            client_socket.sendall(response)
        client_socket.close()

ServerCore()

