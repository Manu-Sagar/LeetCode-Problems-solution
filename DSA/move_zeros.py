def move_zero(values):
    ind=0
    for index,value in enumerate(values):
        if value!=0:
            values[ind],values[index]=values[index],values[ind]
            ind+=1
    return values

print(move_zero([1,5,0,6,0,8]))