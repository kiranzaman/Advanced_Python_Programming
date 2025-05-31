def process_data(data):
    if __debug__:
        print(f"Debug: Received data: {data}")
    # Simulate processing
    result = [x * 2 for x in data]
    return result

print(process_data([1, 2, 3]))
