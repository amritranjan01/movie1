def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)
def find_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"The inverse of {a} modulo {m} does not exist.")
    else:
        return x % m

def express_as_linear_sum(numbers):
    n = len(numbers)
    if n == 0:
        return "No numbers provided"
    elif n == 1:
        return numbers[0], (1,)
    elif n == 2:
        gcd_val = gcd(numbers[0], numbers[1])
        x, y = extended_gcd(numbers[0], numbers[1])[1:]
        return gcd_val, (x, y)
    else:
        gcd_val, *coefficients = express_as_linear_sum(numbers[:-1])
        last_number = numbers[-1]
        new_gcd, x, y = extended_gcd(gcd_val, last_number)
        new_coefficients = [c * x for c in coefficients] + [y]
        return new_gcd, tuple(new_coefficients)

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Finding gcd
    gcd_result = gcd(num1, num2)
    print("GCD of", num1, "and", num2, ":", gcd_result)

    # Express gcd as a linear sum
    gcd_linear_sum = express_as_linear_sum([num1, num2])
    print("GCD expressed as a linear sum:", gcd_linear_sum)

    # Finding inverse modulo
    num = int(input("Enter the number to find its inverse: "))
    modulo = int(input("Enter the modulo: "))

    try:
        inverse = find_inverse(num, modulo)
        print("Inverse of", num, "modulo", modulo, ":", inverse)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
