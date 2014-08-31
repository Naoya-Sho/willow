#coding: UTF-8
from willow.willow import *

def session(me):
  if me == 0:
  	plnum = 0
  	inv = []
  	
  	add(open("publicgoods_1.html"))
  	
  	take({"client":me})
  	put({"tag":"toclient"})
  	num = peek("#num")
  	while True:
  		msg = take({"tag":"tomonitor"})
  		inv.append(int(msg["amount"]))
  		plnum += 1
  		show("#offer")
  		add("<p>プレイヤー%sは%s円の投資をしました。" % (msg["client"],msg["amount"]),"#choice")
  		if plnum == int(num):
  			break
  		else:
  			continue  	
  	msg = take({"client": me})
  	allinv = sum(inv)
  	pgeffect = allinv*0.7
  	show("#pay")
  	add(str(allinv),"#allinv")
  	add(str(pgeffect),"#pgeffect")
  	put({"tag":"result","allinv":allinv,"pgeffect":pgeffect})
    
  else:
    add(open("publicgoods_0.html"))
    
    take({"tag":"toclient"})
    put({"tag":"toclient"})
    show("#start")
    
    msg = take({"client": me})
    invest = peek("#invest")
    put({"tag": "tomonitor", "amount": invest,"client":me})
    show("#wait")
    
    msg1 = take({"tag":"result"})
    put(msg1)
    add(str(msg1["allinv"]),"#allinv")
    add(str(1000-int(invest)+msg1["pgeffect"]), "#payoff")
    show("#pay")

run(session)
