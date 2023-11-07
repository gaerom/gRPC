# gRPC(Remote Procedure Call)
1️⃣ The gRPC framework allows you to directly call the methods of a remote application as if they were local methods.  
2️⃣ You can send requests directly from the client to the server.  
3️⃣ You can create distributed applications more easily. 

<img width="1024" alt="architecture" src="https://github.com/gaerom/gRPC/assets/92725975/c74fe84f-1b44-4bd3-8fa2-f342b5d624db">


# Usage  
First, install prerequisites with
```
$ python -m pip install grpcio
$ python -m pip install grpcio-tools
```

## Compilation
💡 When you write a .proto file and compile it, server skeleton and client stub are automatically generated.  
You can check a newly generated protocol buffer file.

```
python -m grpc_tools.protoc -I. —python_out=. —grpc_python_out=. ./calculator.proto
```

## Run
### Run the Server(Start the server first)
```
python3 CalculatorServer.py
```

### Run the Client
```
python3 CalculatorClient.py
```
