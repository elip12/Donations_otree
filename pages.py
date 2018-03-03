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

class Charity(Page):
    form_model = 'player'
    form_fields = ['time_Charity', 'charity']

    def is_displayed(self):
        return self.round_number == 1

class TaskInstructions(Page):
    form_model = 'player'
    form_fields = ['time_TaskInstructions']

    def is_displayed(self):
        rn = self.round_number

        if rn == 1:
            return True
        else:
            mode = Constants.round_data[rn - 1]['mode']
            prev_mode = Constants.round_data[rn - 2]['mode']
            if not (mode == prev_mode):
                return True
            return False

    def vars_for_template(self):
        return {
            'mode': Constants.round_data[self.round_number - 1]['mode'].capitalize(),
        }

# Decision page. Includes instrucitons, and returns some input form fields for ease of recording data
class Decision(Page):
    form_model = 'player'
    form_fields = ['time_Decision', 'money_kept', 'money_donated', 'mode', 'rebate', 'charity_dec']

    def vars_for_template(self):
        return {
            'mode': Constants.round_data[self.round_number - 1]['mode'],
            'rebate': round((Constants.round_data[self.round_number - 1]['rebate'] - 1) * 100),
            'round_num': self.round_number,
            'charity': Constants.charity_map[self.player.in_round(1).charity]
        }


# displays chosen round and player's payoff,
# as well as a thank you message
class Results(Page):
    form_model = 'player'
    form_fields = ['time_Results']

    # only display this page in the final round after all decisions
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        # get paying round
        pr = random.randrange(1, Constants.num_rounds + 1, 1)
        self.player.set_payoffs(pr)
        payoff = self.player.payoff
        donation = self.player.in_round(pr).money_donated

        # we don't need to return the payoff here because it is
        # automatically passed to templates
        return {
            'pr': pr,
            'mode': Constants.round_data[pr - 1]['mode'],
            'rebate': round((Constants.round_data[pr - 1]['rebate'] - 1) * 100),
            'charity': Constants.charity_map[self.player.in_round(1).charity],
            'payoff': payoff,
            'donation': round(donation)
        }


page_sequence = [
    Instructions,
    Charity,
    TaskInstructions,
    Decision,
    Results
]
