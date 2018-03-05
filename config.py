# config file for Donations otree experiment
# Rachel Zhang, Eli Pandolfo
# There will never be more than 12 participants.
# Each participant is given a participant code by the room


data =  [
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
def export_csv(fname):
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

