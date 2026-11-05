# s.strip() is used to remove  both sides extra spaces.
s = "  hello world  "
s2 = s.strip()
print(s2)

#s.lsptrip()is used to remove left side space.
s3 = s.lstrip()
print(s3)
# or
print(f"lstrip : {s3}")

#s.rsptrip() is used to remove right side space.
s4 = s.rstrip()
print(s4)
#or
print(f"s.rstrip : {s4}")


# split() it used for string into list with spliting every word

sp1 = "apple banana is my favourite fruits"
sp2 = sp1.split()
print(sp2)

sp4 = " hello, world"
sp5 = sp4.split(",",1)
sp6 = sp4.split(",",2)
print(sp5)
print(sp4)

#########tuple
