#queue_module.py

class Node:
    def __init__(self, name, age, next = None):
        self.name = name
        self.age = age
        self.next = next
        
    def get_next(self):
        return self.next
   
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def set_next(self, ptr):
        self.next = ptr

class Queue:
    def __init__(self, root = None):
        self.root = root
        
    def enqueue(self, new_data):
        new_name = new_data[0]
        new_age = new_data[1]
        new_node = Node(new_name, new_age)
        if self.root == None:
            self.root = new_node
        else:
            this_node = self.root
            while this_node.get_next() != None:
                this_node = this_node.get_next()
            this_node.set_next(new_node)
     
    def size(self):
        counter = 0
        if self.root == None:
            return counter
        else:
            this_node = self.root
            while this_node != None:
                counter += 1
                this_node = this_node.get_next()
            return counter

    def dequeue(self):
        if self.root == None:
            print('Cannot remove from an empty queue.')
        else:
            name = self.root.get_name()
            self.root = self.root.get_next()
            return name

    def display(self):
        if self.root == None:
            print('There is no one in the queue.')
        else:
            this_node = self.root
            print(this_node.get_name(), end=' <- ')
            
            while this_node.get_next():
                this_node = this_node.get_next()
                print(this_node.get_name(), end=' <- ')
        print()
