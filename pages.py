from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

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
            mode = Constants.round_data[self.participant.id_in_session - 1][rn - 1][0]
            prev_mode = Constants.round_data[self.participant.id_in_session - 1][rn - 2][0]
            if not (mode == prev_mode):
                return True
            return False

    def vars_for_template(self):
        return {
            'mode': Constants.round_data[self.participant.id_in_session - 1][self.round_number - 1][0].capitalize(),
        }

# Decision page. Includes instrucitons, and returns some input form fields for ease of recording data
class Decision(Page):
    form_model = 'player'
    form_fields = ['time_Decision', 'money_kept', 'money_donated', 'mode', 'rebate', 'charity_dec']

    def vars_for_template(self):
        return {
            'mode': Constants.round_data[self.participant.id_in_session - 1][self.round_number - 1][0],
            'rebate': round((Constants.round_data[self.participant.id_in_session - 1][self.round_number - 1][1] - 1) * 100),
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

        # set payoffs
        pr = self.participant.vars['pr']
        self.player.set_payoffs(pr)
        payoff = self.player.payoff
        donation = self.player.in_round(pr).money_donated

        # we don't need to return the payoff here because it is
        # automatically passed to templates
        return {
            'pr': pr,
            'mode': Constants.round_data[self.participant.id_in_session - 1][pr - 1][0],
            'rebate': round((Constants.round_data[self.participant.id_in_session - 1][pr - 1][1] - 1) * 100),
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
