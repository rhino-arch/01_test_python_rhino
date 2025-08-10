from Grasshopper import DataTree
from Grasshopper.Kernel.Data import GH_Path
from Rhino.Geometry import Point3d

#def createTreee(points, breakP):
    numPath = 0
    newPath = GH_Path(0)
    tree = DataTree[Point3d]()
    
    for num in range(len(points)):
        if num % breakP == 0 and num != 0:
            numPath += 1
            newPath = GH_Path(numPath)
        tree.Add(points[num], newPath)
    return tree


"Toi tao them phan ghi de"