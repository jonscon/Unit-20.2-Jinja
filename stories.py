"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(
                "simple",
                "A Simple Tale",
                ["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code
        self.title = title
        self.words = words
        self.prompt = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.prompt

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# List of Stories

story1 = Story(
    "history",
    "A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "zoo",
    "A Day at the Zoo",
    ["adjective", "animal", "verb", "adverb"],
    """Today, I went to the zoo and saw a(n) {adjective} {animal} jumping
        up and down from the tree. He proceeded to {verb} {adverb} through the tunnel
        and led us to its humble abode!"""
)

story3 = Story(
    "game",
    "Star Wars",
    ["noun", "name", "verb_singular", "adverb", "weapon"],
    """In the game Star Wars, you are Luke Skywalker and you try to destroy
        every {noun} possible. Your worst enemy, {name}, appears out of thin
        air and {verb_singular} {adverb} at you. In their hand appears a {weapon},
        and you commence your battle."""
)

# Create a dictionary to store these stories, with code and story instance as key value pairs.

stories = {story.code:story for story in [story1, story2, story3]}