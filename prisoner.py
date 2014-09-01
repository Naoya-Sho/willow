from willow.willow import *

def session(me):
  if me == 0:
      add(open("prisoner.html"))
      msg0 = take({"client": me})
      choice_0 = msg0["id"]
      put({"choice_0":choice_0})
      show("#wait")
      add(choice_0, "#pchoice")
      msg0 = take({"choice_1": choice_1})

      if choice_0 == choice_1 == "confess":
          penal = "7"
      elif choice_0 == "confess" and choice_1 == "silence":
          penal = "1"
      elif choice_0 == "silence" and choice_1 == "confess":
          penal = "10"
      elif choice_0 == choice_1 == "silence":
          penal = "3"

      show("#sentence")
      add(penal, "#penal")

  elif me == 1:
      add(open("prisoner.html"))
      msg1 = take({"client": me})
      choice_1 = msg1["id"]
      put({"choice_1":choice_1})
      show("#wait")
      add(choice_1, "#pchoice")
      msg1 = take({"choice_0": choice_0})

      if choice_0 == choice_1 == "confess":
          penal = "7"
      elif choice_0 == "confess" and choice_1 == "silence":
          penal = "10"
      elif choice_0 == "silence" and choice_1 == "confess":
          penal = "1"
      elif choice_0 == choice_1 == "silence":
          penal = "3"
    
      show("#sentence")
      add(penal, "#penal")

run(session)

