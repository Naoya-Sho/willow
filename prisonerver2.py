from willow.willow import *

def session(me):
  if me == 0:
      add(open("prisoner.html"))
      msg0 = take({"client": me})
      choice_0 = msg0["id"]
      put({"tag":"pl_0","choice_0":choice_0})
      show("#wait")
      add(choice_0, "#pchoice")
      msg0 = take({"tag": "pl_1"})

      if choice_0 == msg0["choice_1"] == "confess":
          penal = "7"
      elif choice_0 == "confess" and msg0["choice_1"] == "silence":
          penal = "1"
      elif choice_0 == "silence" and msg0["choice_1"] == "confess":
          penal = "10"
      elif choice_0 == msg0["choice_1"] == "silence":
          penal = "3"

      show("#sentence")
      add(penal, "#penal")

  elif me == 1:
      add(open("prisoner.html"))
      msg1 = take({"client": me})
      choice_1 = msg1["id"]
      put({"tag":"pl_1","choice_1":choice_1})
      show("#wait")
      add(choice_1, "#pchoice")
      msg1 = take({"tag": "pl_0"})

      if msg1["choice_0"] == choice_1 == "confess":
          penal = "7"
      elif msg1["choice_0"] == "confess" and choice_1 == "silence":
          penal = "10"
      elif msg1["choice_0"] == "silence" and choice_1 == "confess":
          penal = "1"
      elif msg1["choice_0"] == choice_1 == "silence":
          penal = "3"
    
      show("#sentence")
      add(penal, "#penal")

run(session)