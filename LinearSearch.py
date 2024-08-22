i=0
thislist = [4,6,1,7,9,2,8,12]
for x in thislist:
  i=i+1
  if x==9:
    print('found')
    break 
print(i-1)

if len(thislist)==i:
    print('NotFound')
print(thislist)


# my_list = [21, 44, 35, 11]

# for index, val in enumerate(my_list):
#     print(index, val)
  