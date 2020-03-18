class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        out_list = []
        count = 0
        node = self.head
        if (self.head == None) and (self.tail == None):
            print ('List ia a EMPTY')
            exit()

        while node is not None:
            if node.value == val:
                out_list.append(node.value)
                count += 1
            node = node.next
        if count == 0:
            print('Nothing found')
        return out_list

    def delete(self, val, all=False):
        print('Del function started')



        if all == True: print('key "all" set as "True"')
        if all == False: print('key "all" set as "False"')
        if (self.head == None) and (self.tail == None): ## Проерка списка на отсутсвтие элементов
            print('List ia a EMPTY')
            exit()
        node = self.head

        while node is not None:
            if node.value == val:
                node_del = node

                if (node_del != self.head) and (node_del.next != self.tail):
                    print('Node for delete is:', node_del.value)
                    node_next = node_del.next
                    print('Next_node is:',node_del.next.value)
                    node_pred = self.head
                    while node_pred != node_del:
                        if node_pred.next == node_del:
                            print('Node_pred found:', node_pred.value)
                            node_pred.next = node_next
                            exit()
                        node_pred = node_pred.next
                    continue

                elif (node_del == self.head) and (node_del.next == None):
                    print('List have only one Node')
                    if node_del.value == val:
                        self.head = None
                        self.tail = None
                        exit

                elif (node_del == self.head) and (node_del.next == self.tail):
                    print ('Node found in  head. Only two Nodes in the List')
                    self.head = node_del.next
                    self.tail = None
                    ## exit
                    continue

                elif (node_del == self.tail):
                    print ('Node found in  tail')
                    node_pred = self.head
                    while node_pred is not None:
                        if node_pred.next == node_del:
                            print ('Node_pred found:', node_pred.value)
                            node_pred.next = None
                        node_pred = node_pred.next
                    continue
            node = node.next



    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        none_count = 0
        node = self.head
        if (self.head == None) and (self.tail == None):
            print ('List ia a EMPTY')
            exit()
        else:
            while node is not None:
                count = count +1
                if node.value == None:
                    none_count = none_count +1
                node = node.next
        print ('Len of List is:',count, ' Empty value:', none_count)
        return

    def insert(self, afterNode, newNode):
        pass # здесь будет ваш код

L_list=LinkedList()
n1=Node(9)
n2=Node(14)
n3=Node(12)
n4=Node(15)
L_list.add_in_tail(n1)
L_list.add_in_tail(n2)
L_list.add_in_tail(n3)
L_list.add_in_tail(n4)
L_list.print_all_nodes()












