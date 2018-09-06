def add_items(a):
    count = 0
    if not (isinstance(a,list) ):
            raise TypeError('invalid type')
    for i in a:
        
        if isinstance(i,int):
            count += i
        elif isinstance(i,list):
            count+=add_items(i)
        else:
            pass
    return count

print(add_items([1,2,5,[1,2],]))
