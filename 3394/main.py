"""sendto"""
n, s = map(int, input().split())
next_node = [0] * (n + 1)
for i in range(1, n + 1):
    next_node[i] = int(input())
visited = [False] * (n + 1)
count = 0
curr = s
while curr and not visited[curr]:
    visited[curr] = True
    count += 1
    curr = next_node[curr]
print(count)
