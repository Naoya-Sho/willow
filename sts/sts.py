from willow.willow import *

def session(me):
  if me == 0:
      add(open("sts_0.html"))
      log("Pnum","Qnum","Ans")
      for i in range(18):
      	msg1 = take({"tag": "next"})
      	msg2 = take({"tag": "next"})
      	put({"tag": "next"+str(i+1)})
      	put({"tag": "next"+str(i+1)})

  elif me == 1:
      ans =[]
      trueans = [1,2,2,0,0,3,2,0,3,0,1,2,1,1,2,1,4,2]
      easy = 0
      normal = 0
      hard = 0
      for i in range(18):
      	add(open("sts"+str(i+1)+"_0.html"))
      	msg = take({"client": me})
      	log(me,i+1,msg["id"])
      	ans.append(int(msg["id"]))
      	put({"tag": "next"})
      	take({"tag": "next"+str(i+1)})
      	hide("#sts"+str(i+1)+"_0")
      	
      for i in [2,8,12,15,16]:
      	if ans[i] == trueans[i]:
      		easy += 1
      	else:
      		easy += 0
      		
      for i in [0,1,6,10,11,13,17]:
      	if ans[i] == trueans[i]:
      		normal += 1
      	else:
      		normal += 0
      		
      for i in [5,14]:
      	if ans[i] == trueans[i]:
      		hard += 1
      	else:
      		hard += 0
      
      if normal >= 6:
      	sts = "High"
      elif normal <= 2:
      	sts = "Low"
      else:
      	sts = "Middle"
      
      add(open("sts_result.html"))
      add(easy,"#easy")
      add(normal,"#normal")
      add(hard,"#hard")
      add(sts,"#level")
      
  elif me == 2:
      ans =[]
      trueans = [1,1,2,0,0,2,2,0,1,0,2,1,2,2,2,1,1,4]
      easy = 0
      normal = 0
      hard = 0
      for i in range(18):
      	add(open("sts"+str(i+1)+"_1.html"))
      	msg = take({"client": me})
      	log(me,i+1,msg["id"])
      	ans.append(int(msg["id"]))
      	put({"tag": "next"})
      	take({"tag": "next"+str(i+1)})
      	hide("#sts"+str(i+1)+"_1")
      	
      for i in [0,6,10,11,17]:
      	if ans[i] == trueans[i]:
      		easy += 1
      	else:
      		easy += 0
      		
      for i in [2,5,8,12,14,15,16]:
      	if ans[i] == trueans[i]:
      		normal += 1
      	else:
      		normal += 0
      
      for i in [1,13]:
      	if ans[i] == trueans[i]:
      		hard += 1
      	else:
      		hard += 0
      
      if normal >= 6:
      	sts = "High"
      elif normal <= 2:
      	sts = "Low"
      else:
      	sts = "Middle"
      	
      add(open("sts_result.html"))
      add(easy,"#easy")
      add(normal,"#normal")
      add(hard,"#hard")
      add(sts,"#level")
      
      	
run(session)

