import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_simple(self):
        md = "# Title"
        extracted = extract_title(md)
        self.assertEqual(
            extracted,
            "Title",
        )

    def test_extract_title_complex(self):
        md = """
## Not this one

### Def not this one

It will never be _this_ one

And **this** is the worst one

# But this is good
"""
        extracted = extract_title(md)
        self.assertEqual(
            extracted,
            "But this is good",
        )


if __name__ == "__main__":
    unittest.main()