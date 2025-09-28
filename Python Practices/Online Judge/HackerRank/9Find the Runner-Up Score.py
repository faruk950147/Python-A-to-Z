# def find_runner_up_score(arr):
#     max_score = max(arr)
#     while max_score in arr:
#         arr.remove(max_score)
#     return max(arr)

# another way to find the runner-up score
# def find_runner_up_score(arr):
#     return sorted(set(arr))[-2]

# def find_runner_up_score(arr):
#     return sorted(set(arr), reverse=True)[1]


# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = find_runner_up_score(arr)
#     print(result)


# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))

#     max_score = max(arr)
#     while max_score in arr:
#         arr.remove(max_score)
    
#     runner_up_score = max(arr)
#     print(runner_up_score)
    
# another way to find the runner-up score
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = sorted(set(arr))[-2]
#     print(result)
    
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = sorted(set(arr), reverse=True)[1]
#     print(result)