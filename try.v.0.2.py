import csv
import jellyfish

tags=['scenenumbers','helicopter','hotairballoon','cloud','sun','lightning','rain','rocket','airplane','bouncy','slide','sandbox','grill','swing','tent','table','pinetree','oaktree','appletree','boy','girl','bear','cat','dog','duck','owl','snake','baseballcap','crown','chefhat','piratehat','wintercap','bennie','wizardhat','vikinghat','purpleglasses','sunglasses','pie','pizza','hotdog','ketchup','mustard','hamburger','soda','baseball','pail','beachball','basketball','soccerball','tennisball','football','frisbee','baseballbat','balloons','baseballglove','shovel','tennisracket','kite','fire']
extended=['','spaceobject','bright','yellow','camp','shelter','rest','royal','head','sparkling','can','liquid','cold','workingtool','withhandle','digging']
with open('image_tags.csv', 'r') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')	
	i=59
	j=500
	Matrix=[[0 for x in range(i)] for y in range(j)] 	
	p=0
	for row in readCSV: 
		for i in range (0,59):
			Matrix[p][i] = (row[i])
			#print (p)
		p=p+1
csvfile.close()

print (Matrix[15][58])	
print (Matrix[15][0])

ans = input ('enter the metadata vocabulary(for multiple vocab, use space) ')

def basic(app):
	pinn=0
	vplace=0
	hplace=0
	for vplace in range (0,59):
		pinn=jellyfish.jaro_distance(app, tags[vplace])
		if pinn > 0.85:
			print (tags[vplace])
			for hplace in range (0,500):
				#print(hplace)
				if (Matrix[hplace][vplace]) == '1' or (Matrix[hplace][vplace]) == " 1":
					#print (1)
					print (Matrix[hplace][0])

def ext(app):
	#p=0
	vplace=0
	hplace=0
	for vplace in range(0,16):
		#p=jellyfish.jaro_distance(app, tags[vplace])
		if app == extended[vplace]:
			if vplace <= 3:
				print ("query executed search for :"+tags[4])
				for hplace in range (0,500):
					if (Matrix[hplace][4])=='1' or (Matrix[hplace][vplace]) == " 1":
						print (Matrix[hplace][0])
			
			elif vplace > 3 and vplace <= 6:
				print ("query executed search for :"+tags[14])
				for hplace in range (0,500):
					if (Matrix[hplace][14])=='1' or (Matrix[hplace][vplace]) == " 1":
						print (Matrix[hplace][0])

			elif vplace > 6 and vplace <= 9:
				print ("query executed search for :"+tags[28])
				for hplace in range (0,500):
					if (Matrix[hplace][28])=='1' or (Matrix[hplace][vplace]) == " 1":
						print (Matrix[hplace][0])
			
			elif vplace > 9 and vplace <= 12:
				print ("query executed search for :"+tags[43])
				for hplace in range (0,500):
					if (Matrix[hplace][43])=='1' or (Matrix[hplace][vplace]) == " 1":
						print (Matrix[hplace][0])
			else:
				print ("query executed search for :"+tags[55] )
				for hplace in range (0,500):
					if (Matrix[hplace][55])=='1' or (Matrix[hplace][vplace]) == " 1":
						print (Matrix[hplace][0])
		


an=ans.split(" ")
#print(len(an))


for kk in range(0,len(an)):
	basic(an[kk])
for tt in range(0,len(an)):
	ext(an[tt])

