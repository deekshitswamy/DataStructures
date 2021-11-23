import io
import time

class Test:
    def __init__(self):
        pass

    def testfunc():
        print("Hello test !!!")

class Search:
    def __init__(self):
        pass

    def searchNode(currentnode=None,nodename=None,nodevalue=None):
        rootnode=None
        node=currentnode
        # nav to the root node from current node, if not found raise error
        while node.prev is not None:
            node=node.prev
        if node.prev is None:
            rootnode=node
        
        #check if value found in parent node
        if node.name == nodename:
            return node
        #check left side of the tree and then right
        node = rootnode.left
        checked_right = False
        while node is not None:
            if node.name == nodename:
                return node
            if node.left is not None:
                node=node.left
                continue
            elif node.right is not None:
                node=node.right
                continue
            else:
                node=node.prev
                if node is None and checked_right is False:
                    node=node.right
                    checked_right=True
        return None 
        #check right side of the tree
    
    def searchRootNode(currentnode=None):
        rootnode = None
        node = currentnode
        # nav to the root node from current node, if not found raise error
        while node.prev is not None:
            node = node.prev
        if node.prev is None:
            rootnode = node
        return rootnode       

class Views:
    def __init__(self):
        pass

    def viewTree():
        pass

    def ShowNodes(firstnode=None, n_nodes=1):
        #node = self.first
        node = firstnode
        is_done = False
        tabspace = "|"
        i=0
        while not is_done:
            if node == None:
                is_done = True
                continue
            #print("Node name: {}\nNode value: {}\nFirst Node address: {}".format(node.name, node.value,node.first))
            # right side print
            '''
            print("{tab}[{nodename}]\n{tab}   ({nodevalue})".format(tab=tabspace,
                  nodename=node.name, nodevalue=node.value))
            tabspace+="\t|"
            print("{tab}\\".format(tab=tabspace))
            '''

            # left side print
            tabspace = "\t"
            print("{tab}[{nodename}]\n{tab}   ({nodevalue})".format(tab=(n_nodes-i)*tabspace,
                  nodename=node.name, nodevalue=node.value))
            print("{tab}/".format(tab=(n_nodes-i)*tabspace))

            node = node.next
            #node = node.prev

            i+=1