#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    z = max(arr)
    while max(arr) == z:
        arr.remove(max(arr))
    print (max(arr))