import random


def children(position, k):
    global branch
    return position * branch + k


def noAlphaBeta(currentPosition, depth_, values_, maximizing):
    global branch
    global noAB
    noAB += 1
    if depth_ == 0:
        return values_[currentPosition]

    if maximizing:
        maxValue = -1000000

        for i in range(branch):

            value = noAlphaBeta(children(currentPosition, i), depth_-1, values_, False)
            
            maxValue = max(value, maxValue)
            

        return maxValue

    else:

        minValue = 1000000

        for i in range(branch):

            value = noAlphaBeta(children(currentPosition, i), depth_-1, values_, True)
            
            minValue = min(value, minValue)
            

        return minValue



def alphaBeta(currentPosition, _depth, _values, _alpha, _beta, maximizing):
    global branch
    global AB 
    AB += 1
    if _depth == 0:
        return _values[currentPosition]

    if maximizing:
        maxValue = _alpha

        for i in range(branch):

            value = alphaBeta(children(currentPosition, i), _depth-1, _values, _alpha, _beta, False)
            maxValue = max(value, maxValue)
            _alpha = max(maxValue, _alpha)

            if _alpha >= _beta:
                break

        return maxValue

    else:

        minValue = _beta

        for i in range(branch):

            value = alphaBeta(children(currentPosition, i), _depth-1, _values, _alpha, _beta, True)
            minValue = min(value, minValue)
            _beta = min(minValue, _beta)

            if _alpha >= _beta:
                break

        return minValue


print()
print('-------I N P U T-------')
print()

turns = int(input('Enter number of turns for Riyad: '))
depth = 2 * turns
branch = int(input('Enter the number of branches per each node: '))
minimum = int(input('Enter the Minimum Value of Leaf Node: '))
maximum = int(input('Enter the Maximum Value of Leaf Node: '))

values = [random.randrange(minimum, maximum) for i in range(branch ** depth)]
alpha = -10000000
beta = 10000000
AB = 0
noAB = 0

noAlphaBeta(0, depth, values, True)

print()
print('-------O U T P U T-------')
print()

print(f'Depth: {depth}')
print(f'Branch: {branch}')
print(f'Terminal States (Leaf Nodes): {branch ** depth}')
print(f'Maximum Amount Collected by Riyad: {alphaBeta(0, depth, values, alpha, beta, True)}')
print(f'Comparisons before Alpha-Beta Pruning: {noAB}')
print(f'Comparisons after Alpha-Beta Pruning: {AB}')

