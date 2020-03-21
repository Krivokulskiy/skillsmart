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
        node_to_delete = Node(0)
        node_pre = Node(0)
        len = self.len()

        if all == False:
            print ('Run whit key All = False')
            node_to_delete = self.find(val)
            if (node_to_delete == self.head) and (self.head.next == None):
                self.head = None

            elif node_to_delete == self.head:
                self.head = self.head.next
            elif node_to_delete == self.tail:
                node_pre = self.head
                while node_pre is not None:
                    if node_pre.next == node_to_delete:
                        node_pre.next = None
                    node_pre = node_pre.next
            else:
                node_pre = self.head
                while node_pre is not None:
                    if node_pre.next == node_to_delete:
                        node_pre.next = node_to_delete.next
                    node_pre = node_pre.next
        else:
            print('Run whit key All = True')
            while self.find(val) is not None:
                node_to_delete = self.find(val)
                if len > 2:
                    if node_to_delete == self.head:
                       self.head = self.head.next
                    elif node_to_delete == self.tail:
                        node_pre = self.head
                        while node_pre is not None:
                            if node_pre.next == node_to_delete:
                                node_pre.next = None
                            node_pre = node_pre.next
                    else:
                        node_pre = self.head
                        while node_pre is not None:
                            if node_pre.next == node_to_delete:
                                node_pre.next = node_to_delete.next
                            node_pre = node_pre.next

                elif (self.find(val) == self.head) and (self.head.next == None):
                    self.head = None
                elif (self.find(val) == self.head) and (self.head.next == self.tail):
                    self.head = self.tail
                    self.head.next =None
                elif (self.find(val) == self.tail) and (len == 2):
                    self.head = self.tail
                    self.head.next = None

        return

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
        return count

    def insert(self, afterNode, newNode):
        N_Node = Node(newNode)
        node = self.head
        S_Node = Node(None)
        if afterNode == None:
            S_Node = self.head

            self.head = N_Node
            self.head.next = S_Node

        else:
            while node is not None:
                if node.value == afterNode:
                    if node.next != None:
                        N_Node.next = node.next
                        node.next = N_Node
                    else:
                        self.add_in_tail(N_Node)
                node = node.next


def List_sum (first_list, second_list):
    first_value = None
    second_value = None
    node1 = Node(None)
    node2 = Node(None)
    new_node = Node(None)
    sum = 0
    list_sum = LinkedList()

    if first_list.len() == second_list.len():
        print ('List equal: OK ')
        node1 = first_list.head
        node2 = second_list.head
        while node1 is not None:
            sum = node2.value + node1.value
            new_node = Node(sum)
            list_sum.add_in_tail(new_node)

            node1 = node1.next
            node2 = node2.next
    else:
        print ('Lists are not equal')

    return list_sum














