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
        1: 'Santa Cruz Education Foundation',
        2: 'Año Nuevo Research at UCSC',
        3: 'Santa Cruz Homeless Garden Project',
        4: 'Santa Cruz Humane Society'
    }


class Player(BasePlayer):
    time_Facebook = models.LongStringField()
    time_Instructions = models.LongStringField()
    time_ControlQuestions = models.LongStringField()
    time_Charity = models.LongStringField()
    time_TaskInstructions = models.LongStringField()
    time_Decision = models.LongStringField()
    time_Results = models.LongStringField()
    time_Survey = models.LongStringField()

    # players first choose a charity.
    # otree's dropdown menus need to return an integer
    charity = models.IntegerField(
        choices=[
            # these names can be changed to anything
            [1, Constants.charity_map[1]],
            [2, Constants.charity_map[2]],
            [3, Constants.charity_map[3]],
            [4, Constants.charity_map[4]]])

    money_kept = models.FloatField()
    money_donated = models.IntegerField()
    mode = models.LongStringField()
    rebate = models.FloatField()

    # this is the charity's name. It gets returned in Decision and results
    charity_dec = models.LongStringField()

    #facebook page
    FB_name = models.StringField()
    FB_ID = models.StringField()

    # results page
    chosen_pr = models.IntegerField()
    chosen_mode = models.StringField()
    chosen_charity = models.StringField()
    chosen_rebate = models.FloatField()
    chosen_donation = models.FloatField()

    # survey
    s1 = models.StringField()
    s2 = models.IntegerField(min=1, max=10)
    s3a = models.IntegerField()
    s3b = models.IntegerField()
    s4a = models.IntegerField()
    s4b = models.IntegerField()
    s5a = models.IntegerField()
    s5b = models.IntegerField()

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
