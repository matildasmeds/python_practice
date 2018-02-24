import unittest
import funniest_words

class TestFunniestWords(unittest.TestCase):

  def test_how_funny(self):
    score = funniest_words.how_funny("hääyöaie")
    self.assertEqual(score, 896)

if __name__ == "__main__":
  unittest.main()
