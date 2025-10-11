# ============================= what is alias =============================
# Alias is a way to give a new name to a type.
# It is a way to create a new alias by using the type alias protocol.

# 1. Example
from typing import (
    List, Dict, TypedDict, 
    # Union,
    # Optional, Callable, Type, TypeVar,
    # Generic, Protocol, Literal, NewType,
    # TypedDict, Annotated, Final, ClassVar,
    # TypeAlias
    
)

#============================ alias =============================
hostName = str
address = str
port = int
server = Dict[hostName, address, port]
network = List[server]


class Server(TypedDict):
    hostName: str
    address: str
    port: int
# data server
server: Server = {
    "hostName": "LocalHost",
    "address": "127.0.0.1",
    "port": 8080
}

# list of servers
newServer: List[Server] = [
    {"hostName": "LocalHost", "address": "127.0.0.1", "port": 8080},
    {"hostName": "MyServer", "address": "192.168.0.10", "port": 8000}
]
