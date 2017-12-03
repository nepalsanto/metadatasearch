import csv
import jellyfish

tags=['scenenumbers','helicopter','hotairballoon','cloud','sun','lightning','rain','rocket','airplane','bouncy','slide','sandbox','grill','swing','tent','table','pinetree','oaktree','appletree','boy','girl','bear','cat','dog','duck','owl','snake','baseballcap','crown','chefhat','piratehat','wintercap','bennie','wizardhat','vikinghat','purpleglasses','sunglasses','pie','pizza','hotdog','ketchup','mustard','hamburger','soda','baseball','pail','beachball','basketball','soccerball','tennisball','football','frisbee','baseballbat','balloons','baseballglove','shovel','tennisracket','kite','fire']
extended=['','spaceobject','bright','yellow','camp','shelter','rest','royal','head','sparkling','can','liquid','cold','workingtool','withhandle','digging']
with open('image_tags.csv', 'r') as csvfile:	
	readCSV = csv.reader(csvfile, delimiter=',')	
	i=59
	j=500
	Matrix = [[0 for x in range(i)] for y in range(j)] 	
	p=0
	for row in readCSV: 
		for i in range (0,59):
			Matrix[p][i] = (row[i])
	
		p=p+1
csvfile.close()

list1 =[0 for x in range(59)]#constant list
list2 =[0 for x in range(59)]#variable list
position=[0 for y in range(500)]#position of reformed array
match_count=[0 for y in range(500)]#matches between existing '1' element of each array 

print("enter the scene number:: ((format: 0 for Scene300_0; 20 for Scene301_9 and so on... ))")
ans = int(input ('range from 0 to 499:: '))

for column in range(0,59):
	list1[column]= Matrix[ans][column]

print(list1) 

for row in range(0,500):
	for column in range(0,59):
		list2[column]=Matrix[row][column]
		if list1[column]==list2[column]=='1':
			match_count[row]=match_count[row]+1
#print (Matrix[row][0] , end='')
#print (match_count[row])


print (match_count)
print(len(match_count))

for passnum in range(0,len(match_count)):
	
	for i in range(passnum):					#swapping the values and arranging list in certain order
		if match_count[i] < match_count[i+1]:
			r=Matrix[i][0]
			temp = match_count[i]
			Matrix[i][0]=Matrix[i+1][0]
			match_count[i] = match_count[i+1]
			Matrix[i+1][0]=r
			match_count[i+1] = temp
		
			

print("top 20 results similar to image queried :")
for i in range(0,20):
	print(Matrix[i][0])


