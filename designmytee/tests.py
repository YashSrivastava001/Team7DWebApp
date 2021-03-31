from django.test import TestCase
from designmytee.models import Host, Designer, Submission, Competition, Support_Request 

# Create your tests here.

class CompetitionTests(TestCase):
    def test_start_is_not_before_end(self):
        start_date_question = Competition(startDate="2021-03-21", endDate="2021-04-21")
        self.assertIs(start_date_question.start_date_before_end_date(), True)