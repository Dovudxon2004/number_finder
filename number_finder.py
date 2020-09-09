i=1
print(50)
my_list=list(range(101))
ask=int(input("high=9, low=1, exact=5: "))
if ask==5:
    print('I found the number at once. I am genius😎' )    
while ask!=5:
    if ask==1:
        i=i+1
        my_list=my_list[:(int(len(my_list)/2))]
        print(my_list[int(len(my_list)/2)])
        ask=int(input("high=9, low=1, exact=5: "))
    if ask==9:
        i=i+1
        my_list=my_list[int(len(my_list)/2):]
        print(my_list[int(len(my_list)/2)])
        ask=int(input("high=9, low=1, exact=5: "))
    if ask==5:
        break
if ask==5 and i!=1:
    print('I found the number in '+str(i)+' tries. I am genius😎' )
