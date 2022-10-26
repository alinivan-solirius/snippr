from django.test import TestCase, Client
from snippets.models import Snippet, Language
from django.test.client import RequestFactory
from snippets.views import home, add_snippet, edit_snippet


class SnippetTestCase(TestCase):
    def setUp(self):
        Snippet.objects.create(
            title='Django block of code',
            language=Language.objects.create(title='Python'),
            description="def python_function(): return None"
        )
        Snippet.objects.create(
            title='React block of code',
            language=Language.objects.create(title='JavaScript'),
            description="function reactComponent(props): return <><h1>Hello {props.name}</h1><>"
        )
        self.snippet_object = {
            'title': 'Another Django block of code',
            'language': 1,
            'description': 'def python_function(): return None'
        }
        self.client = Client(enforce_csrf_checks=True)
        self.factory = RequestFactory()

    def test_snippets_displayed_on_home_page(self):
        req = self.factory.get("")
        res = home(req)
        assert res.status_code == 200
        assert b"Django block of code" in res.content
        assert b"React block of code" in res.content

    def test_snippets_created_using_form(self):
        Snippet.objects.create(
            title='Another Django block of code',
            language=Language.objects.create(title='Python'),
            description="def python_function(): return None"
        )
        req = self.factory.get("", follow=True)
        res = home(req)
        assert res.status_code == 200
        assert b"Another Django block of code" in res.content

    def test_snippets_delete_with_confirmation(self):
        self.factory.get("delete_snippet/1/")
        self.factory.delete("edit_snippet/1/")
        res = home(self.factory.get(""))
        assert res.status_code == 200
        assert b"Django block of code" in res.content
