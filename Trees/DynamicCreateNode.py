import io
import os
import time
from CommonTreeFunctions import Test as ctf
from CommonTreeFunctions import Views as ctfv
from CommonTreeFunctions import Search as ctfs
#import CommonTreeFunctions as ctf

class Node:
    def __init__(self, nodename="", nodevalue="", prevnode=None, leftnode=None, rightnode=None):
        self.name = nodename
        self.value = nodevalue
        self.prev = prevnode
        self.left = leftnode
        self.right = rightnode
    
    def input():
        print("called input in Node !!")
    
    def createNodes(n_nodes=0,inputarr={}):
        node=None
        right=None
        left=None
        firstnode=None
        prevnode=None
        nodename=""
        nodevalue=0
        #searchNode
        for k,v in inputarr.items():
            nodename=k
            nodevalue=v[2]
            
            node = Node(nodename=nodename,
                        nodevalue=nodevalue, prevnode=node,
                        leftnode=left, rightnode=right)
            if prevnode is not None:
                parentnode = ctfs.searchNode(currentnode=prevnode, nodename=v[0])
                node.prev=parentnode
                prevnode = parentnode
                if v[1] == "l":
                    parentnode.left = node
                if v[1] == "r":
                    parentnode.right = node
            else:
                prevnode = node
                
        return ctfs.searchRootNode(node)
            


n_nodes = int(input("Number of nodes:"))
nodedata={}
#n_nodes=0
for i in range(n_nodes):
    repeat=True
    while repeat:
        repeat=False
        if i == 0:
            print("---------------\nnode-{}\n---------------".format(i+1))
            inp = (str(input("Enter Root name and value :\neg: NodeA 10\n")).strip()).split(" ")
            try:
                nodename, value = inp
                if not nodedata.get(nodename, True) is True:
                    print(
                        "\nNode with name {} already exists !! Please enter another name\n".format(nodename))
                    repeat = True
                    continue
                nodedata[nodename] = [None, "X", value]
            except ValueError:
                print("\nRequired 2 arguments but given {}!!\n\n".format(len(inp)))
                repeat=True
                continue
        else:
            print("---------------\nnode-{}\n---------------".format(i+1))
            inp = (str(input("Enter ParentNode, Leaf direction(L/R), name and value :\neg: NodeA L NodeB 20\n")).strip()).split(" ")
            try:
                parent, direction, nodename, value = inp
                if nodedata.get(parent, True) is True:
                    print(
                        "\nParent node with name {} doesn't exists !! Please try again.\n".format(parent))
                    repeat = True
                    continue
                if not nodedata.get(nodename, True) is True:
                    print(
                        "\nNode with name {} already exists !! Please enter another name.\n".format(nodename))
                    repeat = True
                    continue
                nodedata[nodename] = [parent, direction, value]
            except ValueError:
                print("\nRequired 4 arguments but given {}!!\n\n".format(len(inp)))
                repeat = True
                continue
        break
    print(end="\n")

print("Creating Nodes....")
node=Node.createNodes(n_nodes,nodedata)
print("Done....")


"""
n_nodes=int(input("Number of nodes:"))
node=None
firstnode=None
nodedata=""
for i in range(n_nodes):
    os.system("cls")
    rightnode=None
    leftnode=None
    prevnode=node
    if node is None:
        pass
        #nodedata=input("Enter Root Node Value:")
    node = Node(nodename="Node-{}".format(i+1), nodevalue=1+i, prevnode=node)
    if prevnode is not None:
        prevnode.next = node
    if firstnode is None:
        firstnode = node
    print("Created Node-{}".format(i+1))
    #node.ShowNodes() # last node, so traverse prev
    # first node, so traverse next
    ctfv.ShowNodes(firstnode=firstnode, n_nodes=n_nodes)
    time.sleep(0.2)
node.first = firstnode

#ctf.testfunc()
#node.ShowNodes()

"""