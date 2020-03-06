def HanoiSolver(nTimes, firstRod, auxRod, endRod):
    if nTimes == 1:
        print(f'Moving disc 1 from {firstRod} to {endRod}')
    else:
        HanoiSolver(nTimes - 1, firstRod, endRod, auxRod)
        print(f'Move disk {nTimes} from {firstRod} to {endRod}')
        HanoiSolver(nTimes - 1, auxRod, firstRod, endRod)
def Counter(nTimes, mult):
    global counter
    if counter < nTimes:
        counter += 1
        mult = 2 * mult + 1
        Counter(nTimes, mult)
    else:
        print(f'\n#####\nThe best solution takes {mult} steps\n#####\n')
mult = 1
counter = 1
while True:
    print('Welcome to the Tower Of Hanoi solver!')
    print('-------------------------------------')
    print('Option 1: Tower Of Hanoi step by step solution')
    print('Option 2: Steps to complete the given number of discs')
    print('Option 3: Quit')
    userInput = input()
    nTimes = int(input('How many disks are there on tower 1? '))
    if userInput == '1':
        HanoiSolver(nTimes, 'first rod', 'middle rod', 'end rod')
    elif userInput == '2':
        Counter(nTimes, mult)
    else:
        break
