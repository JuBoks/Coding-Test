import imp


import sys

def solution():
  cases = int(input())
  for _ in range(cases):
    ppl = int(input())
    ppl_list = map(int, sys.stdin.readline().rstrip().split())
    
    
    nums = int(input())
    for __ in range(nums):
      x, y = map(int, sys.stdin.readline().rstrip().split())

solution()