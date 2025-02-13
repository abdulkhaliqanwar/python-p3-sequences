def print_fibonacci(length):
    fib_sequence = [0, 1]

    if length == 0:
        print([])  # ✅ Print instead of returning
        return
    elif length == 1:
        print([0])  # ✅ Print instead of returning
        return
    elif length == 2:
        print(fib_sequence)  # ✅ Print instead of returning
        return

    while len(fib_sequence) < length:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    print(fib_sequence)  # ✅ Print the final list instead of returning it




