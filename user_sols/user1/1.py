#User 1's solution - add multiples of 3, multiples of 5 and then subtract multiples of 15

def main():
    sol = 0
    
    # Add multiples of 3
    i = 1
    while True:
        if (3 * i) < 1000:
            sol += (3 * i)
            i += 1
        else:
            break

    # Add multiples of 5
    i = 1
    while True:
        if (5 * i) < 1000:
            sol += (5 * i)
            i += 1
        else:
            break

    # We've added multiples of 15 twice. Now remove the duplicates
    i = 1
    while True:
        if (15 * i) < 1000:
            sol -= (15 * i)
            i += 1
        else:
            break

    print(sol)

if __name__ == '__main__':
    main()