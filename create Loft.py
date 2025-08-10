
import ghpythonlib.components as ghcom

# Find Amount of Branches
branchCount = points.BranchCount
#branchList = points.Branch(0)

crvs = []

for lst in range(branchCount):
    lstPoints = points.Branch(lst)
    crv = ghcom.NurbsCurve(lstPoints, 3, False)
    crvs.append(crv.curve)

loft = ghcom.Loft(crvs)

a = loft