#User 2's solution - iterate through all numbers up to 1000, checking for divisibility by 3 or 5

def main():
    sol = 0
    
    for i in xrange(1000):
        if not(i%3) or not(i%5):
            sol += i

    print(sol)

if __name__ == '__main__':
    main()