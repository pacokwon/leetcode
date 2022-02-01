# Capitalize the Title

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        def transform(word):
            if len(word) <= 2:
                return word.lower()
            else:
                return word[0].upper() + word[1:].lower()

        return ' '.join([transform(word) for word in title.split()])


