from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Facebook(Page):
    form_model = 'player'
    form_fields = ['time_Facebook', 'FB_name', 'FB_ID']

    def is_displayed(self):
        return self.round_number == 1

class Instructions(Page):
    form_model = 'player'
    form_fields = ['time_Instructions']

    # only display this page in round 1
    def is_displayed(self):
        return self.round_number == 1

class Charity(Page):
    form_model = 'player'
    form_fields = ['time_Charity', 'charity']

    def charity_choices(self):
        return [[i, self.participant.vars['charities'][i]] for i in range(len(Constants.charities))]

    def vars_for_template(self):
        rnd_charities = [str(i) for i in range(len(Constants.charities))]
        random.shuffle(rnd_charities)

        return {'rnd_charities': rnd_charities}

    def is_displayed(self):
        return self.round_number == 1

class Tetris(Page):
    form_model = 'player'
    form_fields = ['endowment']
    timeout_seconds = 600

    def is_displayed(self):
        return self.round_number == 1

class ControlQuestions(Page):
    form_model = 'player'
    form_fields = ['time_ControlQuestions']

    def is_displayed(self):
        return self.round_number == 1


class ModeInstructionsCQ(Page):
    form_model = 'player'
    form_fields = ['time_ModeInstructionsCQ']

    def is_displayed(self):
        return self.round_number == 1

class InstructionSummary(Page):
    form_model = 'player'
    form_fields = ['time_InstructionSummary']

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {'charity': self.participant.vars['charities'][self.player.in_round(1).charity]}

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
    form_fields = ['time_Decision', 'donated_yes_no', 'money_kept', 'money_donated', 'mode', 'rebate', 'charity_dec']

    def vars_for_template(self):
        if self.round_number > 1:
            self.player.endowment = self.player.in_round(1).endowment
        return {
            'total_cash_available': self.player.endowment + Constants.participation_fee,
            'mode': Constants.round_data[self.participant.id_in_session - 1][self.round_number - 1][0].capitalize(),
            'rebate': round((Constants.round_data[self.participant.id_in_session - 1][self.round_number - 1][1] - 1) * 100),
            'round_num': self.round_number,
            'charity': self.participant.vars['charities'][self.player.in_round(1).charity]
        }


# displays chosen round and player's payoff,
# as well as a thank you message
class Results(Page):
    form_model = 'player'
    form_fields = ['time_Results', 'chosen_pr', 'chosen_mode', 'chosen_charity', 'chosen_rebate', 'chosen_donation']

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
            'charity': self.participant.vars['charities'][self.player.in_round(1).charity],
            'payoff': payoff,
            'donation': round(donation)
        }

class Survey(Page):
    form_model = 'player'

    def get_pub_90_don(self):
        rn = -1
        # add clear documetnation here for why this is here
        for index, round_data in enumerate(Constants.round_data[self.participant.id_in_session - 1]):
            if round_data[0] == 'public' and round_data[1] == 1.9:
                rn = index + 1
                break

        donation = self.player.in_round(rn).money_donated
        return donation

    def s8_choices(self):
        don = self.get_pub_90_don()
        charity = self.player.in_round(1).charity_dec
        return [
            [0, 'Donate $0 and have no message posted on your Facebook'],
            [1, 'Donate $' + str(don) + ' and have the message "Thank you for donating $'
                + str(don) + ' to ' + charity + ' with a 90% rebate support by UCSC \
                LEEPS Lab!" posted on your Facebook']
        ]

    def vars_for_template(self):
        don = self.get_pub_90_don()
        if don == 0:
            q9 = '8'
            q10 = '9'
            q11 = '10'
        else:
            q9 = '9'
            q10 = '10'
            q11 = '11'

        s9_r = random.randint(0, 10)
        s10_r = random.randint(0, 10)
        s11_r = random.randint(0, 10)

        return {
            's7_initial': random.randint(1, 10),
            's9_r': s9_r,
            's9_l': 10 - s9_r,
            's10_r': s10_r,
            's10_l': 10 - s10_r,
            's11_r': s11_r,
            's11_l': 10 - s11_r,
            'pub_90_don': don,
            'q9': q9,
            'q10': q10,
            'q11': q11
        }

    def get_form_fields(self):
        don = self.get_pub_90_don()
        if don == 0:
            return ['time_Survey', 's1', 's2', 's3', 's4', 's5', 's6','s7',
                's9a', 's9b', 's10a', 's10b', 's11a', 's11b']
        else:
            return ['time_Survey', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8',
                's9a', 's9b', 's10a', 's10b', 's11a', 's11b']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def error_message(self, values):
        if values['s9a'] + values['s9b'] != 10 or values['s10a'] + values['s10b'] != 10 or values['s11a'] + values['s11b'] != 10:
            return 'The numbers must add up to 10'


page_sequence = [
#   Facebook,
    Instructions,
    Charity,
    Tetris,
    ControlQuestions,   
    ModeInstructionsCQ,
    InstructionSummary,
#    TaskInstructions,
    Decision,
    Results,
    Survey
]
