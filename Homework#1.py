import sys
import math
import argparse

"""Betty Kouadio
I pledge on my honor that I have not given or received any unauthorized assistance on this assignment. """



def  get_min_payment(total_amount_mortage,annual_interest_rate,term_mortgage=30, number_of_payment_per_year=12) :
    """• Parameters
◦ the total amount of the mortgage (called the principal; should be a positive number)
◦ the annual interest rate (should be a float between 0 and 1)
◦ the term of the mortgage, in years (should be a positive integer; default value: 30)
◦ the number of payments per year (should be a positive integer; default value: 12)
• Functionality
◦ Compute the minimum mortgage payment. Should use the formula A= (P*r)*(1+r) /((1+r)*-1)

 """
    n =  (term_mortgage* number_of_payment_per_year)
    A  =  (total_amount_mortage*annual_interest_rate)*(1+annual_interest_rate)**n / ((1+annual_interest_rate)**n - 1)
    return math.ceil(A)



def interest_due(balance_of_mortgage,annual_interest_rate, number_of_payment_per_year =12) :
    """ • Parameters
◦ the balance of the mortgage (the part of the principal that has not been paid back yet; should be a
positive number)
◦ the annual interest rate (should be a float between 0 and 1)
◦ the number of payments per year (should be a positive integer; default value: 12)
• Functionality
◦ Compute and return the amount of interest due in the next payment according to the formula i = br,
where
▪ i is the amount of interest due in the next payment
▪ b is the balance of the mortgage
▪ r is the interest rate per payment (the annual interest rate divided by the number of payments per
year)"""
    interest_rate_per_payment = (annual_interest_rate/number_of_payment_per_year)
    due_next_payment = (balance_of_mortgage * interest_rate_per_payment)
    i  = due_next_payment
    return i


def remaining_payments(balance_of_mortgage,annual_interest_rate,payment,number_of_payment_per_year=12) :
    """Parameters
◦ the balance of the mortgage (the part of the principal that has not been paid back yet; should be a
positive number)
◦ the annual interest rate (should be a float between 0 and 1)
◦ the payment amount (the amount the user wants to pay per payment; should be a positive number)
◦ the number of payments per year (should be a positive integer; default value: 12)
Functionality
◦ Compute and return the number of payments required to pay off the mortgage. We will do this by
simulating payments one at a time until the balance of the mortgage reaches zero, assuming fixed
payments (in other words, assume that each payment is the same amount of money as the previous
one).

 """
    count = 0
    while balance_of_mortgage >0 :
        money_to_bank = payment - interest_due(balance_of_mortgage,annual_interest_rate,number_of_payment_per_year)
        balance_of_mortgage -= money_to_bank 
        count += 1
    return count

def main(total_amount_mortage,interest_rate,term_mortgage=30, number_of_payment_per_year =12,target_payment= None) :
    """ • Parameters
◦ the total amount of the mortgage (i.e., the principal; should be a positive number)
◦ the annual interest rate (should be a float between 0 and 1)
◦ the term of the mortgage, in years (should be a positive integer; default value: 30)
◦ the number of payments per year (should be a positive integer; default value: 12)
◦ the user's target payment (the amount the user wishes to pay per payment; should be a positive
number or None; default value: None)
▪ A value of None indicates that the user wishes to use the minimum payment
• Functionality
◦ Compute the minimum payment using the get_min_payment() function
"""

    minimun_payment = get_min_payment(total_amount_mortage,interest_rate,term_mortgage,number_of_payment_per_year)
    if target_payment == None:
        target_payment = minimun_payment
    elif target_payment < minimun_payment:
        print("Your target payment is less than the minimum payment for this mortgage")
    else:
        payment_left= remaining_payments(total_amount_mortage,interest_rate,target_payment,number_of_payment_per_year)
        print("If you make payments of $"+{target_payment}+ ",You will pay off your mortgage in " +{payment_left})

def parse_args(args_list) :
    """ Compute the minimum payment using the get_min_payment() function
◦ Display the minimum payment to the user
◦ If the user's target payment is None, set the target payment to the minimum payment
◦ If the user's target payment is less than the minimum payment, print a message to the user (e.g.,
Your target payment is less than the minimum payment for this mortgage"""
    parser_args = argparse.ArgumentParser(args_list)
    parser_args.add_argument("total_amount_mortage",type=float, help="Total mortgage")
    parser_args.add_argument("interest_rate",type=float, help="Interest rate ")
    parser_args.add_argument("--term_mortgage",type=int, default=30, help="Total mortgage")
    parser_args.add_argument("--number_of_payment_per_year",type=int,default=12, help="Number of payment fer year")
    parser_args.add_argument("--target_payment",type=float, help="Monthly mortgage Payment")
    arguments= parse_args(args_list)
    return arguments

if __name__ == "__main__":
    system_arguments = parse_args(sys.argv[1:])
    main(system_arguments.total_amount_mortgage, system_arguments.interest_rate,system_arguments.term_mortgage,system_arguments.number_of_payment_per_year,system_arguments.target_payment)
    print(get_min_payment(int(sys.argv[1])))
    print(interest_due(int(sys.argv[1])))
    print(remaining_payments(float(sys.argv[1])))
    
    
    
    



