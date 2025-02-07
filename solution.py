import art
print(art.logo)
bidding_dictionary={}
def highest_bidding(bidding_dictionary):
    if should_continue == "no":
        maximum = 0
        for key in bidding_dictionary:
            if bidding_dictionary[key] > maximum:
                maximum = bidding_dictionary[key]
            else:
                continue
        print(f"The highest bid is {maximum} by {key}")
continue_bidding = True
while continue_bidding:
    Name = input("Enter your Name:")
    price = int(input("Enter the bidding price in $:"))
    bidding_dictionary[Name] = price
    should_continue = input("Are there any new bids yes_or_no?:")
    if should_continue == "no":
        continue_bidding = False
        maximum = 0
        for key in bidding_dictionary:
            if bidding_dictionary[key] > maximum:
                maximum = bidding_dictionary[key]
            else:
                continue
        print(f"The highest bid is {maximum} by {key}")
    elif should_continue == "yes":
        print("\n"*100)
        continue_bidding = True
    else:
        print("Error in input")
