#Challenge: Given an array of positions like Left, Right, forward, backward.
#A person moves according to these directions. Check and find whether after a set of directions,
#he comes back to his original position.

# Input = [n, s, l, r]


from operator import add

num = int(input('Enter num of routes'));
routes = [];
print('Enter the routes: ');

for i in range(num):
    routes.append(input());

print('Routes are : ', routes);

initalPos = [0, 0];

rotationVal = [[0,1], [-1, 0], [0, -1], [1, 0]];

def rotate(array, n):
    return array[n:] + array[:n]

def moveForward(pos, rot):
    global initalPos
    print('The initail positin is: ', pos)
    initalPos = list(map(add, pos, rot[0]))

def moveLeft(pos, rot):
    global initalPos
    global rotationVal
    initalPos = list(map(add, pos, rot[1]))
    rotationVal = rotate(rot, 1)

def moveBackward(pos, rot):
    global  initalPos
    global rotationVal
    initalPos = list(map(add, pos, rot[2]))
    rotationVal = rotate(rot, 2)

def moveRight(pos, rot):
    global initalPos
    global rotationVal
    initalPos = list(map(add, pos, rot[3]))
    rotationVal = rotate(rot, -1)

routeDic = {'n': moveForward, 'l': moveLeft, 's': moveBackward, 'r': moveRight}


for route in routes:
    try:
        routeDic[route](initalPos, rotationVal);
    except:
        print('There is an unknown direction', route)

posChange = False

for pos in initalPos:
    if (pos != 0 ):
        posChange = True

if posChange:
    print('Posistion has been changed: ', initalPos)
else: 
    print('No change in position: ')


