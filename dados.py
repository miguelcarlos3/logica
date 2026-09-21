liguangem = ["Python","C++","Java","Rust","SQL","Lua"]
liguangem.sort ()

liguangem = ["Python","C++","Java","Rust","SQL","Lua"]
liguangem.sort (reverse=True)

liguangem = ["Python","C++","Java","Rust","SQL","Lua"]
liguangem.sort (key=lambda x: len(x))

liguangem = ["Python","C++","Java","Rust","SQL","Lua"]
liguangem.sort (key=lambda x: len(x), reverse= True)


print (liguangem)
print (liguangem.sort (key=lambda x: len(x), reverse= True))
print (liguangem.sort ())


