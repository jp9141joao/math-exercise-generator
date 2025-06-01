import time  # Import time module for pauses
import random  # Import random module for generating random numbers
import os  # Import os module to clear the console
import math  # Import math module for mathematical operations

def Addition(quantity, difficulty):
    """
    Function to practice addition problems.
    quantity: number of exercises
    difficulty: difficulty level (1, 2, or 3)
    """
    os.system('cls')  # Clear console (Windows)
    attempts = 0  # Tracks the number of incorrect attempts
    if quantity <= 0:
        print('Invalid quantity!')
        return  # Exit if the quantity is invalid

    if difficulty == 1:
        # Easy level: numbers between 1 and 100
        for i in range(quantity):
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            answer = int(input(f'{i+1}) {x} + {y} = '))
            # Loop until the user provides the correct sum
            while answer != x + y:
                attempts += 1
                print('Incorrect answer!')
                answer = int(input(f'{i+1}) {x} + {y} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 2:
        # Medium level: x between 10 and 1000, y between 10 and 100
        for i in range(quantity):
            x = random.randint(10, 1000)
            y = random.randint(10, 100)
            answer = int(input(f'{i+1}) {x} + {y} = '))
            while answer != x + y:
                attempts += 1
                print('Incorrect answer!')
                answer = int(input(f'{i+1}) {x} + {y} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 3:
        # Hard level: numbers between 1000 and 10000
        for i in range(quantity):
            x = random.randint(1000, 10000)
            y = random.randint(1000, 10000)
            answer = int(input(f'{i+1}) {x} + {y} = '))
            while answer != x + y:
                attempts += 1
                print('Incorrect answer!')
                answer = int(input(f'{i+1}) {x} + {y} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    else:
        print('Invalid difficulty!')

    time.sleep(5)  # Pause for 5 seconds before returning

def Subtraction(quantity, difficulty):
    """
    Function to practice subtraction problems.
    quantity: number of exercises
    difficulty: difficulty level (1, 2, or 3)
    """
    os.system('cls')
    attempts = 0
    if quantity <= 0:
        print('Invalid quantity!')
        return

    if difficulty == 1:
        # Easy level: numbers between 1 and 100
        for i in range(quantity):
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            # Ensure the subtraction result is non-negative by ordering x and y
            if x > y:
                answer = int(input(f'{i+1}) {x} - {y} = '))
                while answer != x - y:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = int(input(f'{i+1}) {x} - {y} = '))
            else:
                answer = int(input(f'{i+1}) {y} - {x} = '))
                while answer != y - x:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = int(input(f'{i+1}) {y} - {x} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 2:
        # Medium level: numbers between 10 and 1000
        for i in range(quantity):
            x = random.randint(10, 1000)
            y = random.randint(10, 1000)
            if x > y:
                answer = int(input(f'{i+1}) {x} - {y} = '))
                while answer != x - y:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = int(input(f'{i+1}) {x} - {y} = '))
            else:
                answer = int(input(f'{i+1}) {y} - {x} = '))
                while answer != y - x:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = int(input(f'{i+1}) {y} - {x} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 3:
        # Hard level: numbers between 1000 and 10000
        for i in range(quantity):
            x = random.randint(1000, 10000)
            y = random.randint(1000, 10000)
            if x > y:
                answer = int(input(f'{i+1}) {x} - {y} = '))
                while answer != x - y:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = int(input(f'{i+1}) {x} - {y} = '))
            else:
                answer = int(input(f'{i+1}) {y} - {x} = '))
                while answer != y - x:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = int(input(f'{i+1}) {y} - {x} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    else:
        print('Invalid difficulty!')

    time.sleep(5)

def Multiplication(quantity, difficulty):
    """
    Function to practice multiplication problems.
    quantity: number of exercises
    difficulty: difficulty level (1, 2, or 3)
    """
    os.system('cls')
    attempts = 0
    if quantity <= 0:
        print('Invalid quantity!')
        return

    if difficulty == 1:
        # Easy level: numbers between 1 and 50
        for i in range(quantity):
            x = random.randint(1, 50)
            y = random.randint(1, 50)
            answer = int(input(f'{i+1}) {x} x {y} = '))
            while answer != x * y:
                attempts += 1
                print('Incorrect answer!')
                answer = int(input(f'{i+1}) {x} x {y} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 2:
        # Medium level: numbers between 10 and 100
        for i in range(quantity):
            x = random.randint(10, 100)
            y = random.randint(10, 100)
            answer = int(input(f'{i+1}) {x} x {y} = '))
            while answer != x * y:
                attempts += 1
                print('Incorrect answer!')
                answer = int(input(f'{i+1}) {x} x {y} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 3:
        # Hard level: numbers between 100 and 1000
        for i in range(quantity):
            x = random.randint(100, 1000)
            y = random.randint(100, 1000)
            answer = int(input(f'{i+1}) {x} x {y} = '))
            while answer != x * y:
                attempts += 1
                print('Incorrect answer!')
                answer = int(input(f'{i+1}) {x} x {y} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    else:
        print('Invalid difficulty!')

    time.sleep(5)

def Division(quantity, difficulty):
    """
    Function to practice division problems.
    quantity: number of exercises
    difficulty: difficulty level (1, 2, or 3)
    """
    os.system('cls')
    attempts = 0
    if quantity <= 0:
        print('Invalid quantity!')
        return

    if difficulty == 1:
        # Easy level: generate divisible pairs; x from 1–100, y from 1–20
        for i in range(quantity):
            x = random.randint(1, 100)
            y = random.randint(1, 20)
            # Ensure x is exactly divisible by y
            while x % y != 0:
                x = random.randint(1, 1000)
                y = random.randint(1, 100)
            answer = float(input(f'{i+1}) {x} / {y} = '))
            while answer != x / y:
                attempts += 1
                print('Incorrect answer!')
                answer = float(input(f'{i+1}) {x} / {y} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 2:
        # Medium level: x and y from 1–100, check to two decimal places
        for i in range(quantity):
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            if x > y:
                answer = float(input(f'{i+1}) {x} / {y} = '))
                while round(answer, 2) != round(x / y, 2):
                    attempts += 1
                    print('Incorrect answer!')
                    answer = float(input(f'{i+1}) {x} / {y} = '))
            else:
                answer = float(input(f'{i+1}) {y} / {x} = '))
                while round(answer, 2) != round(y / x, 2):
                    attempts += 1
                    print('Incorrect answer!')
                    answer = float(input(f'{i+1}) {y} / {x} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 3:
        # Hard level: x and y from 100–1000, check to two decimal places
        for i in range(quantity):
            x = random.randint(100, 1000)
            y = random.randint(100, 1000)
            if x > y:
                answer = float(input(f'{i+1}) {x} / {y} = '))
                while round(answer, 2) != round(x / y, 2):
                    attempts += 1
                    print('Incorrect answer!')
                    answer = float(input(f'{i+1}) {x} / {y} = '))
            else:
                answer = float(input(f'{i+1}) {y} / {x} = '))
                while round(answer, 2) != round(y / x, 2):
                    attempts += 1
                    print('Incorrect answer!')
                    answer = float(input(f'{i+1}) {y} / {x} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    else:
        print('Invalid difficulty!')

    time.sleep(5)

def MatrixSum(quantity, difficulty):
    """
    Function to practice calculating sums of rows and columns in a matrix.
    quantity: number of matrices to generate
    difficulty: difficulty level (1, 2, or 3)
    """
    os.system('cls')
    attempts = 0
    if quantity <= 0:
        print('Invalid quantity!')
        return

    mat = []       # Will hold matrix values
    row_sums = []  # To store sums of each row
    col_sums = []  # To store sums of each column

    if difficulty == 1:
        # Easy level: 5x5 matrix with values 10–99
        for _ in range(quantity):
            mat.clear()
            row_sums.clear()
            col_sums.clear()
            # Build and display the 5x5 matrix
            for i in range(5):
                mat.append([])
                for j in range(5):
                    mat[i].append(random.randint(10, 99))
                    print(f'{mat[i][j]}', end=' ')
                print()
            print()

            # Calculate row sums
            for i in range(5):
                total = 0
                for j in range(5):
                    total += mat[i][j]
                row_sums.append(total)

            # Calculate column sums
            for i in range(5):
                total = 0
                for j in range(5):
                    total += mat[j][i]
                col_sums.append(total)

            # Prompt user to input each row sum
            for i in range(5):
                answer = int(input(f'{i+1}) Enter the sum of row {i+1}: '))
                while answer != row_sums[i]:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = int(input(f'{i+1}) Enter the sum of row {i+1}: '))
                print('Correct answer!')

            # Prompt user to input each column sum
            for i in range(5):
                answer = int(input(f'{i+1}) Enter the sum of column {i+1}: '))
                while answer != col_sums[i]:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = int(input(f'{i+1}) Enter the sum of column {i+1}: '))
                print('Correct answer!')

            print(f'Number of errors: {attempts}')

    elif difficulty == 2:
        # Medium level: 8x8 matrix with values 10–99
        for _ in range(quantity):
            mat.clear()
            row_sums.clear()
            col_sums.clear()
            for i in range(8):
                mat.append([])
                for j in range(8):
                    mat[i].append(random.randint(10, 99))
                    print(f'{mat[i][j]}', end=' ')
                print()
            print()

            # Calculate row sums
            for i in range(8):
                total = 0
                for j in range(8):
                    total += mat[i][j]
                row_sums.append(total)

            # Calculate column sums
            for i in range(8):
                total = 0
                for j in range(8):
                    total += mat[j][i]
                col_sums.append(total)

            # Prompt user for row sums
            for i in range(8):
                answer = int(input(f'{i+1}) Enter the sum of row {i+1}: '))
                while answer != row_sums[i]:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = int(input(f'{i+1}) Enter the sum of row {i+1}: '))
                print('Correct answer!')

            # Prompt user for column sums
            for i in range(8):
                answer = int(input(f'{i+1}) Enter the sum of column {i+1}: '))
                while answer != col_sums[i]:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = int(input(f'{i+1}) Enter the sum of column {i+1}: '))
                print('Correct answer!')

            print(f'Number of errors: {attempts}')

    elif difficulty == 3:
        # Hard level: 8x8 matrix with values 100–999
        for _ in range(quantity):
            mat.clear()
            row_sums.clear()
            col_sums.clear()
            for i in range(8):
                mat.append([])
                for j in range(8):
                    mat[i].append(random.randint(100, 999))
                    print(f'{mat[i][j]}', end=' ')
                print()
            print()

            # Calculate row sums
            for i in range(8):
                total = 0
                for j in range(8):
                    total += mat[i][j]
                row_sums.append(total)

            # Calculate column sums
            for i in range(8):
                total = 0
                for j in range(8):
                    total += mat[j][i]
                col_sums.append(total)

            # Prompt user for row sums
            for i in range(8):
                answer = int(input(f'{i+1}) Enter the sum of row {i+1}: '))
                while answer != row_sums[i]:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = int(input(f'{i+1}) Enter the sum of row {i+1}: '))
                print('Correct answer!')

            # Prompt user for column sums
            for i in range(8):
                answer = int(input(f'{i+1}) Enter the sum of column {i+1}: '))
                while answer != col_sums[i]:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = int(input(f'{i+1}) Enter the sum of column {i+1}: '))
                print('Correct answer!')

            print(f'Number of errors: {attempts}')

    else:
        print('Invalid difficulty!')

    time.sleep(5)

def SquareRoot(quantity, difficulty):
    """
    Function to practice calculating integer square roots.
    quantity: number of exercises
    difficulty: difficulty level (1, 2, or 3)
    """
    os.system('cls')
    attempts = 0
    if quantity <= 0:
        print('Invalid quantity!')
        return

    if difficulty == 1:
        # Easy level: A is 1–50, ensure perfect square
        for i in range(quantity):
            a = random.randint(1, 50)
            while math.sqrt(a) % 1 != 0:
                a = random.randint(1, 50)
            answer = int(input(f'{i+1}) √{a} = '))
            # Use integer square root for comparison
            while answer != math.isqrt(a):
                attempts += 1
                print('Incorrect answer!')
                answer = int(input(f'{i+1}) √{a} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 2:
        # Medium level: A is 10–200, ensure perfect square
        for i in range(quantity):
            a = random.randint(10, 200)
            while math.sqrt(a) % 1 != 0:
                a = random.randint(10, 200)
            answer = int(input(f'{i+1}) √{a} = '))
            while answer != math.isqrt(a):
                attempts += 1
                print('Incorrect answer!')
                answer = int(input(f'{i+1}) √{a} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 3:
        # Hard level: A is 50–1000, ensure perfect square
        for i in range(quantity):
            a = random.randint(50, 1000)
            while math.sqrt(a) % 1 != 0:
                a = random.randint(50, 1000)
            answer = int(input(f'{i+1}) √{a} = '))
            while answer != math.isqrt(a):
                attempts += 1
                print('Incorrect answer!')
                answer = int(input(f'{i+1}) √{a} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    else:
        print('Invalid difficulty!')

    time.sleep(5)

def Exponentiation(quantity, difficulty):
    """
    Function to practice exponentiation (powers).
    quantity: number of exercises
    difficulty: difficulty level (1, 2, or 3)
    """
    os.system('cls')
    attempts = 0
    if quantity <= 0:
        print('Invalid quantity!')
        return

    if difficulty == 1:
        # Easy level: a from 1–50, b from 1–10
        for i in range(quantity):
            a = random.randint(1, 50)
            b = random.randint(1, 10)
            answer = int(input(f'{i+1}) {a} ^ {b} = '))
            while answer != a ** b:
                attempts += 1
                print('Incorrect answer!')
                answer = int(input(f'{i+1}) {a} ^ {b} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 2:
        # Medium level: a from 10–100, b from 5–20
        for i in range(quantity):
            a = random.randint(10, 100)
            b = random.randint(5, 20)
            answer = int(input(f'{i+1}) {a} ^ {b} = '))
            while answer != a ** b:
                attempts += 1
                print('Incorrect answer!')
                answer = int(input(f'{i+1}) {a} ^ {b} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 3:
        # Hard level: a from 10–500, b from 10–30
        for i in range(quantity):
            a = random.randint(10, 500)
            b = random.randint(10, 30)
            answer = int(input(f'{i+1}) {a} ^ {b} = '))
            while answer != a ** b:
                attempts += 1
                print('Incorrect answer!')
                answer = int(input(f'{i+1}) {a} ^ {b} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    else:
        print('Invalid difficulty!')

    time.sleep(5)

def Factorial(quantity, difficulty):
    """
    Function to practice factorial calculations.
    quantity: number of exercises
    difficulty: difficulty level (1, 2, or 3)
    """
    os.system('cls')
    attempts = 0
    if quantity <= 0:
        print('Invalid quantity!')
        return

    if difficulty == 1:
        # Easy level: a from 1–10
        for i in range(quantity):
            a = random.randint(1, 10)
            answer = int(input(f'{i+1}) {a}! = '))
            result = math.factorial(a)  # Compute factorial
            while answer != result:
                attempts += 1
                print('Incorrect answer!')
                answer = int(input(f'{i+1}) {a}! = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 2:
        # Medium level: a from 5–12
        for i in range(quantity):
            a = random.randint(5, 12)
            answer = int(input(f'{i+1}) {a}! = '))
            result = math.factorial(a)
            while answer != result:
                attempts += 1
                print('Incorrect answer!')
                answer = int(input(f'{i+1}) {a}! = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 3:
        # Hard level: a from 8–15
        for i in range(quantity):
            a = random.randint(8, 15)
            answer = int(input(f'{i+1}) {a}! = '))
            result = math.factorial(a)
            while answer != result:
                attempts += 1
                print('Incorrect answer!')
                answer = int(input(f'{i+1}) {a}! = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    else:
        print('Invalid difficulty!')

    time.sleep(5)

def LinearEquation(quantity, difficulty):
    """
    Function to practice solving first-degree linear equations (ax ± b = 0).
    quantity: number of exercises
    difficulty: difficulty level (1, 2, or 3)
    """
    os.system('cls')
    attempts = 0
    if quantity <= 0:
        print('Invalid quantity!')
        return

    if difficulty == 1:
        # Easy level: a and b are even, a from 1–10, b from 1–20
        for i in range(quantity):
            while True:
                a = random.randint(1, 10)
                b = random.randint(1, 20)
                if a % 2 == 0 and b % 2 == 0:
                    break  # Ensure both a and b are even
            option = random.randint(1, 2)  # Choose between ax + b or ax - b
            if option == 1:
                answer = float(input(f'{i+1}) {a}x + {b} = '))
                result = round((-b) / a, 2)
                while answer != result:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = float(input(f'{i+1}) {a}x + {b} = '))
            else:
                answer = float(input(f'{i+1}) {a}x - {b} = '))
                result = round(b / a, 2)
                while answer != result:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = float(input(f'{i+1}) {a}x - {b} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 2:
        # Medium level: same constraints on a and b
        for i in range(quantity):
            while True:
                a = random.randint(1, 10)
                b = random.randint(1, 20)
                if a % 2 == 0 and b % 2 == 0:
                    break
            option = random.randint(1, 2)
            if option == 1:
                answer = float(input(f'{i+1}) {a}x + {b} = '))
                result = round((-b) / a, 2)
                while answer != result:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = float(input(f'{i+1}) {a}x + {b} = '))
            else:
                answer = float(input(f'{i+1}) {a}x - {b} = '))
                result = round(b / a, 2)
                while answer != result:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = float(input(f'{i+1}) {a}x - {b} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    elif difficulty == 3:
        # Hard level: same constraints on a and b
        for i in range(quantity):
            while True:
                a = random.randint(1, 10)
                b = random.randint(1, 20)
                if a % 2 == 0 and b % 2 == 0:
                    break
            option = random.randint(1, 2)
            if option == 1:
                answer = float(input(f'{i+1}) {a}x + {b} = '))
                result = round((-b) / a, 2)
                while answer != result:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = float(input(f'{i+1}) {a}x + {b} = '))
            else:
                answer = float(input(f'{i+1}) {a}x - {b} = '))
                result = round(b / a, 2)
                while answer != result:
                    attempts += 1
                    print('Incorrect answer!')
                    answer = float(input(f'{i+1}) {a}x - {b} = '))
            print('Correct answer!')
        print(f'Number of errors: {attempts}')

    else:
        print('Invalid difficulty!')

    time.sleep(5)

# Main program loop displaying the menu and handling user selection
while True:
    os.system('cls')
    option = int(input(
        '*Option Menu*\n'
        '1- Practice Addition\n'
        '2- Practice Subtraction\n'
        '3- Practice Multiplication\n'
        '4- Practice Division\n'
        '5- Practice Matrix Sum\n'
        '6- Practice Square Root\n'
        '7- Practice Exponentiation\n'
        '8- Practice Factorial\n'
        '9- Practice Linear Equation\n'
        '10- Print Exercise List\n'
        '11- Exit\n'
        'R: '
    ))

    if option == 11:
        print('Program terminated!')
        break  # Exit the loop and end program
    elif option > 11 or option <= 0:
        os.system('cls')
        print('Invalid option!')
        time.sleep(2)
        continue  # Restart loop if option is invalid

    os.system('cls')
    quantity = int(input('How many exercises do you want to do? '))
    os.system('cls')
    difficulty = int(input('Select difficulty level:\n1- Easy\n2- Medium\n3- Hard\nR: '))

    # Call the corresponding function based on user choice
    if option == 1:
        Addition(quantity, difficulty)
    elif option == 2:
        Subtraction(quantity, difficulty)
    elif option == 3:
        Multiplication(quantity, difficulty)
    elif option == 4:
        Division(quantity, difficulty)
    elif option == 5:
        MatrixSum(quantity, difficulty)
    elif option == 6:
        SquareRoot(quantity, difficulty)
    elif option == 7:
        Exponentiation(quantity, difficulty)
    elif option == 8:
        Factorial(quantity, difficulty)
    elif option == 9:
        LinearEquation(quantity, difficulty)
    elif option == 10:
        ListExercises(quantity, difficulty)  # Assumes ListExercises is defined elsewhere
