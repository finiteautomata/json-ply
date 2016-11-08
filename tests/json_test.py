import unittest
from jsonparse import parse

class JsonParseTest(unittest.TestCase):
    def test_converts_empty_json_to_empty_dict(self):
        self.assertEqual(parse("{}"), {})

    def test_converts_json_with_one_definition(self):
        self.assertEqual(parse("""
            {
                \"a\": \"bcd\"
            }"""), {'a': 'bcd'})

    def test_converts_with_multiple_definitions(self):
        json_str = """
            {
              "a": "b",
              "c": 1
            }
        """

        self.assertEqual(parse(json_str), {'a': 'b', 'c': 1})

    def test_supports_recursive_structures(self):

        json_str = """
            {
                "a": {
                    "b" : 1
                }
            }
        """

        self.assertEqual(parse(json_str), {'a': {'b': 1}})

    def test_parses_arrays(self):
        json_str = """
            ["foo", "bar"]
        """

        self.assertEqual(parse(json_str), ['foo', 'bar'])

    def test_twice_nested_object(self):
        json_str = """
            {
                "a": [
                    {"b" : 1},
                    {"c" : []}
                ]
            }
        """

        self.assertEqual(parse(json_str), {
                "a": [
                    { "b" : 1 },
                    { "c" : []}
                ]
            })

    def test_it_returns_none_when_not_correct(self):
        self.assertIsNone(parse('''[[]}'''))