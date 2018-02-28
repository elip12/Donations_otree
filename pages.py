from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Instructions(Page):
    form_model = 'player'
    form_fields = ['time_Instructions']

    # only display this page in round 1
    def is_displayed(self):
        return self.round_number == 1

# add taskinstructions page

class Decision(Page):
    form_model = 'player'
    form_fields = ['time_Decision', 'money_kept', 'money_donated']

    def vars_for_template(self):
        return {
            'mode': Constants.round_data[self.round_number - 1]['mode'],
            'rebate': round((Constants.round_data[self.round_number - 1]['rebate'] - 1) * 100),
            'round_num': self.round_number
        }

# displays player's round and payoff
class Results(Page):
    form_model = 'player'
    form_fields = ['time_Results']

    # only display this page in the final round after all decisions
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        # get paying round
        pr = random.randrange(1, 7, 1)
        self.player.set_payoffs(pr)

        # we don't need to return the payoff here because it is
        # automatically passed to templates
        return {'pr': pr}


page_sequence = [
    Instructions,
    Decision,
    Results
]
