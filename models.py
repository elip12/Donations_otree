from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from . import config
import random


author = 'Eli Pandolfo'

doc = """
    Players choose to either donate to charity or keep 
    money for themselves, given different incentives.
"""


class Constants(BaseConstants):

    # each round is either public or private, and has a % rebate
    round_data = config.export_data()

    name_in_url = 'Donations'
    players_per_group = None
    num_rounds = len(round_data[0])
    endowment = 10
    participation_fee = 5

    # otree dropdown menu only returns intgers, here we map them
    # to strings representing the charity names
    charity_map = {
        1: 'Save the Dinosaurs',
        2: 'World Multistrata Agroforestry Fund',
        3: 'Combjellies Are People Too!',
        4: 'Washed Up Movie Stars Rehab Fund'
    }


class Player(BasePlayer):
    time_Instructions = models.TextField()
    time_Charity = models.TextField()
    time_TaskInstructions = models.TextField()
    time_Decision = models.TextField()
    time_Results = models.TextField()

    # players first choose a charity.
    # players can donate some money, keep some money, and sometimes get a rebate
    # on their donation
    charity = models.IntegerField(
        choices=[
            # these names can be changed to anything
            [1, Constants.charity_map[1]], 
            [2, Constants.charity_map[2]], 
            [3, Constants.charity_map[3]], 
            [4, Constants.charity_map[4]]])

    money_kept = models.FloatField()
    money_donated = models.FloatField() # make only integers
    mode = models.TextField()
    rebate = models.FloatField()
    charity_dec = models.TextField()

    # pr is the paying round: this is randomly chosen 
    # in the Results class in Pages.py
    def set_payoffs(self, pr):
        # gets money kept in paying round
        kept = self.in_round(pr).money_kept
        donated = self.in_round(pr).money_donated
        rebate = Constants.round_data[self.participant.id_in_session - 1][pr - 1][1]

        # multiplies money kept by rebate to get total payoff
        self.payoff = kept + (donated * (rebate - 1))
    
class Subsession(BaseSubsession):
    
    def creating_session(self):
        # set paying round
        for p in self.get_players():
            p.participant.vars['pr'] = random.randrange(1, Constants.num_rounds + 1, 1)


class Group(BaseGroup):
    pass
