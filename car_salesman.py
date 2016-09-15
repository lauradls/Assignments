#HW 1 - Car Salesman problem

fees = {'dealerprep':293, 'destination':600}
Base_price = int(input("What is the base price of your car?" )) 
Actual_price = Base_price + (0.0685 * Base_price) + (0.65 * Base_price) + fees['dealerprep'] + fees['destination'] 
print ("The actual price is", Actual_price, "dollars.")
