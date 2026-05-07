def print_formatted(n):
    wid=len(f"{n:b}")
    for i in range(1,n+1):
        print(f"{i:>{wid}d} {i:>{wid}o} {i:>{wid}X} {i:>{wid}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)