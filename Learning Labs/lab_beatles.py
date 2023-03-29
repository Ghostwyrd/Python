# step 1
beatles = []
beatles_main = ["John Lennon", "Paul McCartney", "George Harrison"]
beatles_aux = ["Stu Sutcliffe", "Pete Best", "Ringo Starr"]
print("Step 1:", beatles)


# step 2
for b in range(3):
    beatles.append(beatles_main[b])
print("Step 2:", beatles)

# step 3
for b in range(len(beatles_aux)-1):
    beatles.append(beatles_aux[b])
    print("Current:", beatles)
    del beatles[-1]
print("Step 3:", beatles)
##

# step 4
print("Step 4:", beatles)
## called step 4 del in step 3 loop


### step 5
beatles.insert(0, beatles_aux[-1])
print("Step 5:", beatles)

# testing list legth
print("The Fab", len(beatles))

print(beatles)
