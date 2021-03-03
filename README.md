# TCP

A simple TCP server/client implementation using Python module socket and threading.

## Usage

### Server

Enter `python server.py` in terminal to boot the server. On receiving a message from a client, server will print it and forward it to other clients. 


```
Client at ('192.168.72.1', 5615) has connected
Client at ('192.168.72.1', 5617) has connected
Client at ('192.168.72.1', 5615): hey
Client at ('192.168.72.1', 5617): hello
Client at ('192.168.72.1', 5628) has connected
Client at ('192.168.72.1', 5628): hi
Client at ('192.168.72.1', 5628) has disconnected
Client at ('192.168.72.1', 5617) has disconnected
Client at ('192.168.72.1', 5615) has disconnected
```
### Client

Enter `python client.py` in another terminal to boot a client. input something then press enter, client will send this message to server.

#### Client A

```
hey
Client at ('192.168.72.1', 5617): hello
Client at ('192.168.72.1', 5628): hi
```

#### Client B

```
Client at ('192.168.72.1', 5615): hey
hello
Client at ('192.168.72.1', 5628): hi
```

#### Client C

```
hi
```