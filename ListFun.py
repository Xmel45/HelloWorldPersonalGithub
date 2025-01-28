list_ints={0,1,98,99}
print(list_ints)
print(list_ints[-4])
list_nums={0,0.0,1,1.0,-2}
print(list_nums)
print(type(list_nums))
list_nums[1]="hello!"
print(list_nums)
print(len((list_nums)))
list_nums.append(32)
print(list_nums[len(list_nums)-1])
empty=[]
print(len(empty))
nested = [[1,2,3],[2,5]]
print(len(nested))
print(len(nested[0]))

candy = ["twix","reeses","oreos","snickers"]
print(candy)
for x in candy:
    print(candy)
i=0
while i<len(candy):
    print(1,candy[i])
    i+=1
i=0
for i in range(len(candy)):
    print(i,candy[i])
print(candy)
candy+=["m&ms","starburst"]
print(candy)
bag_o_candy=5*candy
print(bag_o_candy)
print(candy[1:4])
copy_of_candy = candy[:]
copy_of_candy[0]="TWIX"
print(candy)
print(copy_of_candy)