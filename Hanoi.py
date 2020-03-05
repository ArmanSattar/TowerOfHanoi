def HanoiSolver(nTimes, firstRod, auxRod, endRod):
    if nTimes == 1:
        print(f'Moving disc 1 from {firstRod} to {endRod}')
    else:
        HanoiSolver(nTimes - 1, firstRod, endRod, auxRod)
        print(f'Move disk {nTimes} from {firstRod} to {endRod}')
        HanoiSolver(nTimes - 1, auxRod, firstRod, endRod)

nTimes = int(input('How many disks are there on tower 1? '))
HanoiSolver(nTimes, 'first rod', 'middle rod', 'end rod')
