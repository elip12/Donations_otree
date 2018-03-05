# config file for Donations otree experiment
# Rachel Zhang, Eli Pandolfo
# There will never be more than 12 participants.
# Each participant is given a participant code by the room

# this is a static list that is copied out of to get the sets we want for experiments
'''
perms =  [  
            #Rachel's permutations, 72 in total
            #6 in this block, base permutation
            [['pub', 0.0],   ['pub', 0.1],    ['pub', 0.9],    ['pri', 0.0],    ['pri', 0.1],    ['pri', 0.9]],
            [['pub', 0.0],   ['pub', 0.9],    ['pub', 0.1],    ['pri', 0.0],    ['pri', 0.9],    ['pri', 0.1]],
            [['pub', 0.1],   ['pub', 0.0],    ['pub', 0.9],    ['pri', 0.1],    ['pri', 0.0],    ['pri', 0.9]],
            [['pub', 0.1],   ['pub', 0.9],    ['pub', 0.0],    ['pri', 0.1],    ['pri', 0.9],    ['pri', 0.0]],
            [['pub', 0.9],   ['pub', 0.0],    ['pub', 0.1],    ['pri', 0.9],    ['pri', 0.0],    ['pri', 0.1]],
            [['pub', 0.9],   ['pub', 0.1],    ['pub', 0.0],    ['pri', 0.9],    ['pri', 0.1],    ['pri', 0.0]],
    
            #6 in this block, base permutation
            [['pri', 0.0],   ['pri', 0.1],    ['pri', 0.9],    ['pub', 0.0],    ['pub', 0.1],    ['pub', 0.9]],
            [['pri', 0.0],   ['pri', 0.9],    ['pri', 0.1],    ['pub', 0.0],    ['pub', 0.9],    ['pub', 0.1]],
            [['pri', 0.1],   ['pri', 0.0],    ['pri', 0.9],    ['pub', 0.1],    ['pub', 0.0],    ['pub', 0.9]],
            [['pri', 0.1],   ['pri', 0.9],    ['pri', 0.0],    ['pub', 0.1],    ['pub', 0.9],    ['pub', 0.0]],
            [['pri', 0.9],   ['pri', 0.0],    ['pri', 0.1],    ['pub', 0.9],    ['pub', 0.0],    ['pub', 0.1]],
            [['pri', 0.9],   ['pri', 0.1],    ['pri', 0.0],    ['pub', 0.9],    ['pub', 0.1],    ['pub', 0.0]],

            #5 in each of the following blocks
            [['pub', 0.0],   ['pub', 0.1],    ['pub', 0.9],    ['pri', 0.0],    ['pri', 0.9],    ['pri', 0.1]],
            [['pub', 0.0],   ['pub', 0.1],    ['pub', 0.9],    ['pri', 0.1],    ['pri', 0.0],    ['pri', 0.9]],
            [['pub', 0.0],   ['pub', 0.1],    ['pub', 0.9],    ['pri', 0.1],    ['pri', 0.9],    ['pri', 0.0]],
            [['pub', 0.0],   ['pub', 0.1],    ['pub', 0.9],    ['pri', 0.9],    ['pri', 0.0],    ['pri', 0.1]],
            [['pub', 0.0],   ['pub', 0.1],    ['pub', 0.9],    ['pri', 0.9],    ['pri', 0.1],    ['pri', 0.0]],
    
            [['pub', 0.0],   ['pub', 0.9],    ['pub', 0.1],    ['pri', 0.0],    ['pri', 0.9],    ['pri', 0.1]],
            [['pub', 0.0],   ['pub', 0.9],    ['pub', 0.1],    ['pri', 0.1],    ['pri', 0.0],    ['pri', 0.9]],
            [['pub', 0.0],   ['pub', 0.9],    ['pub', 0.1],    ['pri', 0.1],    ['pri', 0.9],    ['pri', 0.0]],
            [['pub', 0.0],   ['pub', 0.9],    ['pub', 0.1],    ['pri', 0.9],    ['pri', 0.0],    ['pri', 0.1]],
            [['pub', 0.0],   ['pub', 0.9],    ['pub', 0.1],    ['pri', 0.9],    ['pri', 0.1],    ['pri', 0.0]],
    
            [['pub', 0.1],   ['pub', 0.0],    ['pub', 0.9],    ['pri', 0.0],    ['pri', 0.9],    ['pri', 0.1]],
            [['pub', 0.1],   ['pub', 0.0],    ['pub', 0.9],    ['pri', 0.1],    ['pri', 0.0],    ['pri', 0.9]],
            [['pub', 0.1],   ['pub', 0.0],    ['pub', 0.9],    ['pri', 0.1],    ['pri', 0.9],    ['pri', 0.0]],
            [['pub', 0.1],   ['pub', 0.0],    ['pub', 0.9],    ['pri', 0.9],    ['pri', 0.0],    ['pri', 0.1]],
            [['pub', 0.1],   ['pub', 0.0],    ['pub', 0.9],    ['pri', 0.9],    ['pri', 0.1],    ['pri', 0.0]],
    
            [['pub', 0.1],   ['pub', 0.9],    ['pub', 0.0],    ['pri', 0.0],    ['pri', 0.9],    ['pri', 0.1]],
            [['pub', 0.1],   ['pub', 0.9],    ['pub', 0.0],    ['pri', 0.1],    ['pri', 0.0],    ['pri', 0.9]],
            [['pub', 0.1],   ['pub', 0.9],    ['pub', 0.0],    ['pri', 0.1],    ['pri', 0.9],    ['pri', 0.0]],
            [['pub', 0.1],   ['pub', 0.9],    ['pub', 0.0],    ['pri', 0.9],    ['pri', 0.0],    ['pri', 0.1]],
            [['pub', 0.1],   ['pub', 0.9],    ['pub', 0.0],    ['pri', 0.9],    ['pri', 0.1],    ['pri', 0.0]],
    
            [['pub', 0.9],   ['pub', 0.0],    ['pub', 0.1],    ['pri', 0.0],    ['pri', 0.9],    ['pri', 0.1]],
            [['pub', 0.9],   ['pub', 0.0],    ['pub', 0.1],    ['pri', 0.1],    ['pri', 0.0],    ['pri', 0.9]],
            [['pub', 0.9],   ['pub', 0.0],    ['pub', 0.1],    ['pri', 0.1],    ['pri', 0.9],    ['pri', 0.0]],
            [['pub', 0.9],   ['pub', 0.0],    ['pub', 0.1],    ['pri', 0.9],    ['pri', 0.0],    ['pri', 0.1]],
            [['pub', 0.9],   ['pub', 0.0],    ['pub', 0.1],    ['pri', 0.9],    ['pri', 0.1],    ['pri', 0.0]],
    
            [['pub', 0.9],   ['pub', 0.1],    ['pub', 0.0],    ['pri', 0.0],    ['pri', 0.9],    ['pri', 0.1]],
            [['pub', 0.9],   ['pub', 0.1],    ['pub', 0.0],    ['pri', 0.1],    ['pri', 0.0],    ['pri', 0.9]],
            [['pub', 0.9],   ['pub', 0.1],    ['pub', 0.0],    ['pri', 0.1],    ['pri', 0.9],    ['pri', 0.0]],
            [['pub', 0.9],   ['pub', 0.1],    ['pub', 0.0],    ['pri', 0.9],    ['pri', 0.0],    ['pri', 0.1]],
            [['pub', 0.9],   ['pub', 0.1],    ['pub', 0.0],    ['pri', 0.9],    ['pri', 0.1],    ['pri', 0.0]],

            [['pri', 0.0],   ['pri', 0.1],    ['pri', 0.9],    ['pub', 0.0],    ['pub', 0.9],    ['pub', 0.1]],
            [['pri', 0.0],   ['pri', 0.1],    ['pri', 0.9],    ['pub', 0.1],    ['pub', 0.0],    ['pub', 0.9]],
            [['pri', 0.0],   ['pri', 0.1],    ['pri', 0.9],    ['pub', 0.1],    ['pub', 0.9],    ['pub', 0.0]],
            [['pri', 0.0],   ['pri', 0.1],    ['pri', 0.9],    ['pub', 0.9],    ['pub', 0.0],    ['pub', 0.1]],
            [['pri', 0.0],   ['pri', 0.1],    ['pri', 0.9],    ['pub', 0.9],    ['pub', 0.1],    ['pub', 0.0]],
    

            [['pri', 0.0],   ['pri', 0.9],    ['pri', 0.1],    ['pub', 0.0],    ['pub', 0.9],    ['pub', 0.1]],
            [['pri', 0.0],   ['pri', 0.9],    ['pri', 0.1],    ['pub', 0.1],    ['pub', 0.0],    ['pub', 0.9]],
            [['pri', 0.0],   ['pri', 0.9],    ['pri', 0.1],    ['pub', 0.1],    ['pub', 0.9],    ['pub', 0.0]],
            [['pri', 0.0],   ['pri', 0.9],    ['pri', 0.1],    ['pub', 0.9],    ['pub', 0.0],    ['pub', 0.1]],
            [['pri', 0.0],   ['pri', 0.9],    ['pri', 0.1],    ['pub', 0.9],    ['pub', 0.1],    ['pub', 0.0]],
    

            [['pri', 0.1],   ['pri', 0.0],    ['pri', 0.9],    ['pub', 0.0],    ['pub', 0.9],    ['pub', 0.1]],
            [['pri', 0.1],   ['pri', 0.0],    ['pri', 0.9],    ['pub', 0.1],    ['pub', 0.0],    ['pub', 0.9]],
            [['pri', 0.1],   ['pri', 0.0],    ['pri', 0.9],    ['pub', 0.1],    ['pub', 0.9],    ['pub', 0.0]],
            [['pri', 0.1],   ['pri', 0.0],    ['pri', 0.9],    ['pub', 0.9],    ['pub', 0.0],    ['pub', 0.1]],
            [['pri', 0.1],   ['pri', 0.0],    ['pri', 0.9],    ['pub', 0.9],    ['pub', 0.1],    ['pub', 0.0]],
    

            [['pri', 0.1],   ['pri', 0.9],    ['pri', 0.0],    ['pub', 0.0],    ['pub', 0.9],    ['pub', 0.1]],
            [['pri', 0.1],   ['pri', 0.9],    ['pri', 0.0],    ['pub', 0.1],    ['pub', 0.0],    ['pub', 0.9]],
            [['pri', 0.1],   ['pri', 0.9],    ['pri', 0.0],    ['pub', 0.1],    ['pub', 0.9],    ['pub', 0.0]],
            [['pri', 0.1],   ['pri', 0.9],    ['pri', 0.0],    ['pub', 0.9],    ['pub', 0.0],    ['pub', 0.1]],
            [['pri', 0.1],   ['pri', 0.9],    ['pri', 0.0],    ['pub', 0.9],    ['pub', 0.1],    ['pub', 0.0]],
    

            [['pri', 0.9],   ['pri', 0.0],    ['pri', 0.1],    ['pub', 0.0],    ['pub', 0.9],    ['pub', 0.1]],
            [['pri', 0.9],   ['pri', 0.0],    ['pri', 0.1],    ['pub', 0.1],    ['pub', 0.0],    ['pub', 0.9]],
            [['pri', 0.9],   ['pri', 0.0],    ['pri', 0.1],    ['pub', 0.1],    ['pub', 0.9],    ['pub', 0.0]],
            [['pri', 0.9],   ['pri', 0.0],    ['pri', 0.1],    ['pub', 0.9],    ['pub', 0.0],    ['pub', 0.1]],
            [['pri', 0.9],   ['pri', 0.0],    ['pri', 0.1],    ['pub', 0.9],    ['pub', 0.1],    ['pub', 0.0]],
    

            [['pri', 0.9],   ['pri', 0.1],    ['pri', 0.0],    ['pub', 0.0],    ['pub', 0.9],    ['pub', 0.1]],
            [['pri', 0.9],   ['pri', 0.1],    ['pri', 0.0],    ['pub', 0.1],    ['pub', 0.0],    ['pub', 0.9]],
            [['pri', 0.9],   ['pri', 0.1],    ['pri', 0.0],    ['pub', 0.1],    ['pub', 0.9],    ['pub', 0.0]],
            [['pri', 0.9],   ['pri', 0.1],    ['pri', 0.0],    ['pub', 0.9],    ['pub', 0.0],    ['pub', 0.1]],
            [['pri', 0.9],   ['pri', 0.1],    ['pri', 0.0],    ['pub', 0.9],    ['pub', 0.1],    ['pub', 0.0]]
    
        ]

perms = [
            #Eli's permutations
            # pub and pri rebates in same order
            # this is the base permutation
            [['pub', 0.0],   ['pub', 0.1],    ['pub', 0.9],    ['pri', 0.0],    ['pri', 0.1],    ['pri', 0.9]],
            [['pub', 0.0],   ['pub', 0.9],    ['pub', 0.1],    ['pri', 0.0],    ['pri', 0.9],    ['pri', 0.1]],
            [['pub', 0.1],   ['pub', 0.0],    ['pub', 0.9],    ['pri', 0.1],    ['pri', 0.0],    ['pri', 0.9]],
            [['pub', 0.1],   ['pub', 0.9],    ['pub', 0.0],    ['pri', 0.1],    ['pri', 0.9],    ['pri', 0.0]],
            [['pub', 0.9],   ['pub', 0.0],    ['pub', 0.1],    ['pri', 0.9],    ['pri', 0.0],    ['pri', 0.1]],
            [['pub', 0.9],   ['pub', 0.1],    ['pub', 0.0],    ['pri', 0.9],    ['pri', 0.1],    ['pri', 0.0]],
            [['pri', 0.0],   ['pri', 0.1],    ['pri', 0.9],    ['pub', 0.0],    ['pub', 0.1],    ['pub', 0.9]],
            [['pri', 0.0],   ['pri', 0.9],    ['pri', 0.1],    ['pub', 0.0],    ['pub', 0.9],    ['pub', 0.1]],
            [['pri', 0.1],   ['pri', 0.0],    ['pri', 0.9],    ['pub', 0.1],    ['pub', 0.0],    ['pub', 0.9]],
            [['pri', 0.1],   ['pri', 0.9],    ['pri', 0.0],    ['pub', 0.1],    ['pub', 0.9],    ['pub', 0.0]],
            [['pri', 0.9],   ['pri', 0.0],    ['pri', 0.1],    ['pub', 0.9],    ['pub', 0.0],    ['pub', 0.1]],
            [['pri', 0.9],   ['pri', 0.1],    ['pri', 0.0],    ['pub', 0.9],    ['pub', 0.1],    ['pub', 0.0]], 

            # cols 4 and 5 switched
            [['pub', 0.0],   ['pub', 0.1],    ['pub', 0.9],    ['pri', 0.1],    ['pri', 0.0],    ['pri', 0.9]],
            [['pub', 0.0],   ['pub', 0.9],    ['pub', 0.1],    ['pri', 0.9],    ['pri', 0.0],    ['pri', 0.1]],
            [['pub', 0.1],   ['pub', 0.0],    ['pub', 0.9],    ['pri', 0.0],    ['pri', 0.1],    ['pri', 0.9]],
            [['pub', 0.1],   ['pub', 0.9],    ['pub', 0.0],    ['pri', 0.9],    ['pri', 0.1],    ['pri', 0.0]],
            [['pub', 0.9],   ['pub', 0.0],    ['pub', 0.1],    ['pri', 0.0],    ['pri', 0.9],    ['pri', 0.1]],
            [['pub', 0.9],   ['pub', 0.1],    ['pub', 0.0],    ['pri', 0.1],    ['pri', 0.9],    ['pri', 0.0]],
            [['pri', 0.0],   ['pri', 0.1],    ['pri', 0.9],    ['pub', 0.1],    ['pub', 0.0],    ['pub', 0.9]],
            [['pri', 0.0],   ['pri', 0.9],    ['pri', 0.1],    ['pub', 0.9],    ['pub', 0.0],    ['pub', 0.1]],
            [['pri', 0.1],   ['pri', 0.0],    ['pri', 0.9],    ['pub', 0.0],    ['pub', 0.1],    ['pub', 0.9]],
            [['pri', 0.1],   ['pri', 0.9],    ['pri', 0.0],    ['pub', 0.9],    ['pub', 0.1],    ['pub', 0.0]],
            [['pri', 0.9],   ['pri', 0.0],    ['pri', 0.1],    ['pub', 0.0],    ['pub', 0.9],    ['pub', 0.1]],
            [['pri', 0.9],   ['pri', 0.1],    ['pri', 0.0],    ['pub', 0.1],    ['pub', 0.9],    ['pub', 0.0]],

            # cols 5 and 6 switched
            [['pub', 0.0],   ['pub', 0.1],    ['pub', 0.9],    ['pri', 0.0],    ['pri', 0.9],    ['pri', 0.1]],
            [['pub', 0.0],   ['pub', 0.9],    ['pub', 0.1],    ['pri', 0.0],    ['pri', 0.1],    ['pri', 0.9]],
            [['pub', 0.1],   ['pub', 0.0],    ['pub', 0.9],    ['pri', 0.1],    ['pri', 0.9],    ['pri', 0.0]],
            [['pub', 0.1],   ['pub', 0.9],    ['pub', 0.0],    ['pri', 0.1],    ['pri', 0.0],    ['pri', 0.9]],
            [['pub', 0.9],   ['pub', 0.0],    ['pub', 0.1],    ['pri', 0.9],    ['pri', 0.1],    ['pri', 0.0]],
            [['pub', 0.9],   ['pub', 0.1],    ['pub', 0.0],    ['pri', 0.9],    ['pri', 0.0],    ['pri', 0.1]],
            [['pri', 0.0],   ['pri', 0.1],    ['pri', 0.9],    ['pub', 0.0],    ['pub', 0.9],    ['pub', 0.1]],
            [['pri', 0.0],   ['pri', 0.9],    ['pri', 0.1],    ['pub', 0.0],    ['pub', 0.1],    ['pub', 0.9]],
            [['pri', 0.1],   ['pri', 0.0],    ['pri', 0.9],    ['pub', 0.1],    ['pub', 0.9],    ['pub', 0.0]],
            [['pri', 0.1],   ['pri', 0.9],    ['pri', 0.0],    ['pub', 0.1],    ['pub', 0.0],    ['pub', 0.9]],
            [['pri', 0.9],   ['pri', 0.0],    ['pri', 0.1],    ['pub', 0.9],    ['pub', 0.1],    ['pub', 0.0]],
            [['pri', 0.9],   ['pri', 0.1],    ['pri', 0.0],    ['pub', 0.9],    ['pub', 0.0],    ['pub', 0.1]],

            # cols 4 and 6 switched
            [['pub', 0.0],   ['pub', 0.1],    ['pub', 0.9],    ['pri', 0.1],    ['pri', 0.9],    ['pri', 0.0]],
            [['pub', 0.0],   ['pub', 0.9],    ['pub', 0.1],    ['pri', 0.9],    ['pri', 0.1],    ['pri', 0.0]],
            [['pub', 0.1],   ['pub', 0.0],    ['pub', 0.9],    ['pri', 0.0],    ['pri', 0.9],    ['pri', 0.1]],
            [['pub', 0.1],   ['pub', 0.9],    ['pub', 0.0],    ['pri', 0.9],    ['pri', 0.0],    ['pri', 0.1]],
            [['pub', 0.9],   ['pub', 0.0],    ['pub', 0.1],    ['pri', 0.0],    ['pri', 0.1],    ['pri', 0.9]],
            [['pub', 0.9],   ['pub', 0.1],    ['pub', 0.0],    ['pri', 0.1],    ['pri', 0.0],    ['pri', 0.9]],
            [['pri', 0.0],   ['pri', 0.1],    ['pri', 0.9],    ['pub', 0.1],    ['pub', 0.9],    ['pub', 0.0]],
            [['pri', 0.0],   ['pri', 0.9],    ['pri', 0.1],    ['pub', 0.9],    ['pub', 0.1],    ['pub', 0.0]],
            [['pri', 0.1],   ['pri', 0.0],    ['pri', 0.9],    ['pub', 0.0],    ['pub', 0.9],    ['pub', 0.1]],
            [['pri', 0.1],   ['pri', 0.9],    ['pri', 0.0],    ['pub', 0.9],    ['pub', 0.0],    ['pub', 0.1]],
            [['pri', 0.9],   ['pri', 0.0],    ['pri', 0.1],    ['pub', 0.0],    ['pub', 0.1],    ['pub', 0.9]],
            [['pri', 0.9],   ['pri', 0.1],    ['pri', 0.0],    ['pub', 0.1],    ['pub', 0.0],    ['pub', 0.9]]

            # there are to my knowledge no other ways to permutate this here data
        ]
'''

# this is where models will look for the current experiment data. When you are done with it, put it at the bottom, commented out
data =  [   #first 12 permutations
            [['pub', 0.0],   ['pub', 0.1],    ['pub', 0.9],    ['pri', 0.0],    ['pri', 0.1],    ['pri', 0.9]],
            [['pub', 0.0],   ['pub', 0.9],    ['pub', 0.1],    ['pri', 0.0],    ['pri', 0.9],    ['pri', 0.1]],
            [['pub', 0.1],   ['pub', 0.0],    ['pub', 0.9],    ['pri', 0.1],    ['pri', 0.0],    ['pri', 0.9]],
            [['pub', 0.1],   ['pub', 0.9],    ['pub', 0.0],    ['pri', 0.1],    ['pri', 0.9],    ['pri', 0.0]],
            [['pub', 0.9],   ['pub', 0.0],    ['pub', 0.1],    ['pri', 0.9],    ['pri', 0.0],    ['pri', 0.1]],
            [['pub', 0.9],   ['pub', 0.1],    ['pub', 0.0],    ['pri', 0.9],    ['pri', 0.1],    ['pri', 0.0]],
            [['pri', 0.0],   ['pri', 0.1],    ['pri', 0.9],    ['pub', 0.0],    ['pub', 0.1],    ['pub', 0.9]],
            [['pri', 0.0],   ['pri', 0.9],    ['pri', 0.1],    ['pub', 0.0],    ['pub', 0.9],    ['pub', 0.1]],
            [['pri', 0.1],   ['pri', 0.0],    ['pri', 0.9],    ['pub', 0.1],    ['pub', 0.0],    ['pub', 0.9]],
            [['pri', 0.1],   ['pri', 0.9],    ['pri', 0.0],    ['pub', 0.1],    ['pub', 0.9],    ['pub', 0.0]],
            [['pri', 0.9],   ['pri', 0.0],    ['pri', 0.1],    ['pub', 0.9],    ['pub', 0.0],    ['pub', 0.1]],
            [['pri', 0.9],   ['pri', 0.1],    ['pri', 0.0],    ['pub', 0.9],    ['pub', 0.1],    ['pub', 0.0]]
        ]

# exports data to a csv format
def export_csv(fname, data):
    with open(fname + '.csv', 'w') as f:

        # write header for csv
        for index, _ in enumerate(data[0]):
            s = 'round_' + str(index + 1) + '_mode,round_' + str(index + 1) + '_rebate'
            if index != len(data[0]) - 1:
                s += ','
            f.write(s)
        f.write('\n')
        
        # write data
        # each line of data represents a player,
        # and each list within that holds data for a round
        for subject in data:
            for index, period in enumerate(subject):
                s = period[0] + ',' + str(period[1])
                if index != len(subject) - 1:
                    s += ','
                f.write(s)
            f.write('\n')

# exports data to models.py
# formats data to make it easier for models.py to parse it
def export_data():
    for player in data:
        for period in player:
            if period[0] == 'pub':
                period[0] = 'public'
            elif period[0] == 'pri':
                period[0] = 'private'
            period[1] += 1.0
    return data

'''
This is where old experiment data goes. 
Before you put it here, you can export it to CSV format 
if you want, passing in the current date and session
as the filename and data as the data.



'''

