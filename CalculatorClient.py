import grpc
import calculator_pb2
import calculator_pb2_grpc

def main():
    target = "localhost:50051"

    channel = grpc.insecure_channel(target)
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    operands = calculator_pb2.Operands(op1=6, op2=3)

    try:
        result = stub.Add(operands)
        print(f"6 + 3 = {result.value}")
        result = stub.Subtract(operands)
        print(f"6 - 3 = {result.value}")
        result = stub.Multiply(operands)
        print(f"6 * 3 = {result.value}")
    except grpc.RpcError as e:
        print(f"WARNING RPC failed: {e.code()}")

    channel.close()

if __name__ == "__main__":
    main()