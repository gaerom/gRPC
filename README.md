# gRPC
Implementing a Server

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
