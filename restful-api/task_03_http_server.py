import http.server
import socketserver
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Sadə HTTP sorğularını idarə edən sinif.
    """

    def do_GET(self):
        """
        GET sorğularını endpointlərə görə yönləndirir.
        """
        if self.path == '/':
            # Əsas səhifə (Root)
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            # JSON məlumatı qaytaran endpoint
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            # Status yoxlanışı
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            # Əlavə məlumat endpointi
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            # Tapılmayan endpointlər üçün 404 xətası
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

# Serverin işə salınması
if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Server {PORT} portunda işləyir...")
        httpd.serve_forever()
