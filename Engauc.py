#coding: UTF-8
from willow.willow import *
import random
def session(me):

    if me == 0:  ### For monitor
        pl = 0

        add(open("Engauc0.html"))
  	
        take({"client":me})     # Block until the initial setting is ready.

        plnum = peek("#plnum")  # Define variables from initial settings
        gnum = peek("#gnum") 
        valuemin = peek("#valuemin")
        valuemax = peek("#valuemax")
        put({"tag":"toclient","plnum":plnum, "gnum":gnum, "valuemin":valuemin, "valuemax":valuemax}) # Make a dictionary to let clients to start the experiments.

        while True:  # Wait until every client reads the instruction.

            msg = take({"tag":"readinst"})
  	    pl += 1
            add("<p>Client %s has finished reading instructions.</p>" % msg["number"])

            if pl == int(plnum):
                break
            else:
                continue

        msg = take({"client": me}) # Start the main part.
        put({"tag":"ready"})

        ### main auction part starts from here. can be changed for other types of auctions.

        count = 0
        round = 1
        price = valuemin - 10

        while True:  
            put({"tag":"auction", "round":round, "price":price})

            add("<p>Begin round %s. Current price is %s."%round, price)

            while True:  
                msg = take({"tag":"tomonitor"})
                pl += 1
                if msg["choice"] == "bid":
                    count += 1
                add("<p>Client %s has chosen %s." % msg["client"], msg["choice"])

                if pl == int(plnum):
                    break
                else:
                    continue

            if count <= gnum:
                show("#finish")
                break
                put({"tag":"toclient","finish":True}) # To tell the clients that the auction has finished.


            else:
                add("<p>There are %s bids for %s goods. Proceed to a next round." % count, gnum)
                round += 1
                price = price + 10
                put({"tag":"toclient","continue":True}) # To tell the clients that the auction has not finished yet.
                continue


    else:  ### For clients
        add(open("Engauc1.html"))

        variables = take({"tag":"toclient"}) # Block until the monitor finishes the itinial setting.
        put(variables) # Recreate the dictionary for other clients

        value = random.randint(variables["valuemin"], variables["valuemax"]) # Calcurate the private value of the goods

        show("#start") # Start to show an instruction
        add(variables["gnum"], "#gnum")
        add(value, "#value")

        take({"client":me}) # Block until the client finishes reading instructions
        put({"tag":"readinst", "number":me }) # Let the monitor know that the client is ready

        take({"tag":"ready"})
        put({"tag":"ready"}) 

        ### main auction part starts from here.
        
        auction = take({"tag":"auction"})
        put(auction)

        show("#auction")
        add(auction["price"],"#price")

        mychoice = take({"client": me}) # choice in the 1st round
        put({"tag":"tomonitor", "choice":mychoice["id"], "client":me}) 

        msg = take({"tag":"toclient"}) # For checking whether proceed or stop
        put(msg)

        while "continue" in msg: # loop for rounds after 1st
            auction = take({"tag":"auction"})
            put(auction)
            add("<p>The number of bids exeeds the number of goods. Please proceed to a next round.</p>")
            add("<p>The value of the goods for you is <strong>%s</strong>. The current price is <strong>%s</strong></p>"% value, auction["price"] )
            add("<p>Please select your action from below.</p>")
            add("<input class='choice' id='bid' value='Bid' type='submit' />")
            add("<input class='choice' id='stop' value='Stop' type='submit' />")
            mychoice = take({"client": me})
            put({"tag":"tomonitor", "choice":msg["id"], "client":me})
            
            msg = take({"tag":"toclient"}) # For checking whether proceed or stop
            put(msg)

        else:
            put({"tag":"result", "choice":msg["id"], "client":me}) # Send a result to the monitor
            if msg["id"] == bid:
                payoff = value - auction["price"]
                add("<p>You successfully purchased the good for %s Yen. </p>"% auction["price"] )
                add("<p>Your final payoff is %s .</p>"% payoff)

            else:
                add("<p>You did not purchase the good.</p>")
                add("<p>Your final payoff is 0.</p>")


run(session)


