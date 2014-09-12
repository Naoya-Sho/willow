#coding: UTF-8
from willow.willow import *
import random
def session(me):

    if me == 0:  ### For monitor
        pl = 0

        add(open("Engauc0.html"))
  	
        take({"tag": "click"})     # Block until the initial setting is ready.

        plnum = int(peek("#plnum"))  # Define variables from initial settings
        gnum = int(peek("#gnum"))
        valuemin = int(peek("#valuemin"))
        valuemax = int(peek("#valuemax"))
        put({"tag":"toclient","plnum":plnum, "gnum":gnum, "valuemin":valuemin, "valuemax":valuemax}) # Make a dictionary to let clients to start the experiments.

        while True:  # Wait until every client reads the instruction.

            msg = take({"tag":"readinst"})
  	    pl += 1
            add("<p>Client %s has finished reading instructions.</p>" % msg["number"], "#inst")

            if pl == int(plnum):
                break
            else:
                continue

        show("#ready")
        msg = take({"client": me}) # Start the main part.
        put({"tag":"ready"})
        show("#start")

        ### main auction part starts from here. can be changed for other types of auctions.

        count = 0
        round = 0
        price = valuemin - 10

        while True:

            ## Initialize the variables and dictionaries
            pl = 0
            count = 0
            price += 10
            round += 1

            sleep(3)
            grab({"tag":"loop"})

            put({"tag":"auction", "round":round, "price":price})
            add("<p>Begin round %s. Current price is %s." % (str(round), str(price)))

            while True:
                clchoice = take({"tag":"mychoice"})
                pl += 1
                winners = []

                if clchoice["choice"] == "bid":
                    count += 1
                    winners.append(clchoice["client"])
 
                add("<p>Client %s has chosen %s." % (clchoice["client"], clchoice["choice"]), "#action")
                log(clchoice["client"], clchoice["choice"], price)

                if pl == int(plnum):
                    break
                else:
                    continue

            if count <= int(gnum):
                show("#finish")
                grab({"tag":"auction"})
                put({"tag":"loop","finish":True}) # To tell the clients that the auction has finished.
                #add("<p>Clients s% have purchased the goods for s% Yen." % (str(winners), str(price)),"#result")
                break

            else:
                add("<p>There are %s bids for %s goods. Proceed to a next round." % (str(count), str(gnum)))
                grab({"tag":"auction"})
                put({"tag":"loop","continue":True}) # To tell the clients that the auction has not finished yet.
                continue


    else:  ### For clients
        add(open("Engauc1.html"))

        variables = take({"tag":"toclient"}) # Block until the monitor finishes the itinial setting.
        put(variables) # Recreate the dictionary for other clients

        value = random.randrange(variables["valuemin"], variables["valuemax"], 10) # Calcurate the private value of the goods

        show("#start") # Start to show an instruction
        add(variables["gnum"], "#gnum")
        add(value, "#value0")
        add(value, "#value1")
        add(value, "#value2")

        take({"client":me}) # Block until the client finishes reading instructions
        put({"tag":"readinst", "number":me }) # Let the monitor know that the client is ready

        take({"tag":"ready"})
        put({"tag":"ready"}) 

        ### main auction part starts from here.
        
        auction = take({"tag":"auction"})
        put(auction)

        show("#auction")
        add(value, "#value3")
        add(auction["price"],"#price")


        mychoice = take({"client": me}) # choice in the 1st round
        put({"tag":"mychoice", "choice": mychoice["id"], "client":me}) 
        clloop = take({"tag":"loop"}) # For checking whether to proceed or stop
        put(clloop)

        while "continue" in clloop: # loop for rounds after 1st 
            auction = take({"tag":"auction"})
            put(auction)
            add("<p>The number of bids exceeds the number of goods. Please proceed to a next round.</p>")
            add("<p>The value of the goods for you is <strong>%s</strong>. The current price is <strong>%s</strong></p>" % (str(value), str(auction["price"])))
            add("<p>Please select your action from below.</p>")
            add("<input class='choice' id='bid' value='Bid' type='submit' />")
            add("<input class='choice' id='stop' value='Stop' type='submit' />")
            mychoicel = take({"client": me})
            put({"tag":"mychoice", "choice":mychoicel["id"], "client":me})
            clloop = take({"tag":"loop"}) # For checking whether to proceed or stop
            put(clloop)

        else:
            put({"tag":"result", "choice":mychoicel["id"], "client":me}) # Send a result to the monitor
            show("#finish")
            if mychoicel["id"] == "bid":
                payoff = value - auction["price"]
                add("<p>You successfully purchased the good for %s Yen. </p>"% str(auction["price"]),"#purchase")
                add("<p>Your final payoff is %s .</p>"% str(payoff),"#purchase")

            else:
                add("<p>You did not purchase the good.</p>")
                add("<p>Your final payoff is 0.</p>")


run(session)


