def add_items(a):
    count = 0
    if not (isinstance(a,list) ):
            raise TypeError('invalid type')
    if len(a)==0:
        return ('no value')
    else:
        for i in a:
        
            if isinstance(i,int):
                count += i
            elif isinstance(i,list):
                count+=add_items(i)
            else:
                pass
        return count

print(add_items([1,2,3,[3],[1,3]]))
