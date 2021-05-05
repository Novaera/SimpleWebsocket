from websocket_server import WebsocketServer

""" 
# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	server.send_message_to_all("Hey all, a new client has joined us") """


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
	print("Client(%d) said: %s" % (client['id'], message))
	server.send_message_to_all(message)


PORT=9001
HOST='0.0.0.0'
server = WebsocketServer(PORT)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
