import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is link for [google](https://google.com)"
        )
        self.assertListEqual([("google", "https://google.com")], matches)


    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is text with two images, one is ![image](https://i.imgur.com/zjjcJKZ.png) and another is ![this one](https://i.imgur.com/foobar.png)"
        )
        self.assertListEqual([
            ("image", "https://i.imgur.com/zjjcJKZ.png"),
            ("this one", "https://i.imgur.com/foobar.png"),
        ], matches)


    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "This is link for [google](https://google.com), and [this is for](https://bing.com)"
        )
        self.assertListEqual([
            ("google", "https://google.com"),
            ("this is for", "https://bing.com"),
        ], matches)

    def test_extract_markdown_links_none(self):
        matches = extract_markdown_links(
            "There is no link here"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images_none(self):
        matches = extract_markdown_images(
            "There are no images here"
        )
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()