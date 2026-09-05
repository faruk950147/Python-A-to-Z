from typing import (
    List, Dict
)

hostName = str
print(f"hostName: {type(hostName)}") # <class 'type'>

address = str
print(f"address: {type(address)}") # <class 'type'>

port = int
print(f"port: {type(port)}") # <class 'type'>

server = Dict[str, str | int]
print(f"server: {type(server)}") # <class 'typing._GenericAlias'>

network = List[server]
print(f"network: {type(network)}") # <class 'typing._GenericAlias'>




# Type Hinting with Literal

server_data: Dict[str, str | int] = {
    "hostName": "localhost",
    "address": "127.0.0.1",
    "port": 8000
}

network_data: List[Dict[str, str | int]] = [server_data]
print(server_data)
print(network_data)
