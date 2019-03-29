import string;


# side_1 = [];
# side_2 = [];
# side_3 = [];
# side_4 = [];
# side_5 = [];
# side_6 = [];

cube = [['G','G','G','G','G','G','G','G','G'],['O','O','O','O','O','O','O','O','O'],['R','R','R','R','R','R','R','R','R'],['Y','Y','Y','Y','Y','Y','Y','Y','Y'],['W','W','W','W','W','W','W','W','W'],['B','B','B','B','B','B','B','B','B']]

# string_1= raw_input('Type Side1 colors in order starting at the top left corner and go row by row for the whole side: (Use capital letters for colors Ex: YOB = Yellow, Orange, Blue): ');
# cube[0] = list(string_1);
#
# string_2= raw_input('Type Side2 colors in order starting at the top left corner and go row by row for the whole side: (Use capital letters for colors Ex: YOB = Yellow, Orange, Blue): ');
# cube[1] = list(string_2);
# string_3= raw_input('Type Side3 colors in order starting at the top left corner and go row by row for the whole side: (Use capital letters for colors Ex: YOB = Yellow, Orange, Blue): ');
# cube[2] = list(string_3);
# string_4= raw_input('Type Side4 colors in order starting at the top left corner and go row by row for the whole side: (Use capital letters for colors Ex: YOB = Yellow, Orange, Blue): ');
# cube[3] = list(string_4);
# string_5= raw_input('Type Side5 colors in order starting at the top left corner and go row by row for the whole side: (Use capital letters for colors Ex: YOB = Yellow, Orange, Blue): ');
# cube[4] = list(string_5);
# string_6= raw_input('Type Side6 colors in order starting at the top left corner and go row by row for the whole side: (Use capital letters for colors Ex: YOB = Yellow, Orange, Blue): ');
# cube[5] = list(string_6);



def rowTurn(row_numb, direction):
    # 1 = Right and -1 = Left
    tempList1 = []
    tempList2 = []
    tempList3 = []
    tempList4 = []
    if(row_numb == 1):
        start = 0
        end = 3
    elif(row_numb == 2):
        if(direction == 1):
            rowTurn(1,-1)
            rowTurn(3,-1)
            swap(0,3)
            swap(4,3)
            swap(3,5)
            return
        else:
            rowTurn(1,1)
            rowTurn(3,1)
            swap(0,4)
            swap(3,4)
            swap(4,5)
            return
    else:
        start = 6
        end = 9
    # If its the first row then we know the first 3 numbers from each array will be altered
    if(direction == 1):
        for x in range(start,end):
            tempList1.append(cube[0][x])
            tempList2.append(cube[3][x])
            tempList3.append(cube[4][x])
            tempList4.append(cube[5][x])
        # This copies the first 3 numbers of the sides into lists
        y=0
        for x in range(start,end):
            cube[0][x] = tempList2[y]
            cube[3][x] = tempList4[y]
            cube[4][x] = tempList1[y]
            cube[5][x] = tempList3[y]
            y+=1
        del tempList1[:]
        del tempList2[:]
        del tempList3[:]
        del tempList4[:]
    # Now we do the a similar format for the opposite direction (Left)
    if(direction == -1):
        for x in range(start,end):
            tempList1.append(cube[0][x])
            tempList2.append(cube[3][x])
            tempList3.append(cube[4][x])
            tempList4.append(cube[5][x])

        # This copies the first 3 numbers of the sides into lists
        y=0
        for x in range(start,end):
            cube[0][x] = tempList3[y]
            cube[3][x] = tempList1[y]
            cube[4][x] = tempList4[y]
            cube[5][x] = tempList2[y]
            y+=1

        del tempList1[:]
        del tempList2[:]
        del tempList3[:]
        del tempList4[:]

    return

def colFlip(col_numb, direction):
    # 1 = Up and -1 = Down
    tempList1 = []
    tempList2 = []
    tempList3 = []
    tempList4 = []
    if(col_numb == 1):
        index = [0,3,6]
    elif(col_numb == 2):
        if(direction == 1):
            colFlip(1,-1)
            colFlip(3,-1)
            swap(0,2)
            swap(1,2)
            swap(2,5)
            return
        else:
            colFlip(1,1)
            colFlip(3,1)
            swap(0,1)
            swap(5,1)
            swap(5,2)
            return
    else:
        index = [2,5,8]
    # If its the first row then we know the first 3 numbers from each array will be altered
    if(direction == 1):
        for x in range(3):
            tempList1.append(cube[0][index[x]])
            tempList2.append(cube[1][index[x]])
            tempList3.append(cube[2][index[x]])
            tempList4.append(cube[5][index[x]])
        # This copies the first 3 numbers of the sides into lists
        y=0
        for x in range(3):
            cube[0][index[x]] = tempList3[y]
            cube[1][index[x]] = tempList1[y]
            cube[2][index[x]] = tempList4[y]
            cube[5][index[x]] = tempList2[y]
            y+=1
        del tempList1[:]
        del tempList2[:]
        del tempList3[:]
        del tempList4[:]
    # Now we do the a similar format for the opposite direction (Left)
    if(direction == -1):
        for x in range(3):
            tempList1.append(cube[0][index[x]])
            tempList2.append(cube[1][index[x]])
            tempList3.append(cube[2][index[x]])
            tempList4.append(cube[5][index[x]])

        # This copies the first 3 numbers of the sides into lists
        y=0
        for x in range(3):
            cube[0][index[x]] = tempList2[y]
            cube[1][index[x]] = tempList4[y]
            cube[2][index[x]] = tempList1[y]
            cube[5][index[x]] = tempList3[y]
            y+=1

        del tempList1[:]
        del tempList2[:]
        del tempList3[:]
        del tempList4[:]

    return

def faceRotate(direction):
    # 1 = Clockwise and -1 = Counter Clockwise
    cubeRotate(1)
    if (direction == 1):    # clockwise
        colFlip(3,1)   
    elif (direction == -1): # counter clockwise
        colFlip(3,-1)
    cubeRotate(-1)          # return to previous orientation


def cubeFlip(direction):
    #1 is up and -1 is down
    if(direction == -1):
        swap(0,1)
        swap(2,1)
        swap(1,5)
        faceSwap(2,0,3)
        faceSwap(5,1,3)
        faceSwap(8,2,3)
        faceSwap(5,3,3)
        faceSwap(8,6,3)
        faceSwap(7,5,3)
        faceSwap(2,0,4)
        faceSwap(5,1,4)
        faceSwap(8,2,4)
        faceSwap(5,3,4)
        faceSwap(8,6,4)
        faceSwap(7,5,4)


    else:
        swap(0,2)
        swap(1,2)
        swap(5,2)
        faceSwap(6,0,3)
        faceSwap(3,1,3)
        faceSwap(6,2,3)
        faceSwap(7,3,3)
        faceSwap(5,7,3)
        faceSwap(8,6,3)
        faceSwap(6,0,4)
        faceSwap(3,1,4)
        faceSwap(6,2,4)
        faceSwap(7,3,4)
        faceSwap(5,7,4)
        faceSwap(8,6,4)


def cubeRotate(direction):
    # 1 = clockwise or to the right and -1 = counter clockwise or to the left
    if(direction == 1):
        swap(3,0)
        swap(5,3)
        swap(4,5)
        # Now we got to fix to coordinates for the indexes on sides [1,2]
        faceSwap(2,0,1)
        faceSwap(5,1,1)
        faceSwap(8,2,1)
        faceSwap(5,3,1)
        faceSwap(8,6,1)
        faceSwap(7,5,1)
        faceSwap(2,0,2)
        faceSwap(5,1,2)
        faceSwap(8,2,2)
        faceSwap(5,3,2)
        faceSwap(8,6,2)
        faceSwap(7,5,2)
    else:
        swap(4,0)
        swap(3,4)
        swap(4,5)

        faceSwap(6,0,1)
        faceSwap(3,1,1)
        faceSwap(6,2,1)
        faceSwap(7,3,1)
        faceSwap(5,7,1)
        faceSwap(8,6,1)
        faceSwap(6,0,2)
        faceSwap(3,1,2)
        faceSwap(6,2,2)
        faceSwap(7,3,2)
        faceSwap(5,7,2)
        faceSwap(8,6,2)
    return

# Swap opposite faces of the cube (useful for 2nd row turn and 2nd col flip)
def swap(start,end):
    cube[start], cube[end] = cube[end], cube[start]
    return
def faceSwap(start,end,side):
    cube[side][start],cube[side][end] = cube[side][end], cube[side][start]
    return
# Function that returns which color is on the center of a passed in side
# The color in the center dictates which color pieces should be on that side
def getCenter(side):
    return cube[side][4]

# Function that returns the other color on the edge cubie.
def getOtherEdgeColor(side, ele):
    if (side == 0):
        if (ele == 1): return cube[1][7]
        elif (ele == 3): return cube[3][5]
        elif (ele == 5): return cube[4][3]
        elif (ele == 7): return cube[2][1]
        else: return 'x'
    elif (side == 1):
        if (ele == 1): return cube[5][1]
        elif (ele == 3): return cube[3][1]
        elif (ele == 5): return cube[4][1]
        elif (ele == 7): return cube[0][1]
        else: return 'x'
    elif (side == 2):
        if (ele == 1): return cube[0][7]
        elif (ele == 3): return cube[3][7]
        elif (ele == 5): return cube[4][7]
        elif (ele == 7): return cube[5][7]
        else: return 'x'
    elif (side == 3):
        if (ele == 1): return cube[1][3]
        elif (ele == 3): return cube[5][5]
        elif (ele == 5): return cube[0][3]
        elif (ele == 7): return cube[2][3]
        else: return 'x'
    elif (side == 4):
        if (ele == 1): return cube[1][5]
        elif (ele == 3): return cube[0][5]
        elif (ele == 5): return cube[5][3]
        elif (ele == 7): return cube[2][5]
        else: return 'x'
    elif (side == 5):
        if (ele == 1): return cube[1][1]
        elif (ele == 3): return cube[4][5]
        elif (ele == 5): return cube[3][3]
        elif (ele == 7): return cube[2][7]
        else: return 'x'
    else: return 'y'

# # Function that returns the other 2 colors on the corner cubie.
def getOtherCornerColors(side, ele):
    if (side == 0):
        if (ele == 0): return [cube[3][2], cube[1][6]]
        elif (ele == 2): return [cube[4][0], cube[1][8]]
        elif (ele == 6): return [cube[3][8], cube[2][0]]
        elif (ele == 8): return [cube[2][2], cube[4][6]]
        else: return ['x','x']
    elif (side == 1):
        if (ele == 0): return [cube[3][0], cube[5][2]]
        elif (ele == 2): return [cube[4][2], cube[5][0]]
        elif (ele == 6): return [cube[3][2], cube[0][0]]
        elif (ele == 8): return [cube[0][2], cube[4][0]]
        else: return ['x','x']
    elif (side == 2):
        if (ele == 0): return [cube[0][6], cube[3][8]]
        elif (ele == 2): return [cube[4][6], cube[0][8]]
        elif (ele == 6): return [cube[3][6], cube[5][8]]
        elif (ele == 8): return [cube[5][6], cube[4][8]]
        else: return ['x','x']
    elif (side == 3):
        if (ele == 0): return [cube[5][2], cube[1][0]]
        elif (ele == 2): return [cube[0][0], cube[1][6]]
        elif (ele == 6): return [cube[2][6], cube[5][8]]
        elif (ele == 8): return [cube[0][6], cube[2][0]]
        else: return ['x','x']
    elif (side == 4):
        if (ele == 0): return [cube[0][2], cube[1][8]]
        elif (ele == 2): return [cube[5][0], cube[1][2]]
        elif (ele == 6): return [cube[0][8], cube[2][2]]
        elif (ele == 8): return [cube[2][8], cube[5][6]]
        else: return ['x','x']
    elif (side == 5):
        if (ele == 0): return [cube[4][2], cube[1][2]]
        elif (ele == 2): return [cube[3][0], cube[1][0]]
        elif (ele == 6): return [cube[2][8], cube[4][8]]
        elif (ele == 8): return [cube[2][6], cube[3][6]]
        else: return ['x','x']
    else: return ['y','y']

# Print a specific side for debugging purposes
# side == (0->front, 1-> top, 2->bottom, 3->left, 4->right, 5->back)
def printSide(side):
    print(cube[side][0] + ' ' + cube[side][1] + ' ' + cube[side][2])
    print(cube[side][3] + ' ' + cube[side][4] + ' ' + cube[side][5])
    print(cube[side][6] + ' ' + cube[side][7] + ' ' + cube[side][8])

def printAllSides():
    print("Front Side")
    printSide(0)    # Front side
    print("======")
    print("Top Side")
    printSide(1)    # Top side
    print("======")
    print("Bottom Side")
    printSide(2)    # Bottom side
    print("======")
    print("Left Side")
    printSide(3)    # Left Side
    print("======")
    print("Right Side")
    printSide(4)    # Right Side
    print("======")
    print("Back Side")
    printSide(5)    # Back Side
    print("======")

# Function to check if the top cross pieces are in the correct places
# This also checks that the centers of the adjacent sides align with the edge piece colors
def checkTopCross ():
    if (cube[0][1] == getCenter(0) and getOtherEdgeColor(0,1) == getCenter(1)) and (cube[0][3] == getCenter(0) and getOtherEdgeColor(0,3) == getCenter(3)) and (cube[0][5] == getCenter(0) and getOtherEdgeColor(0,5) == getCenter(4)) and (cube[0][7] == getCenter(0) and getOtherEdgeColor(0,7) == getCenter(2)):
        return true
    else:
        return false

# def checkTopSide:

#Going Based on this website: https://www.speedcube.com.au/pages/how-to-solve-a-rubiks-cube
#Step 1: Complete First Layer Cross
# Substep A: Keep White Centre on top -  Done
# Substep B: Face Green Centre towards you
# Substep C: Find and Adjust Green/White edge piece
# Substep D: Match situation and add rotations

# Function that returns the side number of the specified color. This is used to orient the cube
def centerSide (side_color):
    for x in range(len(cube)):
        if getCenter(x) == side_color:
            return x
    return 69

# Function to to move the specified side to the top. Accepts side number
def moveTop(side):
    #Top is side 1
    if(side == 0):
        cubeFlip(1)
        return
    elif (side == 1):
        return
    elif (side == 2):
        cubeFlip(1)
        cubeFlip(1)
        return
    elif (side == 3):
        cubeRotate(1)
        cubeFlip(1)
        return
    elif (side == 4):
        cubeRotate(-1)
        cubeFlip(1)
        return
    else :
        cubeFlip(-1)
        return

# Function to to move the specified side to the front. Accepts side number
def moveFront(side):
    #Front is side 0
    if(side == 0):
        return
    elif(side == 3):
        cubeRotate(1)
        return
    elif(side == 4):
        cubeRotate(-1)
        return
    elif(side == 5):
        cubeRotate(1)
        cubeRotate(1)
        return
    return

# side_print = centerSide('W')
# moveTop(side_print)
# print("Side with the white is: ",side_print)
# side_green = centerSide('G')
# moveFront(side_green)
# printAllSides()

# Assuming that the top side is now White and the front side is now Green,
# we want to find the edge piece that is white + green.
# Where can it be? - First we find all the edge pieces that are of the color
# white(color1 variable). Then out of those we find the poition of the one
# that also has the other edge color as green(color 2 variable).
def findSpecifiedEdge(color1, color2):
    # Edges can be at positions [x][1], [x][3], [x][5] and [x][7]. Hence, check these only
    for x in range(len(cube)):
        for y in [1, 3, 5, 7]:
            # Color 2 will be in front and color 1 should be on top. We want it from the perspective
            # color 2
            if cube[x][y] == color2 and getOtherEdgeColor(x,y) == color1:
                return [x,y]

# Now that we know the position of that cube (x,y) that is (side, 0-8), we have to move it to the
# right spot. The right spot is (0, 1) so that color1 is on top and color2 is in front.
# Wishing I had a cube right now..
def moveEdgeToCorrectPosition(side, ele, color1, color2):
    # If the edge is already in the right spot, return
    if (side == 0) and (ele == 1): return
    # Handle cases when it is on the front side(0)
    if (side == 0):
        if (ele == 3):
            # move face clockwise
            faceRotate(1)
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 5):
            # move face counter clockwise
            faceRotate(-1)
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 7):
            # move face clockwise twice
            faceRotate(1)
            faceRotate(1)
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
    # Handle cases when it is on the left side(3)
    elif (side == 3):
        if (ele == 1):
            colFlip(1, -1)
            rowTurn(1,-1)
            colFlip(3,1)
            rowTurn(1,1)
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 3):
            # do moves
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 5):
            rowTurn(1,-1)
            colFlip(3,1)
            rowTurn(1,1)
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 7):
            rowTurn(3, 1)
            # move face clockwise twice
            faceRotate(1)
            faceRotate(1)
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
    # Handle cases when it is on the right side(4)
    elif (side == 4):
        if (ele == 1):
            colFlip(3, -1)
            rowTurn(1, 1)
            colFlip(3, 1)
            rowTurn(1, -1)
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 3):
            rowTurn(1,1)
            colFlip(3,1)
            rowTurn(1,-1)
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 5):
            # do moves
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 7):
            rowTurn(3, -1)
            # move face clockwise twice
            faceRotate(1)
            faceRotate(1)
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
    # Handle cases when it is on the back side(5)
    elif (side == 5):
        if (ele == 1):
            faceRotate(1)
            faceRotate(1)
            rowTurn(3, 1)
            rowTurn(3, 1)
            faceRotate(1)
            faceRotate(1)
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 3):
            # do moves
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 5):
            # do moves
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 7):
            rowTurn(3, 1)
            rowTurn(3, 1)
            # move face clockwise twice
            faceRotate(1)
            faceRotate(1)
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
    # Handle cases when it is on the top side(1)
    elif (side == 1):
        if (ele == 1):
            # do moves
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 3):
            # do moves
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 5):
            # do moves
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 7):
            faceRotate(1)
            rowTurn(1, 1)
            colFlip(3, 1)
            rowTurn(1, -1)
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
    # Handle cases when it is on the bottom side(2)
    elif (side == 2):
        if (ele == 1):
            faceRotate(-1)
            rowTurn(1, 1)
            colFlip(3, 1)
            rowTurn(1, -1)
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 3):
            # do moves
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 5):
            # do moves
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front
        elif (ele == 7):
            # do moves
            recover(color1, color2)     # recover to orientation with color1 on top and color2 in front

# Function to come back to orientation after moves
def recover(colorTop, colorFront):
    moveTop(colorTop)
    moveFront(colorFront)


# side_print = whiteSide();
# print("Side with the white is: ",side_print)
# cubeRotate(1,-1)
# printAllSides()

# colFlip(2,-1)
# rowTurn(2,1)
# printAllSides()
# for x in range(len(cube[0])):
#     print(cube[0][x])

# print(cube[1][1])


#Step #2
#Keep white on Top
#Put green centre piece in Front
#Find green/white/red corner piece
#Move this corner piece to a specific position either bottom right or bottom left corner

#First call - moveTop(centerSide('W'))
#Next call- moveFront(centerSide('G'))

#In this function we want to find the Green/White/Corner piece
#We will do this by looping through the cube and checking only the corner pieces to see what corner colors they match with
#We know the edges possible coordinates are: [0,6,2] (Top left corner) , [2,8,0] (Top right corner), [6,8,0] (bottom left corner), and lastly [8,6,2] (bottom right corner)
#We will call this function with findTripleCorner('G','W','R')
def findTripleCorner(color1,color2,color3):


    for x in range (len(cube)):
         #this is checking so you only go through this logic if one of the corner pieces on the current side is green white or red (later ill relplace with color1 color2 and color3)
        moveFront(x)
        print(x)
        if(cube[x][0] == 'G' or cube[x][0] == 'W' or cube[x][0] ==  'R'  or cube[x][2] == 'G' or cube[x][2] == 'W' or cube[x][2] == 'R' or cube[x][6] == 'G' or cube[x][6] == 'W' or cube[x][6] == 'R'or cube[x][8] == 'G' or cube[x][8] == 'W' or cube[x][8] == 'R'):
                if((cube[1][6] == 'G' or cube[1][6] =='W' or cube[1][6] == 'R') and (cube[3][2] == 'G' or cube[3][2] == 'W' or cube[3][2] == 'R') and (cube[0][0] == 'G' or cube[0][0] == 'W' or cube[0][0] == 'R' )):
                    #return format is coordinate of the triple edge and the last number is the side number
                    return [0,6,2,x]
                elif((cube[1][8] == 'G' or cube[1][8] =='W' or cube[1][8] =='R') and (cube[4][0] == 'G' or cube[4][0] =='W' or cube[4][0] =='R') and (cube[0][2] == 'G' or cube[0][2] =='W' or cube[0][2] =='R' )):
                    return[2,8,0,x]
                elif((cube[3][8] == 'G' or cube[3][8] =='W' or cube[3][8] =='R') and (cube[2][0] == 'G' or cube[2][0] =='W' or cube[2][0] =='R') and (cube[0][6] == 'G' or cube[0][6] =='W' or cube[0][6] =='R' )):
                    return[6,8,0,x]
                elif((cube[4][6] == 'G' or cube[4][6] =='W' or cube[4][6] =='R') and (cube[2][2] == 'G' or cube[2][2] =='W' or cube[2][2] =='R') and (cube[0][8] == 'G' or cube[0][8] =='W' or cube[0][8] =='R' )):
                    return[8,6,2,x]



print(findTripleCorner('G','W','R'))
# print(cube[0][2])
