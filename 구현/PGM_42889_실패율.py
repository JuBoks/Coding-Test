def solution(N, stages):
    answer = []
    num_of_ppl = len(stages)
    stages_arr = [0 for _ in range(N+2)]
    ppl_remain_arr = [0 for _ in range(N+1)]
    
    for ppl in range(num_of_ppl):
        stage_name = stages[ppl]
        stages_arr[stage_name] += 1
    
    ppl_remain_arr[1] = num_of_ppl
    for stage in range(2, N+1):
        ppl_remain_arr[stage] = ppl_remain_arr[stage-1] - stages_arr[stage-1]
    
    rate_arr = []
    for idx in range(1, N+1):
        if ppl_remain_arr[idx] > 0:
            value = stages_arr[idx] * 100 / ppl_remain_arr[idx]
        else:
            value = 0
        rate_arr.append((idx, value))
    
    arr = sorted(rate_arr, key = lambda x: -x[1])
    
    for elm in arr:
        answer.append(elm[0])
        
    return answer