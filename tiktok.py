"""tiktok"""
text = input()
text_split = text.split(" ")
r = int(text_split[0])
x = int(text_split[1])
y = int(text_split[2])
point = (x**2) + (y**2)
radius = r**2
if point < radius :
    print("IN")
if point == radius :
    print('ON')
if point > radius :
    print("OUT")
