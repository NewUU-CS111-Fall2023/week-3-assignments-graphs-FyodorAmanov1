class graph:
    def Search(a, b):
        list = []
        while(a <= b):
            list.append(b)
            if b%10  == 1:
                b = (b-1)//10
            elif b %2 == 0:
                b//= 2
            else:
                break
        if list[-1] == a:
            print("Yes")
            print(len(list))
            print(*list)
        else:
            print("No")

            #print(list[0'start':20'stop':3'step'])
            'can be print(list[::-1])'