from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Eli Pandolfo'

doc = """
    Players choose to either donate to charity or keep 
    money for themselves, given different incentives.
"""


class Constants(BaseConstants):
    name_in_url = 'Donations'
    players_per_group = None
    num_rounds = 6
    endowment = c(10)
    participation_fee = c(5)

    # there are six rounds, and for right now they are all predetermined.
    # We can change this to a config file at some point.

    # each round is either public or private, and has a % rebate
    round_data = [
        {'mode': 'private', 'rebate': 1.0},
        {'mode': 'private', 'rebate': 1.1},
        {'mode': 'private', 'rebate': 1.9},
        {'mode': 'public', 'rebate': 1.0},
        {'mode': 'public', 'rebate': 1.1},        
        {'mode': 'public', 'rebate': 1.9} 
    ]

class Player(BasePlayer):
    time_Instructions = models.TextField()
    time_Decision = models.TextField()
    time_Results = models.TextField()

    # players can donate some money, keep some money, and sometimes get a rebate
    # on their donation
    money_kept = models.FloatField()
    money_donated = models.FloatField(min=0, max=10) # make only integers

    # pr is the paying round: this is randomly chosen 
    # in the Results class in Pages.py
    def set_payoffs(self, pr):
        # gets money kept in paying round
        kept = self.in_round(pr).money_kept

        # multiplies money kept by rebate to get total payoff
        self.payoff = kept * Constants.round_data[pr - 1]['rebate']
    
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass
