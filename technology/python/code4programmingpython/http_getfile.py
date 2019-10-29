import http.client
class URL:
	def __init__(self,sn,fn):
		self.sn = sn #servername
		self.fn = fn #filename

	def fetch(self):
		server = http.client.HTTPConnection(self.sn)
		server.putrequest('GET',self.fn)
		server.putheader('Accept', 'text/html')
		server.endheaders()
		reply = server.getresponse()
		if reply.status != 200:
			print('Error sending request', reply.status, reply.reason)
		else:
			data = reply.readlines()
			reply.close()
			for line in data:
				print(line)
