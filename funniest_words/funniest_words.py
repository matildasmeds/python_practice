# Count a funniness-score for each word in the Finnish
# classic "Alastalon Salissa".
# Full instructions in Finnish at https://wunder.dog/hassuimmat-sanat
import re
def how_funny(word):
    wovels = re.findall("[aeiouyäö]+", word)
    score = 0
    for group in wovels:
       score += len(group) * (2 ** len(group))
    return score

def funny_words(lines):
    results = {}
    for line in lines:
        for word in line.split(' '):
            score = how_funny(word)
            if score not in results:
                results[score] = []
            results[score].append(word)
    return results

def main():
    f = open("alastalon_salissa.txt")
    lines = f.readlines()
    results = funny_words(lines)
    max_funny = max(results.keys())
    print("Max funny score: " + str(max_funny))
    print("Funniest word(s): ")
    for result in results[max_funny]:
      print(str(result))

if __name__=="__main__":
    main()
