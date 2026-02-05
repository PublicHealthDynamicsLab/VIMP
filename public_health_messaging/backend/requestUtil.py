import simplejson

def parse_request(request):
        # Parse the HTTP request
        request_lines = request.split("\r\n")
        request_line = request_lines[0]
        (request_method, path, request_version) = request_line.split(" ")
        return (request_method, path, request_version, request_lines[1:])
    

def parse_POST_body(request):
    print(request)
    return simplejson.loads("\r\n\r\n".join(request.split("\r\n\r\n")[1:]))

def build_response(status_code, body, content_type='text/html'):
    # Build the HTTP response
    status_line = f"HTTP/1.1 {status_code}\r\n"
    headers = f"Content-Type: {content_type}\r\nContent-Length: {len(body)}\r\n"
    response = f"{status_line}{headers}\r\n{body}"
    return response.encode()