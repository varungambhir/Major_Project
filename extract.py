import json
import webbrowser

def fun(image,fps):
	x=int(image)
	pos=x/float(fps)
	print pos
	URL="https://www.youtube.com/watch?v=xDMP3i36naA#t="+str(pos)+"s"
	print URL
	webbrowser.open(URL)
	
f=open('abc.txt','w')
tweets = []
for line in open('response.txt', 'r'):
    tweets.append(json.loads(line))
    
f.write(str(tweets[0]['result_final'][0]))


#for i in tweets[0]['result_final'][0]['results'][0]['tags']:
#	print i['tag'],i['confidence']
	
	

dict={}	
n=len(tweets[0]['result_final'])
print "n="+str(n)

cnt=0
for outer in tweets[0]['result_final']:
	cnt=cnt+1
	
		
 	if outer['results'][0]['image'].endswith('.jpg'):
		outer['results'][0]['image']=outer['results'][0]['image'][:-4]
	else:	
		outer['results'][0]['image']=outer['results'][0]['image'][:-5]
	foo=outer['results'][0]['image'][45:]
	print "val="+foo+str(cnt)
	if foo=='':
		continue

	for j in outer['results'][0]['tags']:
		var= str(j['tag'])#,j['confidence']
		
		
		
		

		if var in dict:
			dict[var]=min(int(foo),dict[var])
		else:
			dict[var]=int(foo)	
		
	print 
print dict	
q=raw_input("Enter a word")
if q in dict:
	print dict[q]
	fun(dict[q],30)

