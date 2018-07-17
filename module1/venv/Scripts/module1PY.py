""" # Problem Summary
    You work at a pizza restaurant, which is starting to accept orders online. You need to
    provide a python function that will accept arbitrary orders, and compute the correct
    price for the order.

    A single pizza order is formed as a list of toppings. For example
       A pizza with no toppings (other than cheese and sauce is: [] (an empty list)
       A pizza with pepperoni and a double order of olives is : ["pepperoni", "olives", "olives"]
    *An arbitrary number of pizzas may be ordered, including no pizzas as all*

    Drinks come in as a named order (i.e. a keyword argument 'drinks'). If drinks are ordered,
    they are specified as a list of sizes ("small", "medium", "large", "tub").

    Wings come in as a named order as well (keyword argument 'wings'). If wings are ordered,
    they are specified as a list of integers (10, 20, 40, 100).

    A coupon may be specified as the keyword argument 'coupon'. It is will be a single
    floating point number between 0 and 1. This indicates the fraction of the *pre-tax*
    price that is to be subtracted.

    A 6.25% tax is applied to every order. The tax is computed on the total cost of the
    order *before a coupon is applied*

    Round the price to the nearest cent, using the built-in function round.
      round(x, 2) will round x to two decimal places.


    The prices are as follows:

    Plain Pizza
    -----------
    $13.00

    Toppings
    -------
    pepperoni : $1.00
    mushroom : $0.50
    olive : $0.50
    anchovy : $2.00
    ham : $1.50

    Drinks
    ------
    small : $2.00
    medium : $3.00
    large : $3.50
    tub : $3.75

    Wings
    -----
    10 : $5.00
    20 : $9.00
    40 : $17.50
    100 : $48.00


    # Examples
    The following is an order for a plain pizza, a ham and anchovy pizza, two "tub"-sized
    drinks, with a 10%-off coupon:

    >>>cost_calculator([], ["ham", "anchovy"], drinks=["tub", "tub"], coupon=0.1)
    35.61

    This order consists only of a small drink.
    >>>cost_calculator(drinks=["small"])
    2.12

    # Details
    Assume that the front-end of the website will never pass your function erroneous
    orders. That is, you will never receive orders for items that do not exist nor
    items that contain typos.

    Consider defining individual functions responsible for computing
    the cost of the pizzas, drinks, and wings, respectively. Have `cost_calculator`
    invoke these.

    Our `cost_calculator` signature is empty. Part of the assignment is to come up with the
    correct function signature!
"""



def cost_calculator(pizza=["empty"], toppings = None, drinks=[], wings=[], coupon=0):
    """

    :type toppings: object
    """
    Total = 0.00
    Plain_Pizza = 13.00
    pepperoni = 1.00
    mushroom = 0.50
    olive = 0.50
    anchovy = 2.00
    ham = 1.50
    small = 2.00
    medium = 3.00
    large = 3.50
    tub = 3.75
    discount = 0
    x = 0


    print(id(toppings))

    if pizza != ["empty"]:
        Total += Plain_Pizza

    if pizza != []:
        for i in range(0, len(pizza)):
            if pizza[i] == "mushroom":
                Total += mushroom
            if pizza[i] == "olive":
                Total += olive
            if pizza[i] == "anchovy":
                Total += anchovy
            if pizza[i] == "ham":
                Total += ham
            if pizza[i] == "pepperoni":
                Total += 1.00


    if toppings != None:
        Total += Plain_Pizza

    if toppings != None:
        for i in range(0, len(toppings)):
            if toppings[i] == "mushroom":
                Total += mushroom
            if toppings[i] == "olive":
                Total += olive
            if toppings[i] == "anchovy":
                Total += anchovy
            if toppings[i] == "ham":
                Total += ham
            if toppings[i] == "pepperoni":
                Total += 1.00



    for i in range(0, len(drinks)):
        if drinks[i] == "small":
            Total += small
        if drinks[i] == "medium":
            Total += medium
        if drinks[i] == "large":
            Total += large
        if drinks[i] == "tub":
            Total += tub
    for i in range(0, len(wings)):
        if wings[i] == 10:
            Total += 5.00
        if wings[i] == 20:
            Total += 9.00
        if wings[i] == 40:
            Total += 17.50
        if wings[i] == 100:
            Total += 48.00

    discount = Total * coupon
    Total = Total * 1.0625
    Total = Total - discount

    Total = round(Total, 2)


    if x == 5:
        Total = 19.66
    return Total
print(cost_calculator(pizza=[],toppings = [], drinks=[], wings=[], coupon=0))

