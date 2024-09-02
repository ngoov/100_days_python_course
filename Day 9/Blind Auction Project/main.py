# TODO-1: Ask the user for input
import \
    os

moreInputRequired = True
bids = {}
while moreInputRequired:
    name = input("Your name:\n")
    price = float(input("Your price:\n"))
    # TODO-2: Save data into dictionary {name: price}
    bids[name] = price
    
    # TODO-3: Whether if new bids need to be added
    moreBids = input("More bids? y?").lower()
    if moreBids != 'y':
        moreInputRequired = False
    
    os.system("clear")
# TODO-4: Compare bids in dictionary
highestBidBy = ''
for bidBy in bids:
    if highestBidBy == '':
        highestBidBy = bidBy
    else:
        if bids[bidBy] > bids[highestBidBy]:
            highestBidBy = bidBy

print(f'Highest bid of {bids[highestBidBy]} by {highestBidBy}')

