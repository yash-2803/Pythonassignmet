n=int(input())
score=map(int,input().split())
score=list(set(score))
score.remove(max(score))
print(max(score))
