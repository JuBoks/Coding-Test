def solution_before(answers):
  answer = []
  p1 = [1, 2, 3, 4, 5]
  p2 = [2, 1, 2, 3, 2, 4, 2, 5]
  p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  
  # 1. score 를 배열로 관리
  score1 = 0
  score2 = 0
  score3 = 0
  
  for i in range(len(answers)):
      i1 = i % 5
      i2 = i % 8
      i3 = i % 10
      if answers[i] == p1[i1]:
          score1 += 1
      if answers[i] == p2[i2]:
          score2 += 1
      if answers[i] == p3[i3]:
          score3 += 1
          
  # 2. enumberate 를 for 를 사용하여 루프돌기
  scores = [score1, score2, score3]
  max_score = max(scores)
  scores = list(enumerate(scores, start=1))
  scores = list(filter(lambda x: x[1] == max_score, scores))
  scores.sort(key=lambda x: x[1])
  answer = list(map(lambda x: x[0], scores))

  return answer
  
def solution(answers):
  answer = []
  p1 = [1, 2, 3, 4, 5]
  p2 = [2, 1, 2, 3, 2, 4, 2, 5]
  p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  scores = [0, 0, 0]
  
  for i in range(len(answers)):
      i1 = i % 5
      i2 = i % 8
      i3 = i % 10
      if answers[i] == p1[i1]:
          scores[0] += 1
      if answers[i] == p2[i2]:
          scores[1] += 1
      if answers[i] == p3[i3]:
          scores[2] += 1
          
  # 2. enumberate 를 for 를 사용하여 루프돌기
  max_score = max(scores)
  for idx, score in enumerate(scores):
    if score == max_score:
      answer.append(idx+1)
  
  # scores = [score1, score2, score3]
  # max_score = max(scores)
  # scores = list(enumerate(scores, start=1))
  # scores = list(filter(lambda x: x[1] == max_score, scores))
  # scores.sort(key=lambda x: x[1])
  # answer = list(map(lambda x: x[0], scores))

  return answer

# ipt = [1, 3, 2, 4, 2]
ipt = [1, 2, 3, 4, 5]
print(solution(ipt))