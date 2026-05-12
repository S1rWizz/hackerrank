#https://www.hackerrank.com/challenges/py-introduction-to-sets


def average(array):
    s1=list(set(array))
    n=len(s1)
    return sum(s1)/n
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)