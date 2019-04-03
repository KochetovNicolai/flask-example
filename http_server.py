import http.server
import socketserver

PORT = 8000

# See: https://docs.python.org/3/library/http.server.html


def run(Handler):
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(http.server.SimpleHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return


if __name__ == '__main__':
    # Handler = http.server.SimpleHTTPRequestHandler
    Handler = testHTTPServer_RequestHandler
    run(Handler)
