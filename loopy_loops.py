if __name__=='__main__':
    pocketmon=('picachu','charmander','bulbasur')
    print(pocketmon[1])
    
    (starter1,starter2,starter3)=pocketmon
    print(f'starter1 = {starter1} starter2 = {starter2} starter3 = {starter3}')
    
    MyName=tuple('Zeus')
    print(f'Is i in my name: {"i" in MyName}')

    i=range(2,11)
    for n in i:
        print(n)

    string_='this is a simple string'
    i=0
    while i<len(string_):
        print(string_[i])
        i+=1
    
    StringTuple=('this', 'is', 'a', 'simple', 'set') 
    i=0
    while i<len(StringTuple):
        j=0
        while j<3:
            print(StringTuple[i])
            j+=1
        i+=1