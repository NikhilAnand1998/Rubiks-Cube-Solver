import string;


# side_1 = [];
# side_2 = [];
# side_3 = [];
# side_4 = [];
# side_5 = [];
# side_6 = [];

cube = [['G','G','G','G','G','G','G','G','G'],['O','O','O','O','O','O','O','O','O'],['R','R','R','R','R','R','R','R','R'],['Y','Y','Y','Y','Y','Y','Y','Y','Y'],['W','W','W','W','W','W','W','W','W'],['B','B','B','B','B','B','B','B','B']];

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
    tempList1 = [];
    tempList2 = [];
    tempList3 = [];
    tempList4 = [];
    if(row_numb == 1):
        start = 0;
        end = 3;
    elif(row_numb == 2):
        if(direction == 1):
            rowTurn(1,-1);
            rowTurn(3,-1);
            swap(0,3);
            swap(4,3);
            swap(3,5);
            return;
        else:
            rowTurn(1,1);
            rowTurn(3,1);
            swap(0,4);
            swap(3,4);
            swap(4,5);
            return;
    else:
        start = 6;
        end =9;
    # If its the first row then we know the first 3 numbers from each array will be altered
    if(direction == 1 ) :
        for x in range(start,end):
            tempList1.append(cube[0][x]);
            tempList2.append(cube[3][x]);
            tempList3.append(cube[4][x]);
            tempList4.append(cube[5][x]);
        # This copies the first 3 numbers of the sides into lists
        y=0;
        for x in range(start,end):
            cube[0][x] = tempList2[y];
            cube[3][x] = tempList4[y];
            cube[4][x] = tempList1[y];
            cube[5][x] = tempList3[y];
            y+=1;
        del tempList1[:];
        del tempList2[:];
        del tempList3[:];
        del tempList4[:];
    # Now we do the a similar format for the opposite direction (Left)
    if(direction == -1 ) :
        for x in range(start,end):
            tempList1.append(cube[0][x]);
            tempList2.append(cube[3][x]);
            tempList3.append(cube[4][x]);
            tempList4.append(cube[5][x]);

        # This copies the first 3 numbers of the sides into lists
        y=0;
        for x in range(start,end):
            cube[0][x] = tempList3[y];
            cube[3][x] = tempList1[y];
            cube[4][x] = tempList4[y];
            cube[5][x] = tempList2[y];
            y+=1;

        del tempList1[:];
        del tempList2[:];
        del tempList3[:];
        del tempList4[:];

    return;

def colFlip(col_numb, direction):
    # 1 = Up and -1 = Down
    tempList1 = [];
    tempList2 = [];
    tempList3 = [];
    tempList4 = [];
    if(col_numb == 1):
        index = [0,3,6];
    elif(col_numb == 2):
        if(direction == 1):
            colFlip(1,-1);
            colFlip(3,-1);
            swap(0,2);
            swap(1,2);
            swap(2,5);
            return;
        else:
            colFlip(1,1);
            colFlip(3,1);
            swap(0,1);
            swap(5,1);
            swap(5,2);
            return;
    else:
        index = [2,5,8];
    # If its the first row then we know the first 3 numbers from each array will be altered
    if(direction == 1 ) :
        for x in range(3):
            tempList1.append(cube[0][index[x]]);
            tempList2.append(cube[1][index[x]]);
            tempList3.append(cube[2][index[x]]);
            tempList4.append(cube[5][index[x]]);
        # This copies the first 3 numbers of the sides into lists
        y=0;
        for x in range(3):
            cube[0][index[x]] = tempList3[y];
            cube[1][index[x]] = tempList1[y];
            cube[2][index[x]] = tempList4[y];
            cube[5][index[x]] = tempList2[y];
            y+=1;
        del tempList1[:];
        del tempList2[:];
        del tempList3[:];
        del tempList4[:];
    # Now we do the a similar format for the opposite direction (Left)
    if(direction == -1 ) :
        for x in range(3):
            tempList1.append(cube[0][index[x]]);
            tempList2.append(cube[1][index[x]]);
            tempList3.append(cube[2][index[x]]);
            tempList4.append(cube[5][index[x]]);

        # This copies the first 3 numbers of the sides into lists
        y=0;
        for x in range(3):
            cube[0][index[x]] = tempList2[y];
            cube[1][index[x]] = tempList4[y];
            cube[2][index[x]] = tempList1[y];
            cube[5][index[x]] = tempList3[y];
            y+=1;

        del tempList1[:];
        del tempList2[:];
        del tempList3[:];
        del tempList4[:];

    return;

def swap(start,end):
    cube[start], cube[end] = cube[end], cube[start];
    return;

# rowTurn(2,-1);
# Print a specific side for debugging purposes
# side == (0->front, 3->left, 4->right, 5->back)
def printSide(side):
    print(cube[side][0] + ' ' + cube[side][1] + ' ' + cube[side][2])
    print(cube[side][3] + ' ' + cube[side][4] + ' ' + cube[side][5])
    print(cube[side][6] + ' ' + cube[side][7] + ' ' + cube[side][8])

def printAllSides():
    print("Front Side")
    printSide(0)    # Front side
    print("=====")
    print("Top Side")
    printSide(1)    # Top side?
    print("=====")
    print("Bottom Side")
    printSide(2)    # Bottom side?
    print("=====")
    print("Left Side")
    printSide(3)    # Left Side
    print("=====")
    print("Right Side")
    printSide(4)    # Right Side
    print("=====")
    print("Back Side")
    printSide(5)    # Back Side
    print("=====")

printSide(0)    # Front side
print("=====")
printSide(1)    # Top side?
print("=====")
printSide(2)    # Bottom side?
print("=====")
printSide(3)    # Left Side
print("=====")
printSide(4)    # Right Side
print("=====")
printSide(5)    # Back Side
print("=====")

# colFlip(2,1);
#rowTurn(2,-1);
# for x in range(len(cube[0])):
#     print(cube[0][x]);

# print(cube[1][1]);
