#HW 1 - Car Salesman problem

fees = {'dealerprep':293, 'destination':600}
Base_price = int(input("What is the base price of your car?" )) 
Actual_price = Base_price + (0.0685 * Base_price) + (0.65 * Base_price) + fees['dealerprep'] + fees['destination'] 
print ("The actual price is", Actual_price, "dollars.")

##These are the sources from where I found my data in order to make an approximation a little close to reality. The information found is not Utah specific and is not accurate enough to trust this model, it only serves the purpose of constructing a simulation.

###1.Dealer prep: http://www.realcartips.com/newcars/482-documentation-fees-by-state.shtml

###2.Destination charge: http://www.kbb.com/car-advice/articles/destination-charges/

###3.Tax: https://www.salestaxhandbook.com/utah/sales-tax-vehicles , http://www.autobytel.com/auto-news/buying-a-new-car-in-utah-107748/ 

###4.License: https://www.dmv.ca.gov/portal/dmv/detail/pubs/brochures/fast_facts/ffvr34
