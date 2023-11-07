# gRPC
1️⃣ The gRPC framework allows you to directly call methods of a remote application as if they were local methods.

2️⃣ You can send requests directly from the client to the server

3️⃣ You can create distributed applications more easily.

## Requirements
```
python -m pip install grpcio
python -m pip install grpcio-tools
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
