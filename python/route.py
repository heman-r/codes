# A person is stading in a town where all the roads and corssings are squares.
# You are given an input of directions and you need to figure out whether the person returns to his
# original position or not
# Sample input = ['n', 's', 'e', 'w']


num = input('Enter no of routes: ');
print('Enter the routes');
routes = [];

for i in range(int(num)):
    routes.append(input());

pos = [0, 0];

def north(pos):
    pos[0] += 1;
    return pos;

def south(pos):
    pos[0] -= 1;
    return pos;

def east(pos):
    pos[1] += 1;
    return pos;

def west(pos):
    pos[1] -= 1;
    return pos;

switcher = {'n': north, 's': south, 'e': east, 'w': west};

for i in routes:    
    try:
        switcher[i](pos);
    except :
        print('There is a unknown direction: ', i);

notOriginalPos = False;

for i in pos:
    if i != 0:
        notOriginalPos = True;

if notOriginalPos:
    print('Person have chaged the position!!');
else:
    print('Sucess person returns to original position for this route string');

