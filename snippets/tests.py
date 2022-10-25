from django.test import TestCase, Client
from snippets.models import Snippet, Language
from django.test.client import RequestFactory
from snippets.views import home, add_snippet


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
        self.factory = RequestFactory()

    def test_snippets_displayed_on_home_page(self):
        req = self.factory.get("")
        res = home(req)
        assert res.status_code == 200
        assert b"Django block of code" in res.content
        assert b"React block of code" in res.content

    def test_snippets_created_using_form(self):
        snippet_object = {
            'title': 'Another Django block of code',
            'language': 1,
            'description': 'def python_function(): return None'
        }
        add_req = self.factory.post("add_snippet", snippet_object)
        print(add_snippet(add_req))
        home_res = home(self.factory.get(""))
        assert home_res.status_code == 200
        assert b"Another Django block of code" in home_res.content

    
