"""
Part 1
The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, 
you need to find the intersection point closest to the central port. 
Because the wires are on a grid, use the Manhattan distance for this measurement.

Part 2

"""


def load_file(filename):
    """Loads a file to a list

    Parameters:
    filename (string): the name of the file containing input on a
    single line

    Returns: 
    a (list) of lists
    """
    inputList = []
    print("Loading list from file...") 
    with open(filename) as file:
        lines = [line.strip('\n') for line in file]
        inputList = [line.split(',') for line in lines]

    return inputList

def partOne():
    """
    """

    input = [
        ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
        ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
    ]

    # input = [
    #     ['R8', 'U5', 'L5', 'D3'],
    #     ['U7','R6','D4','L4']
    # ]

    #input = load_file('input.txt')

    class Wire(object):
        """
        """
        def __init__(self, name, directionList):
            """
            """
            self.name = name
            self.directionList = directionList
            self.coordList = [[0,0]]
            self.xlist = [0]
            self.ylist = [0]
            self.x = 0
            self.y = 0

        def get_directionList(self):
            """
            """
            return self.directionList.copy()
        
        def numDirections(self):
            """
            """
            return len(self.directionList)
        
        def get_x(self):
            """
            """
            return self.x

        def get_y(self):
            """
            """
            return self.y
        
        def get_xlist(self):
            """
            """
            return self.xlist
        
        def get_ylist(self):
            """
            """
            return self.ylist

        def set_x(self, newx):
            """
            """
            self.x = newx
            
        def set_y(self, newy):
            """
            """
            self.y = newy

        def calculateCoord(self, direc, value):
            """
            """
            if direc == 'R':
                for i in range(int(value)):
                    self.xlist.append(self.get_x() + (i+1))
                    self.ylist.append(self.get_y())
                self.set_x(self.get_x() + int(value))

            elif direc == 'L':
                for i in range(int(value)):
                    self.xlist.append(self.get_x() - (i+1))
                    self.ylist.append(self.get_y())
                self.set_x(self.get_x() - int(value))

            elif direc == 'U':
                for i in range(int(value)):
                    self.ylist.append(self.get_y() + (i+1))
                    self.xlist.append(self.get_x())
                self.set_y(self.get_y() + int(value))

            else:  # == 'D'
                for i in range(int(value)):
                    self.ylist.append(self.get_y() - (i+1))
                    self.xlist.append(self.get_x())
                self.set_y(self.get_y() - int(value))

            self.coordList.append([self.get_x(), self.get_y()])

        def __str__(self):
            return "name: {} \ndirections: {}".format(self.name, self.directionList)

    wireTrace1 = []
    wireTrace2 = []
    dist = 0
    shortestdist = 0

    print("Building wire objects...")
    Wire1 = Wire("wire1", input[0])
    Wire2 = Wire("wire2", input[1])

    print("Calculating coordinates...")
    for i in range(Wire1.numDirections()):
        Wire1.calculateCoord(Wire1.get_directionList()[i][:1],
                                Wire1.get_directionList()[i][1:])
    for i in range(Wire2.numDirections()):
        Wire2.calculateCoord(Wire2.get_directionList()[i][:1],
                                Wire2.get_directionList()[i][1:])

    print("Building trace lists...")    
    wireTrace1 = [ "{},{}".format(Wire1.get_xlist()[i], Wire1.get_ylist()[i]) for i in range(len(Wire1.get_xlist())) ]
    wireTrace2 = [ "{},{}".format(Wire2.get_xlist()[i], Wire2.get_ylist()[i]) for i in range(len(Wire2.get_xlist())) ]

    print("Checking for intersections...")
    for coord in wireTrace1:
        if coord in wireTrace2:
            if coord != '0,0':
                #print("found an intersection")
                #print(coord)
                dist = abs(int(coord.split(',')[0])) + abs(int(coord.split(',')[1]))
                #print(dist)
                if shortestdist != 0:
                    if dist < shortestdist:
                        shortestdist = dist
                else:
                    shortestdist = dist
    
    print("Done")
    print(shortestdist)

def partTwo():
    """
    """

    # input = [
    #     ['R8', 'U5', 'L5', 'D3'],
    #     ['U7','R6','D4','L4']
    # ]

    # input = [
    #     ['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
    #     ['U62','R66','U55','R34','D71','R55','D58','R83']
    # ]

    # input = [
    #     ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
    #     ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
    # ]

    input = load_file('input.txt')

    class Wire(object):
        """
        """
        def __init__(self, name, directionList):
            """
            """
            self.name = name
            self.directionList = directionList
            self.coordList = [[0,0]]
            self.xdist = 0
            self.ydist = 0
            self.traceList = ["0,0"]
            self.x = 0
            self.y = 0
            self.intersecs = []

        def get_directionList(self):
            """
            """
            return self.directionList.copy()
        
        def numDirections(self):
            """
            """
            return len(self.directionList)
        
        def get_x(self):
            """
            """
            return self.x

        def get_y(self):
            """
            """
            return self.y
        
        def get_xdist(self):
            """
            """
            return self.xdist
        
        def get_ydist(self):
            """
            """
            return self.ydist
        
        def get_traceList(self):
            """
            """
            return self.traceList
        
        def get_numtraceList(self):
            """
            """
            return len(self.get_traceList())

        def set_x(self, newx):
            """
            """
            self.x = newx
            
        def set_y(self, newy):
            """
            """
            self.y = newy

        def calculateCoord(self, direc, value):
            """
            """
            if direc == 'R':
                for i in range(int(value)):
                    #self.xdist += 1
                    self.traceList.append("{},{}".format(self.get_x() + (i+1), self.get_y()))
                self.set_x(self.get_x() + int(value))

            elif direc == 'L':
                for i in range(int(value)):
                    #self.xdist += 1
                    self.traceList.append("{},{}".format(self.get_x() - (i+1), self.get_y()))
                self.set_x(self.get_x() - int(value))

            elif direc == 'U':
                for i in range(int(value)):
                    #self.ydist += 1
                    self.traceList.append("{},{}".format(self.get_x(), self.get_y() + (i+1)))
                self.set_y(self.get_y() + int(value))

            else:  # == 'D'
                for i in range(int(value)):
                    #self.ydist += 1
                    self.traceList.append("{},{}".format(self.get_x(), self.get_y() - (i+1)))
                self.set_y(self.get_y() - int(value))

            self.coordList.append([self.get_x(), self.get_y()])
            
        def __str__(self):
            return "name: {} \ndirections: {}".format(self.name, self.directionList)


    

    def checkintersetc(wireObject1_iter, wireObject2):
        """
        """
        intersects = {}
        for i in range(len(wireObject1_iter.get_traceList())):
            if wireObject1_iter.get_traceList()[i] in wireObject2.get_traceList():
                if wireObject1_iter.get_traceList()[i] not in intersects:
                    #print("Found intersection at", wireObject1_iter.get_traceList()[i])
                    #print("Length along Wire is:", i)
                    intersects[wireObject1_iter.get_traceList()[i]] = i
                    
        intersects.pop("0,0")
        return intersects


    print("Building wire objects...")
    Wire1 = Wire("wire1", input[0])
    Wire2 = Wire("wire2", input[1])

    print("Calculating coordinates and building first wire trace list...")
    for i in range(Wire1.numDirections()):
        Wire1.calculateCoord(Wire1.get_directionList()[i][:1],
                                Wire1.get_directionList()[i][1:])

    print("Calculating coordinates and building second wire trace list...")    
    for i in range(Wire2.numDirections()):
        Wire2.calculateCoord(Wire2.get_directionList()[i][:1],
                                Wire2.get_directionList()[i][1:])
               
    wire1_intersects = checkintersetc(Wire1, Wire2)
    wire2_intersects = checkintersetc(Wire2, Wire1)
    #print(wire1_intersects)
    #print(wire2_intersects)

    dist = []
    for key in wire1_intersects.keys():
        dist.append(wire1_intersects[key] + wire2_intersects[key])
    
    print(min(dist))
    print("Done")


#partOne()
partTwo()




        
    
