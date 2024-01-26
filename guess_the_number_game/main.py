import sys
import random


def askAnswer(randomNum):
    maxTry = 3
    for x in range(maxTry):
        print('You only have ', (maxTry - x), 'times try')
        sys.stdout.buffer.write(b'guess number: ')
        sys.stdout.flush()
        guessNum = sys.stdin.buffer.readline()

        if randomNum == int(guessNum):
            return True


    return False



def main():
    sys.stdout.buffer.write(b'Max number: ')
    sys.stdout.flush()
    maxNum = sys.stdin.buffer.readline()

    sys.stdout.buffer.write(b'Min number: ')
    sys.stdout.flush()
    minNum = sys.stdin.buffer.readline()

    maxNum = int(maxNum)
    minNum = int(minNum)

    if maxNum < minNum:
        print('max number should be higher or equal')
        return 
    
    randomNum = random.randrange(minNum, maxNum)

    isAnswer = askAnswer(int(randomNum))

    if isAnswer:
        print('Congrats')
    else:
        print("fuck off, answer was ", randomNum)

main()

    
 
    
