import threading
import http.server


class Simple_server(threading.Thread):

	def __init__(self):
		super().__init__()
		
		

	def run(self):
		port= 8080
		bind = "127.0.0.1"
		http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler,port=port,bind=bind)
    

if __name__ == '__main__':
	s = Simple_server()
	s.start()
