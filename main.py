from tkinter import *
import math
import random

#Temp (may be made input in the future)
start = [120, 120]
end = [360, 360]

#Constants
width = 400
height = 400

#variables
forest = [[0, 0, 0, 0]] #Initial tree will be removed
nodes = [[0, 0]] #Initial node will be removed

#Functions
def place_tree(tree):
    return canvas.create_oval(tree[0], tree[1], tree[2], tree[3], fill='green')

def place_start(point):
    x = point[0]
    y = point[1]

    return canvas.create_rectangle(x-10, y-10, x+10, y+10, fill='red')

def place_end(point):
    x = point[0]
    y = point[1]

    return canvas.create_polygon(x-10, y+10, x, y-10, x+10, y+10, outline='black', fill='red')

def draw_node(node):
    return canvas.create_oval(node[0], node[1], node[0], node[1], fill='blue')

def not_on_tree(node, forest):
    x = node[0]
    y = node[1]

    #Calculates if a node is within an ellipse made from the bounding box
    for tree in forest:
        #Simple calculation for speed
        if x < float(tree[0]) or y < float(tree[1]) or x > float(tree[2]) or y > float(tree[3]):
            value = 2
        #Complex calculation for accuracy
        else:
            tree_x = (float(tree[0]) + float(tree[2])) / 2
            tree_y = (float(tree[1]) + float(tree[3])) / 2
            r_x = float(tree[2]) - tree_x
            r_y = float(tree[3]) - tree_y

            value = (((x - tree_x) ** 2) / r_x ** 2) + (((y - tree_y) ** 2) / r_y ** 2)
        
        if value < 1:
            return False


    return True

def get_distance(node1, node2):
    math.sqrt(((node2[0] - node1[0]) ** 2) + ((node2[1] - node1[1]) ** 2))

#Parse Input File
treeFile = open('coordinates.txt', 'r')

for line in treeFile:
    newTree = line.split()
    
    if newTree[0] != "xmin":
        #Remove non-coordinate elements
        newTree.pop(6)
        newTree.pop(5)
        newTree.pop(0)

        forest.append(newTree)

forest.pop(0) #Remove initialization tree

#Create nodes 12 nodes on each of the 400 lines
for y in range(400):
    y = y + 1
    for i in range(25):
        x = random.randrange(1, 401, 1)
        newNode = [x, y]

        if not_on_tree(newNode, forest):
            nodes.append(newNode)

nodes.pop(0) #Remove initialization node

#Initialize window
root = Tk()
root.title("PyroGenesis")
canvas = Canvas(root, width=width, height=height, borderwidth=0, highlightthickness=0, bg="tan")
canvas.grid()
root.resizable(0,0)

#Add trees to image
for tree in forest:
    place_tree(tree)

#Add start and end points
place_start(start)
place_end(end)

#draw nodes
for node in nodes:
    draw_node(node)

#Add shortest path line


#Run the Application
root.mainloop()



