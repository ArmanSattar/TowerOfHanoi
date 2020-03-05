def HanoiSolver(nTimes, firstRod, auxRod, endRod):
    if nTimes == 1:
        rodThree.insert(0, rodOne[0]);rodOne.pop(0)
        print(f'Moving disc 1 from {firstRod} to {endRod}')
    else:
        HanoiSolver(nTimes - 1, firstRod, endRod, auxRod)
        print(f'Move disk {nTimes} from {firstRod} to {endRod}')
        HanoiSolver(nTimes - 1, auxRod, firstRod, endRod)

nTimes = int(input('How many disks are there on tower 1? '))

rodOne = []
rodTwo = []
rodThree = []
x = 1

while x < nTimes + 1:
    rodOne.append(x)
    x += 1
for n in rodThree:
    print(n)
for n in rodOne:
    print(n)
for n in rodTwo:
    print(n)
HanoiSolver(nTimes, 'first rod', 'middle rod', 'end rod')
