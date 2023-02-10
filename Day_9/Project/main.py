#importing the clear function from replit module
from replit import clear

from art import logo
print(logo)
print("welcome to Brendan's Secret Auction Program")

#creating an empty dictionary to store bidder's name as the key and the bid amount as the value
bidder_info = {}
bidding_finish = False
# creating a function that loops through a dictionary
def check_highest_bidder(biddings):
  top_bidder_price = 0
  top_bidder_name = ""
  for bidcheck in biddings:
    bid_amount = biddings[bidcheck]
    if bid_amount > top_bidder_price:
      top_bidder_price = bid_amount
      top_bidder_name = bidcheck
  print(f"The winner is {top_bidder_name} with a bid price of ${top_bidder_price}")
 
 # a loop that adds bidder's information to our empty dictionary "bidder_info" 
while not bidding_finish:
  bidder_name = input("type in your name: ")
  bidder_amount = int(input("type in your bidding amount: $"))
  bidder_info[bidder_name] = bidder_amount
  cont_request = input("Are there other bidders with you? type in 'yes' or 'no': ")
  
  if cont_request == "no":
    bidding_finish = True
    check_highest_bidder(bidder_info)
  elif cont_request == "yes":
    clear()
  
  
    
  
