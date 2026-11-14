class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def get_next(self):
        return self.next
   
    def get_data(self):
        return self.data

    def set_next(self, ptr):
        self.next = ptr

class Queue:
    def __init__(self, root = None):
        self.root = root
        
    def enqueue(self, new_data):
        new_node = Node(new_data)
        if self.root == None:
            self.root = new_node
        else:
            this_node = self.root
            while this_node.get_next() != None:
                this_node = this_node.get_next()
            this_node.set_next(new_node)

    def add(self, new_data):
        new_node = Node(new_data)
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
            data = self.root.get_data()
            self.root = self.root.get_next()
            return data

            
    def peek(self):
        if self.root == None:
            print('Empty queue.')
        else:
            return self.root.get_data()   

    def display(self):
        self.lst = []
        if self.root == None:
            print('There is no element in the queue.')
        else:
            this_node = self.root
            self.lst.append(this_node.get_data())
            print(this_node.get_data(), end=' <- ')
            
            while this_node.get_next():
                this_node = this_node.get_next()
                self.lst.append(this_node.get_data())
                print(this_node.get_data(), end=' <- ')
        print()
        #return self.lst
    
    def populate(self, seq):
        for ele in seq:
            self.add(ele)


def create():

    q1 = [('Adrain', '0825'),
          ('Bryan', '0845'),
          ('Charles', '1230'),
          ('Darren', '1318')]

    q2 = [('Elisa', '0805'),
          ('Farah', '0936'),
          ('Gibert', '1020'),
          ('Hong An', '1155')]

    Q1 = Queue()
    Q2 = Queue()

    Q1.populate(q1)
    Q2.populate(q2)

    return Q1, Q2
