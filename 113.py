"""113"""
st = []
for c in input().strip():
    st.append(c)
    if st[-3:] == ["1", "1", "3"]:
        del st[-3:]
print("".join(st))
