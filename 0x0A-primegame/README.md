# 0x0A. Prime Game

For this project, you will need to leverage your understanding of prime numbers, game theory, and algorithm optimization to solve a competitive game scenario. The challenge involves determining the winner of a game based on the strategic removal of prime numbers and their multiples from a set of consecutive integers.

## Concepts Needed

### Prime Numbers
- **Understanding Prime Numbers**: Learn what prime numbers are.
- **Efficient Prime Identification**: Utilize algorithms to identify prime numbers within a range.

### Sieve of Eratosthenes
- **Efficient Prime Finding**: Implement the Sieve of Eratosthenes algorithm to find all prime numbers up to a given limit.

### Game Theory
- **Competitive Game Dynamics**: Explore basic principles of competitive games where players take turns.
- **Optimal Play**: Understand win conditions and strategies that lead to a win or loss.

### Dynamic Programming/Memoization
- **Optimization Techniques**: Use dynamic programming or memoization to speed up future calculations by leveraging previous results.

### Python Programming
- **Implementing Game Logic**: Utilize loops and conditional statements to implement the game's logic.
- **Data Structures**: Work with arrays and lists to store integers and track removed numbers.

## Resources

### Prime Numbers and Sieve of Eratosthenes
- **Khan Academy: Prime Numbers**: [Introduction to prime numbers](https://www.khanacademy.org/math/cc-fourth-grade-math/imp-factors-multiples-and-patterns/imp-prime-and-composite-numbers/v/prime-numbers)
- **Sieve of Eratosthenes in Python**: [Step-by-step guide to implementing the sieve algorithm in Python](https://geeksforgeeks.org/sieve-of-eratosthenes/)

### Game Theory Basics
- **Game Theory Introduction**: [Simple explanation of game theory and strategic decision-making](https://www.investopedia.com/terms/g/gametheory.asp)

### Dynamic Programming
- **What Is Dynamic Programming With Python Examples**: [Introduction to dynamic programming with Python examples](https://skerritt.blog/dynamic-programming/)

### Python Official Documentation
- **Python Lists**: [Managing lists in Python](https://docs.python.org/3/tutorial/introduction.html#lists)

## Task

### 0. Prime Game

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

#### Prototype:
```python
def isWinner(x, nums)
x: Number of rounds
nums: Array of n values
Return:
name of the player that won the most rounds
None if the winner cannot be determined
Constraints:
n and x will not be larger than 10,000
No imports allowed
Example:
python
Copy code
x = 3, nums = [4, 5, 1]

# First round: 4
# Maria picks 2 and removes 2, 4, leaving 1, 3
# Ben picks 3 and removes 3, leaving 1
# Ben wins because there are no prime numbers left for Maria to choose

# Second round: 5
# Maria picks 2 and removes 2, 4, leaving 1, 3, 5
# Ben picks 3 and removes 3, leaving 1, 5
# Maria picks 5 and removes 5, leaving 1
# Maria wins because there are no prime numbers left for Ben to choose

# Third round: 1
# Ben wins because there are no prime numbers for Maria to choose

# Result: Ben has the most wins
