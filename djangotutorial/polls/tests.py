import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


def create_question(question_text, days_offset):
    return Question.objects.create(
        question_text=question_text,
        pub_date=timezone.now() + datetime.timedelta(days=days_offset),
    )


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_old_question(self):
        old_question = create_question("Old question", days_offset=-2)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        recent_question = create_question("Recent question", days_offset=-0.5)
        self.assertIs(recent_question.was_published_recently(), True)


class IndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_with_one_question(self):
        created_question = create_question("Test question", days_offset=-1)

        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test question")
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [created_question],
            transform=lambda question: question,
        )
