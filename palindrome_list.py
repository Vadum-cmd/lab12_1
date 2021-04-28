"""
Palindrome class realization.
"""
from arraystack import ArrayStack   # or from linkedstack import LinkedStack


class Palindrome:
    """Initialize new class Palindrome."""
    def find_palindromes(self, start_file: str, result_file: str) -> list:
        """The function returns True if the word is a palindrome."""
        input_words = self.read_file(start_file)
        result_words = []
        stack = ArrayStack()

        for word in input_words:
            for letter in word:
                stack.push(letter)

            reversed_line = ''

            while not stack.isEmpty():
                reversed_line += stack.pop()

            if word == reversed_line:
                result_words.append(word)

        if len(result_words) != 0:
            self.write_file(result_words, result_file)
        return result_words

    def read_file(self, file_name: str):
        """This func reads file and returns a list of words."""
        file_text = []
        with open(file_name, encoding='utf-8', errors='ignore') as file:
            for line in file:
                line = line.strip()
                file_text.append(line)
        return file_text

    def write_file(self, lst_of_palidroms: list, result_file: str):
        """The function writes all palindroms in file."""
        with open(result_file, 'w', encoding='utf-8', errors='ignore') as result:
            for word in lst_of_palidroms:
                result.write(word + '\n')


# if __name__ == "__main__":
#     palindrome = Palindrome()
#     palindrome.find_palindromes("base.lst", "palindrome_uk.txt")
#     palindrome.find_palindromes("words.txt", "palindrome_en.txt")
