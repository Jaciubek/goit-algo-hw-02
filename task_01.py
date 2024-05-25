from queue import Queue

# Create a queue
queue = Queue(maxsize=10)

# Defined a unique number for request
request_number = 0

# Function that generates new requests and add them to the queue
def generate_request():
    global request_number
    request_number += 1
    request = f"Request-{request_number}"
    queue.put(request)
    print(f"Generated: {request}")

# Function that processes requests from the queue
def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Processing: {request}")
        print(f"Completed: {request}")
    else:
        print("Important message - The queue is empty")

# Main cycle
def main_cycle():
    try:
        while True:
            generate_request()
            process_request()
    except KeyboardInterrupt:
        print("The program has been terminated by the user.")

if __name__ == "__main__":
    main_cycle()

# Push ctrl+c to terminate this program