if __name__=='__main__':
    food=['rice','beans']
    food.append('broccoli')
    food.extend(['bread','pizza'])
    print(food[0:2])
    print(food[len(food)-1])

    breakfast="eggs,fruit,orange juice".split(',')
    print(breakfast)
    print(f'breakfast has {len(breakfast)} elements')

    floatlist = []
    floatvalue=""
    while floatvalue!='stop':
        floatvalue = input('Enter a floating point value: ')
        if floatvalue != 'stop':
            floatlist.append(float(floatvalue))
    average=sum(floatlist) / len(floatlist)
    minimum=min(floatlist)
    maximum=max(floatlist)
    print(f'Average: {average} Min: {minimum} Max {maximum}')