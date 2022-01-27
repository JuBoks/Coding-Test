from re import I
import sys

def solution():
    ppl = int(input())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.reverse()
    dp = [1 for _ in range(ppl)]

    for idx1 in range(1, ppl):
        val_now = arr[idx1]
        val_max = 1
        for idx_before in range(idx1):
            if arr[idx_before] < val_now:
                val_next = dp[idx_before] + 1
                if val_max < val_next:
                    val_max = val_next
        
        dp[idx1] = val_max

    print(ppl - max(dp))


solution()