#import http.server
#import ssl

# Define server address and port
#HOST = "127.0.0.1"
#PORT = 9090

# Set up HTTP server
#server_address = (HOST, PORT)
#httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Wrap with SSL
#httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="key.pem", certfile="cert.pem", server_side=True)

#print(f"Serving on https://{HOST}:{PORT}/")
#httpd.serve_forever()*/

#import http.server
#import ssl

#HOST = "127.0.0.1"
#PORT = 9090

# Set up HTTP server
#server_address = (HOST, PORT)
#httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Use SSLContext (recommended way)
#context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
#httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

#print(f"Serving on https://{HOST}:{PORT}/")
#httpd.serve_forever()


#import http.server
#import ssl
#import socket

#HOST = "127.0.0.1"
#PORT = 9000

#server_address = (HOST, PORT)

#class ReusableTCPServer(http.server.HTTPServer):
 #   def server_bind(self):
 #       self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 #       super().server_bind()

#httpd = ReusableTCPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Wrap the socket for HTTPS
#httpd.socket = ssl.wrap_socket(
 #   httpd.socket, keyfile="key.pem", certfile="cert.pem", server_side=True
#)

#print(f"Serving on https://{HOST}:{PORT}/")
#httpd.serve_forever()



import http.server
import ssl
import socket

HOST = "127.0.0.1"
PORT = 8090

class ReusableTCPServer(http.server.HTTPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        super().server_bind()

# Create SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

# Initialize server
server_address = (HOST, PORT)
httpd = ReusableTCPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Wrap socket with SSL context
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Serving on https://{HOST}:{PORT}/")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
    httpd.server_close()
