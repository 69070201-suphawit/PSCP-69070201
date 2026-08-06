"""kradathor"""
text = input()
text_split = text.split(" ")
r = float(text_split[0])
h = float(text_split[1])
glue = float(text_split[2])
r_lenght = (2*3.14*r)+glue
wide = h + (2*r)
print(f"{wide:.2f} {r_lenght:.2f}")
