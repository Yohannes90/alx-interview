#!/usr/bin/python3
'''Prime Game'''


def isWinner(rounds, nums):
    '''Determines the winner of the game based on multiple rounds.'''
    # Initialize the winner count
    winner_count = {'Maria': 0, 'Ben': 0}

    # Iterate through each round
    for n in nums:
        winner = findRoundWinner(n)
        if winner:
            winner_count[winner] += 1

    # Determine the overall winner
    if winner_count['Maria'] > winner_count['Ben']:
        return 'Maria'
    elif winner_count['Ben'] > winner_count['Maria']:
        return 'Ben'
    else:
        return None


def findRoundWinner(n):
    '''Determines the winner of a single round based on the number n.'''
    numbers = list(range(1, n + 1))
    players = ['Maria', 'Ben']

    for i in range(n):
        current_player = players[i % 2]
        selected_indexes = []
        prime = None

        for idx, num in enumerate(numbers):
            if prime is not None:
                if num % prime == 0:
                    selected_indexes.append(idx)
            else:
                if isPrime(num):
                    selected_indexes.append(idx)
                    prime = num

        if prime is None:
            return players[1 - (i % 2)]  # Return the opponent's name

        # Remove selected numbers from the list
        for idx in reversed(selected_indexes):
            numbers.pop(idx)

    return None


def isPrime(n):
    '''Checks if a number is prime.'''
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
