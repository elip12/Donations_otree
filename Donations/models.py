from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from . import config
import random
from django.forms import widgets

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
    participation_fee = 4

    # otree dropdown menu only returns intgers, here we map them
    # to strings representing the charity names
    charities = [
        'WHO COVID-19 Response Fund',
        'Año Nuevo Research at UCSC',
        'Santa Cruz Homeless Garden Project',
        'UCSF COVID-19 Response Fund',
        'Santa Cruz County Animal Shelter',
        'UCSC COVID-19 Slug Support Campaign'
    ]


class Player(BasePlayer):
    #time_Facebook = models.LongStringField()
    time_Instructions = models.LongStringField()
    time_tetris = models.LongStringField()
    time_TetrisResults = models.LongStringField()
    time_Charity = models.LongStringField()
    time_ControlQuestions = models.LongStringField()  
    time_ModeInstructionsCQ = models.LongStringField()
    time_InstructionSummary = models.LongStringField()
    time_TaskInstructions = models.LongStringField()
    time_Decision = models.LongStringField()
    time_Results = models.LongStringField()
    time_Survey = models.LongStringField()

    endowment = models.IntegerField()
    # players first choose a charity.
    # otree's dropdown menus need to return an integer
    charity = models.IntegerField()
    donated_yes_no = models.BooleanField(
        choices=[[0, 'No'], [1, 'Yes']],
        widget=widgets.RadioSelect)
    money_kept = models.FloatField(widget=widgets.TextInput(attrs={'autocomplete': 'off'}))
    money_donated = models.IntegerField(widget=widgets.TextInput(attrs={'autocomplete': 'off'}))

    mode = models.LongStringField()
    rebate = models.FloatField()

    # this is the charity's name. It gets returned in Decision and results
    charity_dec = models.LongStringField()

    #facebook page
    FB_name = models.StringField(widget=widgets.TextInput(attrs={'autocomplete': 'off'}))
    FB_ID = models.StringField(widget=widgets.TextInput(attrs={'autocomplete': 'off'}))

    # results page
    chosen_pr = models.IntegerField()
    chosen_mode = models.StringField()
    chosen_charity = models.StringField()
    chosen_rebate = models.FloatField()
    chosen_donation = models.FloatField()

    # survey
    s1 = models.StringField(widget=widgets.TextInput(attrs={'autocomplete': 'off'}))
    s2 = models.IntegerField(widget=widgets.NumberInput(attrs={'autocomplete': 'off'}))
    s3 = models.StringField(widget=widgets.TextInput(attrs={'autocomplete': 'off'}))
    s4 = models.StringField(widget=widgets.TextInput(attrs={'autocomplete': 'off'}))
    s5 = models.BooleanField(
        choices=[[0, 'No'], [1, 'Yes']],
        widget=widgets.RadioSelect)
    s6 = models.IntegerField(
        choices=[
            [0, 'No'],
            [1, 'Yes, part-time'],
            [2, 'Yes, full-time']],
        widget=widgets.RadioSelect)
    s7 = models.IntegerField()
    s8 = models.IntegerField(widget=widgets.RadioSelect)
    s9a = models.IntegerField()
    s9b = models.IntegerField()
    s10a = models.IntegerField()
    s10b = models.IntegerField()
    s11a = models.IntegerField()
    s11b = models.IntegerField()
    s12 = models.IntegerField(
        choices=[
            [0, 'At least once a day'],
            [1, 'At least once a week'],
            [2, 'At least once a month'],
            [3, 'I rarely use Facebook']],
        widget=widgets.RadioSelect)
    s13 = models.StringField(widget=widgets.TextInput(attrs={'autocomplete': 'off'}))
    s14 = models.IntegerField(
        choices=[
            [0, 'The rebate makes my donation appear less generous'],
            [1, 'The rebate has an advertising effect that will attract more friends to donate']],
        widget=widgets.RadioSelect)
    s15a = models.IntegerField(widget=widgets.NumberInput(attrs={'autocomplete': 'off'}), label='Thank you, \'your name\', for donating $10 to ARC!')
    s15b = models.IntegerField(widget=widgets.NumberInput(attrs={'autocomplete': 'off'}), label='Thank you, \'your name\', for donating $10 to ARC, with the LEEPS Lab offering a $5 rebate to you!')
    s15c = models.IntegerField(widget=widgets.NumberInput(attrs={'autocomplete': 'off'}), label='Thank you, \'your name\', for donating $5 to ARC, with the LEEPS Lab matching $5. ARC received $10 total in donations!')

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
            p.participant.vars['charities'] = random.sample(Constants.charities, k=len(Constants.charities))


class Group(BaseGroup):
    pass
