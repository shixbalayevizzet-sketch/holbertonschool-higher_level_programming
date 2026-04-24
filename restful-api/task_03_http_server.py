import http.server
import socketserver
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    http.server.BaseHTTPRequestHandler sinfini miras alaraq 
    sadə bir API idarəedicisi yaradırıq.
    """

    def do_GET(self):
        """
        GET sorğularını idarə edir və uyğun endpointlərə yönləndirir.
        """
        if self.path == '/':
            # Əsas endpoint
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
            # API statusunu yoxlayan endpoint
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            # Versiya və təsvir məlumatı
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            # Əgər endpoint tapılmazsa 404 qaytarılır
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            # Testin keçməsi üçün tələb olunan dəqiq mətn:
            self.wfile.write(b"Endpoint not found")

# Serveri işə salmaq üçün əsas blok
if __name__ == "__main__":
    PORT = 8000
    # TCPServer vasitəsilə serveri 8000 portunda dinləməyə başlayırıq
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Server http://localhost:{PORT} ünvanında işləyir...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer dayandırıldı.")
            httpd.shutdown()
