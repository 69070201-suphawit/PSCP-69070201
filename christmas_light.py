"""christmasslight"""
text = input().split(" ")
colour = text[0]
amount = int(text[1])
colours = ['R', 'G', 'B']
full_names = {
    'R': 'Red',
    'G': 'Green',
    'B': 'Blue'
}
start_index = colours.index(colour)
result = []
for i in range(amount):
    current_index = (start_index + i) % 3
    short_name = colours[current_index]
    result.append(full_names[short_name])
print(" ".join(result))
