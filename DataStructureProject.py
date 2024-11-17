#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Structures GUI")
        self.master.geometry("600x600")
        self.master.configure(bg='darkblue')

        self.title_label = tk.Label(self.master, text="DATA STRUCTURE", font=("Times New Roman", 20, "bold"), bg='darkblue', fg='white').pack()

        self.button_frame = tk.Frame(master, bg='darkblue')
        self.button_frame.pack(side=tk.TOP, pady=15)


        # Create buttons for each data structure
        self.stack_button = tk.Button(self.button_frame, text="Linear \n Stack", command=self.show_stack_gui, bg='lightgray' , height=3, width=15)
        self.stack_button.pack(side=tk.LEFT, padx=10)

        self.singly_ll_button = tk.Button(self.button_frame, text="Singly Linked \n List", command=self.show_singly_linked_list_gui, bg='lightgray', height=3, width=15)
        self.singly_ll_button.pack(side=tk.LEFT, padx=10)

        self.doubly_ll_button = tk.Button(self.button_frame, text="Doubly Linked \n List", command=self.show_doubly_linked_list_gui, bg='lightgray', height=3, width=15)
        self.doubly_ll_button.pack(side=tk.LEFT, padx=10)
        
        self.circular_ll_button = tk.Button(self.button_frame, text="Circular Linked \n List", command=self.show_circular_linked_list_gui, bg='lightgray', height=3, width=15)
        self.circular_ll_button.pack(side=tk.LEFT, padx=10)
        
        self.queue_button = tk.Button(self.button_frame, text="Queue", command=self.show_queue_gui, bg='lightgray', height=3, width=15)
        self.queue_button.pack(side=tk.LEFT, padx=10)

        self.pq_button = tk.Button(self.button_frame, text="Priority Queue", command=self.show_priority_queue_gui, bg='lightgray', height=3, width=15)
        self.pq_button.pack(side=tk.LEFT, padx=10)

    
        self.operation_frame = tk.Frame(master, bg='darkblue')
        self.operation_frame.pack(pady=10)

        self.current_gui = None  # To hold the current active GUI component

    def clear_operation_frame(self):
        for widget in self.operation_frame.winfo_children():
            widget.destroy()

    def show_stack_gui(self):
        self.clear_operation_frame()
        self.current_gui = StackGUI(self.operation_frame)
        
    def show_circular_linked_list_gui(self):
        self.clear_operation_frame()
        self.current_gui = CircularLinkedListGUI(self.operation_frame)
        
    def show_queue_gui(self):
        self.clear_operation_frame()
        self.current_gui = QueueGUI(self.operation_frame)

    def show_priority_queue_gui(self):
        self.clear_operation_frame()
        self.current_gui = PriorityQueueGUI(self.operation_frame)

    def show_singly_linked_list_gui(self):
        self.clear_operation_frame()
        self.current_gui = LinkedListGUI(self.operation_frame)

    def show_doubly_linked_list_gui(self):
        self.clear_operation_frame()
        self.current_gui = DoublyLinkedListGUI(self.operation_frame)

# Stack class
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items

class StackGUI:
    def __init__(self, master):
        self.master = master
        self.title_label = tk.Label(master, text="Linear Stack", font=("Times New Roman", 20, "bold"), bg='darkblue', fg='white')
        self.title_label.pack(pady=10)

        self.stack = Stack()

        self.entry_label = tk.Label(master, text="Enter Element:", font=("Times New Roman", 14), bg='darkblue', fg='white')
        self.entry_label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.push_button = tk.Button(master, text="Push", command=self.push_element,  bg="light Blue", fg="black", font=("Times New Roman", 14))
        self.push_button.pack(pady=5)

        self.pop_button = tk.Button(master, text="Pop", command=self.pop_element,  bg="light Blue", fg="black", font=("Times New Roman", 14))
        self.pop_button.pack(pady=5)

        self.stack_display = tk.Text(master, height=10, width=40, font=("Times New Roman", 14), bg='lightgray')
        self.stack_display.pack(pady=10)

        self.message_label = tk.Label(master, text="", bg='darkblue', fg='white', font=("Times New Roman", 14))
        self.message_label.pack()

    def push_element(self):
        element = self.entry.get()
        if element:
            self.stack.push(element)
            self.entry.delete(0, tk.END)
            self.update_display()
            self.message_label.config(text=f"Pushed: {element}")
        else:
            self.message_label.config(text="Please enter a value to push.")

    def pop_element(self):
        if not self.stack.is_empty():
            popped = self.stack.pop()
            self.update_display()
            self.message_label.config(text=f"Popped: {popped}")
        else:
            self.message_label.config(text="Stack is empty. Nothing to pop.")
    def display_stack(self):
        self.update_display()

    def update_display(self):
        self.stack_display.delete(1.0, tk.END)
        for item in self.stack.display():
            self.stack_display.insert(tk.END, str(item) + "\n")


##Singly linked list

class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = SinglyNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, index):
        if self.head is None:
            return False        
        temp = self.head
        if index == 0:
            self.head = temp.next
            return True
        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                return False
        if temp is None or temp.next is None:
            return False
        temp.next = temp.next.next
        return True

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

class LinkedListGUI:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg='darkblue')

        self.title_label = tk.Label(master, text="Singly Linked List", font=("Times New Roman", 20, "bold"), bg='darkblue', fg='white')
        self.title_label.pack(pady=10)

        self.linked_list = SinglyLinkedList()

        self.entry_label = tk.Label(master, text="Enter Element:", font=("Times New Roman", 14), bg='darkblue', fg='white')
        self.entry_label.pack()

        self.entry = tk.Entry(master, font=("Times New Roman", 14), bg='lightgray', fg='black')
        self.entry.pack()

        self.insert_button = tk.Button(master, text="Insert", command=self.insert_node, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.insert_button.pack(pady=5)

        self.delete_label = tk.Label(master, text="Delete Index:", font=("Times New Roman", 14), bg='darkblue', fg='white')
        self.delete_label.pack()

        self.delete_entry = tk.Entry(master, font=("Times New Roman", 14), bg='lightgray', fg='black')
        self.delete_entry.pack()

        self.delete_button = tk.Button(master, text="Delete", command=self.delete_node, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.delete_button.pack(pady=5)

        self.traverse_button = tk.Button(master, text="Traverse", command=self.traverse_list, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.traverse_button.pack(pady=5)

        # Label to display messages
        self.output_label = tk.Label(master, text="", font=("Times New Roman", 14), bg='darkblue', fg='white')
        self.output_label.pack(pady=10)

    def insert_node(self):
        value = self.entry.get()
        if value:
            self.linked_list.insert(value)
            self.entry.delete(0, tk.END)
            self.output_label.config(text=f"Inserted element: {value}")
        else:
            self.output_label.config(text="Input Error: Please enter a value")

    def delete_node(self):
        index = self.delete_entry.get()
        if index.isdigit():
            success = self.linked_list.delete(int(index))
            if success:
                self.delete_entry.delete(0, tk.END)
                self.output_label.config(text=f"Deleted node at index {index}")
            else:
                self.output_label.config(text="Error: Invalid index or list is empty")
        else:
            self.output_label.config(text="Input Error: Please enter a valid index")

    def traverse_list(self):
        elements = self.linked_list.traverse()
        if elements:
            self.output_label.config(text=f"List Contents: {' -> '.join(elements)}")
        else:
            self.output_label.config(text="List is empty.")
        

### Doubly Linked List
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_node(self, key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            return
        while temp:
            if temp.data == key:
                break
            temp = temp.next
        if temp is None:
            return
        if temp.next is not None:
            temp.next.prev = temp.prev
        if temp.prev is not None:
            temp.prev.next = temp.next

    def traverse(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        return nodes
    
class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def cll_insert(self,value):
        new=CircularNode(value)
        if self.head is None:
            self.head=new
            new.next=self.head
        else:
            new.next=self.head
            curr=self.head
            while curr.next != self.head:
                curr=curr.next
            curr.next=new
    def cll_delete(self, index):
        if self.head is None:
            return False        
        temp = self.head
        if index == 0:
            if temp.next==self.head:
                self.head = None
                return True
            else:
                last = self.head
                while last.next != self.head:
                    last = last.next
                self.head = temp.next
                last.next = self.head
            return True
           
        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                return False
        if temp is None or temp.next is None:
            return False
        temp.next = temp.next.next
        return True
    
    def cll_traverse(self):
        elements = []
        current = self.head
        if not self.head:
            return False
        while True:
            elements.append(current.data)
            current = current.next
            if current ==self. head:
                break
        return elements
    
class CircularLinkedListGUI:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg='darkblue')
        self.title_label = tk.Label(master, text="Circular Linked List", font=("Times New Roman", 20, "bold"), bg='darkblue', fg='white')
        self.title_label.pack(pady=10)
        
        self.cll_linked_list = CircularLinkedList()
        
        self.entry_label = tk.Label(master, text="Enter Element:", font=("Times New Roman", 14), bg='darkblue', fg='white')
        self.entry_label.pack()
        
        self.entry = tk.Entry(master, font=("Times New Roman", 14), bg='lightgray', fg='black')
        self.entry.pack()
        
        self.insert_button = tk.Button(master, text="Insert", command=self.cll_insert_node, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.insert_button.pack(pady=5)
        
        self.delete_label = tk.Label(master, text="Delete Index:", font=("Times New Roman", 14), bg='darkblue', fg='white')
        self.delete_label.pack()

        self.delete_entry = tk.Entry(master, font=("Times New Roman", 14), bg='lightgray', fg='black')
        self.delete_entry.pack()

        self.delete_button = tk.Button(master, text="Delete", command=self.cll_delete_node, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.delete_button.pack(pady=5)

        self.traverse_button = tk.Button(master, text="Traverse", command=self.cll_traverse_list, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.traverse_button.pack(pady=5)

        # Label to display messages
        self.output_label = tk.Label(master, text="", font=("Times New Roman", 14), bg='darkblue', fg='white')
        self.output_label.pack(pady=10)
        
    def cll_insert_node(self):
        value = self.entry.get()
        if value:
            self.cll_linked_list.cll_insert(value)
            self.entry.delete(0, tk.END)
            self.output_label.config(text=f"Inserted element: {value}")
        else:
            self.output_label.config(text="Input Error: Please enter a value")
            
    def cll_delete_node(self):
        index = self.delete_entry.get()
        if index.isdigit():
            success = self.cll_linked_list.cll_delete(int(index))
            if success:
                self.delete_entry.delete(0, tk.END)
                self.output_label.config(text=f"Deleted node at index {index}")
            else:
                self.output_label.config(text="Error: Invalid index or list is empty")
        else:
            self.output_label.config(text="Input Error: Please enter a valid index")
            
    def cll_traverse_list(self):
        elements = self.cll_linked_list.cll_traverse()
        if elements:
            self.output_label.config(text=f"List Contents: {' -> '.join(elements)}")
        else:
            self.output_label.config(text="List is empty.")

class DoublyLinkedListGUI:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg='darkblue')

        self.title_label = tk.Label(master, text="Doubly Linked List", font=("Times New Roman", 20, "bold"), bg='darkblue', fg='white')
        self.title_label.pack(pady=10)

        self.doubly_linked_list = DoublyLinkedList()

        self.entry_label = tk.Label(master, text="Enter Element:",font=("Times New Roman", 14), bg='darkblue', fg='white')
        self.entry_label.pack()

        self.entry = tk.Entry(master, font=("Times New Roman", 14), bg='lightgray', fg='black')
        self.entry.pack()

        self.insert_begin_button = tk.Button(master, text="Insert at Beginning", command=self.insert_at_beginning, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.insert_begin_button.pack(pady=5)

        self.insert_end_button = tk.Button(master, text="Insert at End", command=self.insert_at_end, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.insert_end_button.pack(pady=5)

        self.delete_label = tk.Label(master, text="Delete Element:", bg='darkblue', fg='white', font=("Times New Roman", 14))
        self.delete_label.pack()

        self.delete_entry = tk.Entry(master, font=("Times New Roman", 14), bg='lightgray', fg='black')
        self.delete_entry.pack()

        self.delete_button = tk.Button(master, text="Delete", command=self.delete_element, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.delete_button.pack(pady=5)

        self.traverse_button = tk.Button(master, text="Traverse", command=self.traverse_list, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.traverse_button.pack(pady=5)

        self.dll_display = tk.Text(master, height=10, width=40, bg='lightgray', font=("Times New Roman", 14))
        self.dll_display.pack(pady=10)

        self.message_label = tk.Label(master, text="", bg='darkblue', fg='white', font=("Times New Roman", 14))
        self.message_label.pack()

    def insert_at_beginning(self):
        element = self.entry.get()
        if element:
            self.doubly_linked_list.insert_at_beginning(element)
            self.entry.delete(0, tk.END)
            self.update_display(f"Inserted {element} at the beginning.")
        else:
            messagebox.showwarning("Input Error", "Please enter a value")

    def insert_at_end(self):
        element = self.entry.get()
        if element:
            self.doubly_linked_list.insert_at_end(element)
            self.entry.delete(0, tk.END)
            self.update_display(f"Inserted {element} at the end.")
        else:
            messagebox.showwarning("Input Error", "Please enter a value")

    def delete_element(self):
        element = self.delete_entry.get()
        if element:
            self.doubly_linked_list.delete_node(element)
            self.delete_entry.delete(0, tk.END)
            self.update_display(f"Deleted {element}.")
        else:
            messagebox.showwarning("Input Error", "Please enter a value to delete")

    def traverse_list(self):
        elements = self.doubly_linked_list.traverse()
        self.dll_display.delete(1.0, tk.END)
        if elements:
            self.dll_display.insert(tk.END, " <-> ".join(map(str, elements)))
        else:
            self.dll_display.insert(tk.END, "List is empty.")

    def update_display(self, message):
        self.dll_display.delete(1.0, tk.END)  # Clear the display
        self.dll_display.insert(tk.END, message)  # Show the operation message
        
                
class Queue:
    def __init__(self):
        self.items = []
        self.max_size = None

    def set_size(self, size):
        self.max_size = size

    def enqueue(self, item):
        if self.max_size is not None and len(self.items) >= self.max_size:
            return False
        self.items.append(item)
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def traverse(self):
        return self.items.copy()

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items.clear() 

class QueueGUI:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg='darkblue')

        self.title_label = tk.Label(master, text="Queue Operations", font=("Times New Roman", 20, "bold"), bg='darkblue', fg='white')
        self.title_label.pack(pady=10)

        self.queue = Queue()

        self.size_label = tk.Label(master, text="Set Max Size (optional):", bg='darkblue', fg='white', font=("Times New Roman", 14))
        self.size_label.pack()

        self.size_entry = tk.Entry(master, font=("Times New Roman", 14), bg='lightgray', fg='black')
        self.size_entry.pack()

        self.set_size_button = tk.Button(master, text="Set Size", command=self.set_queue_size, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.set_size_button.pack(pady=5)

        self.entry_label = tk.Label(master, text="Enter Element:", bg='darkblue', fg='white', font=("Times New Roman", 14))
        self.entry_label.pack()

        self.entry = tk.Entry(master, font=("Times New Roman", 14), bg='lightgray', fg='black')
        self.entry.pack()

        self.enqueue_button = tk.Button(master, text="Enqueue", command=self.enqueue_element, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.enqueue_button.pack(pady=5)

        self.dequeue_button = tk.Button(master, text="Dequeue", command=self.dequeue_element, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.dequeue_button.pack(pady=5)

        # Add a traverse button
        self.traverse_button = tk.Button(master, text="Traverse", command=self.traverse_queue, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.traverse_button.pack(pady=5)

        self.queue_display = tk.Text(master, height=5, width=40, bg='lightgray', font=("Times New Roman", 14))
        self.queue_display.pack(pady=10)

        self.message_label = tk.Label(master, text="", bg='darkblue', fg='white', font=("Times New Roman", 14))
        self.message_label.pack()

    def set_queue_size(self):
        size = self.size_entry.get()
        if size.isdigit() and int(size) > 0:
            self.queue.set_size(int(size))
            self.size_entry.delete(0, tk.END)
            self.message_label.config(text="Queue size set successfully.")
        else:
            self.entry.delete(0, tk.END)
            self.message_label.config(text="Invalid Input: Please enter a valid positive number.")

    def enqueue_element(self):
        element = self.entry.get()
        if element:
            if not self.queue.enqueue(element):
                self.message_label.config(text="Queue is full.")
            else:
                self.entry.delete(0, tk.END)
                self.update_display()
                self.message_label.config(text=f"Enqueued: {element}")
        else:
            self.entry.delete(0, tk.END)
            self.message_label.config(text="Please enter an element to enqueue.")

    def dequeue_element(self):
        if self.queue.is_empty():
            self.message_label.config(text="Queue is empty. Nothing to dequeue.")
        else:
            dequeued = self.queue.dequeue()
            self.update_display()
            self.message_label.config(text=f"Dequeued: {dequeued}")

    def traverse_queue(self):
        elements = self.queue.traverse()
        self.queue_display.delete(1.0, tk.END)  # Clear the display
        if elements:
            self.queue_display.insert(tk.END, "->".join(map(str, elements)))  # Show elements line by line
        else:
            self.queue_display.insert(tk.END, "Queue is empty.")

    def update_display(self):
        self.queue_display.delete(1.0, tk.END)
        for item in self.queue.traverse():
            self.queue_display.insert(tk.END, str(item) + "\n")

            

class PriorityQueue:
    def __init__(self, size=0):
        self.queue = []
        self.size = size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.size

    def enqueue(self, data, priority):
        if self.size == 0:
            return "Please set the queue size before enqueuing data"
        if data.strip():
            if self.is_full():
                return "Queue is full"
            elif any(p == priority for p, d in self.queue):
                return "Priority already exists. Please enter a unique priority."
            else:
                self.queue.append((priority, data))
                self.queue.sort(key=lambda x: x[0])  # Smallest priority to highest
                return f"Enqueued: {data} with priority {priority}"
        else:
            return "Data cannot be empty"

    def dequeue_lowest(self):
        if not self.is_empty():
            return self.queue.pop(0)[1]  # Remove first element (smallest priority)
        else:
            return "Priority queue is empty"

    def dequeue_highest(self):
        if not self.is_empty():
            return self.queue.pop(-1)[1]  # Remove last element (highest priority)
        else:
            return "Priority queue is empty"

    def traverse_lowest(self):
        if not self.is_empty():
            return [f"{data}, Priority: {priority}" for priority, data in self.queue]
        else:
            return ["Queue is empty"]

    def traverse_highest(self):
        if not self.is_empty():
            return [f"{data}, Priority: {priority}" for priority, data in reversed(self.queue)]
        else:
            return ["Queue is empty"]

    def clear_queue(self):
        self.queue.clear()

class PriorityQueueGUI:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg="darkblue")
        self.priority_queue = PriorityQueue()

        # Labels and entry widgets
        self.title_label = tk.Label(master, text="Priority Queue Operations", font=("Times New Roman", 20, "bold"), bg="darkblue", fg="white")
        self.title_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        self.size_label = tk.Label(master, text="Queue Size:", bg="darkblue", fg="white", font=("Times New Roman", 14))
        self.size_label.grid(row=1, column=0, padx=10, pady=10)
        self.size_entry = tk.Entry(master, font=("Times New Roman", 14), bg="lightgray", fg="black")
        self.size_entry.grid(row=1, column=1, padx=10, pady=10)
        self.set_size_button = tk.Button(master, text="Set Size", command=self.set_size, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.set_size_button.grid(row=1, column=2, padx=10, pady=10)

        self.data_label = tk.Label(master, text="Data:", bg="darkblue",fg="white", font=("Times New Roman", 14))
        self.data_label.grid(row=2, column=0, padx=10, pady=10)
        self.data_entry = tk.Entry(master, font=("Times New Roman", 14), bg="lightgray", fg="black")
        self.data_entry.grid(row=2, column=1, padx=10, pady=10)

        self.priority_label = tk.Label(master, text="Priority:", bg="darkblue", fg="white", font=("Times New Roman", 14))
        self.priority_label.grid(row=3, column=0, padx=10, pady=10)
        self.priority_entry = tk.Entry(master, font=("Times New Roman", 14), bg="lightgray", fg="black")
        self.priority_entry.grid(row=3, column=1, padx=10, pady=10)

        self.enqueue_button = tk.Button(master, text="Enqueue", command=self.enqueue, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.enqueue_button.grid(row=3, column=2, padx=10, pady=10)

        self.dequeue_lowest_button = tk.Button(master, text="Dequeue Lowest", command=self.dequeue_lowest, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.dequeue_lowest_button.grid(row=4, column=0, padx=10, pady=10)

        self.dequeue_highest_button = tk.Button(master, text="Dequeue Highest", command=self.dequeue_highest, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.dequeue_highest_button.grid(row=4, column=1, padx=10, pady=10)

        self.traverse_lowest_button = tk.Button(master, text="Traverse Lowest", command=self.traverse_lowest, bg="lightblue", fg="black", font=("Times New Roman", 16))
        self.traverse_lowest_button.grid(row=4, column=2, padx=10, pady=10)

        self.traverse_highest_button = tk.Button(master, text="Traverse Highest", command=self.traverse_highest, bg="lightblue", fg="black", font=("Times New Roman", 16))
        self.traverse_highest_button.grid(row=4, column=3, padx=10, pady=10)

        self.clear_button = tk.Button(master, text="Clear Queue", command=self.clear_queue, bg="lightblue", fg="black", font=("Times New Roman", 14))
        self.clear_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.output_text = tk.Text(master, height=10, width=50, bg="lightgray", fg="black", font=("Times New Roman", 14))
        self.output_text.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

    def set_size(self):
        size = self.size_entry.get()
        if size.isdigit() and int(size) > 0:
            self.priority_queue.size = int(size)
            self.update_output(f"Queue size set to {size}.")
            self.size_entry.delete(0, tk.END)
        else:
            self.update_output("Invalid Input: Please enter a valid positive size.")

    def enqueue(self):
        data = self.data_entry.get()
        priority = self.priority_entry.get()
        if not data:
            self.update_output("Invalid Input: Data cannot be empty.")
            return
        if priority.isdigit():
            result = self.priority_queue.enqueue(data, int(priority))
            self.update_output(result)
            if result.startswith("Enqueued"):
                self.data_entry.delete(0, tk.END)
                self.priority_entry.delete(0, tk.END)
        else:
            self.update_output("Invalid Input: Please enter a valid priority.")

    def dequeue_lowest(self):
        item = self.priority_queue.dequeue_lowest()
        self.update_output(f"Dequeued (Lowest Priority): {item}")

    def dequeue_highest(self):
        item = self.priority_queue.dequeue_highest()
        self.update_output(f"Dequeued (Highest Priority): {item}")

    def traverse_lowest(self):
        items = self.priority_queue.traverse_lowest()
        self.update_output("Queue (Lowest to Highest Priority):\n" + "\n".join(items))

    def traverse_highest(self):
        items = self.priority_queue.traverse_highest()
        self.update_output("Queue (Highest to Lowest Priority):\n" + "\n".join(items))



    def clear_queue(self):
        self.priority_queue.clear_queue()
        self.update_output("Queue cleared.")

    def update_output(self, message):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, message + "\n")

        
# Main application code
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




