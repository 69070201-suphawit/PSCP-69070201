"""SurprisingVote"""
sum_score = float(input())
high_score = float(input())
Low_score = max(0, sum_score-(high_score * 2)) # หักคะแนนสูงสุดx2, ไม่ให้ต่ำกว่า 0
if (high_score - Low_score) <= 2 :
    print("Not surprising")
else :
    print("Surprising")
