class Queue:
    def __init__(self, limit=10):
        self.queue = []
        self.front = None
        self.rear = None
        self.limit = limit

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.limit

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full!")
        else:
            self.queue.append(item)
            if self.front is None:
                self.front = self.rear = 0
            else:
                self.rear = self.size()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            self.queue.pop(0)
            if len(self.queue) == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size() - 1

    def size(self):
        return len(self.queue)

    def show(self):
        for i in self.queue:
            print(i, end=" ")
        print()

# Function to display the menu and get the user choice
def display_menu():
    print("Queue Operations Menu:")
    print("1. Check if Queue is empty")
    print("2. Check if Queue is full")
    print("3. Enqueue element")
    print("4. Dequeue element")
    print("5. Show all elements")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    return choice

# Function to perform the user's chosen operation
def perform_operation(choice, queue):
    if choice == 1:
        print("Queue is empty." if queue.is_empty() else "Queue is not empty.")
    elif choice == 2:
        print("Queue is full." if queue.is_full() else "Queue is not full.")
    elif choice == 3:
        if not queue.is_full():
            element = input("Enter the element you want to enqueue: ")
            queue.enqueue(element)
        else:
            print("Cannot enqueue: Queue is full.")
    elif choice == 4:
        queue.dequeue()
    elif choice == 5:
        queue.show()
    elif choice == 6:
        exit()
    else:
        print("Invalid choice. Please try again.")

# Main function to drive the queue operations
def main():
    q = Queue()  # Initialize queue with default size limit 10

    while True:
        choice = display_menu()
        perform_operation(choice, q)

# Run the main function
main()
