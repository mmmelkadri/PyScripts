import glob
import os
import re
import argparse

# HOW: searches all files in all subdirectories of current working directory and prints out all lines
# containing the given word/words.
# Words must be in quotes, and you can input multiple words in separate quotes to only output lines that contain all the
# words. Is case-sensitive.
# example: python find.py -b
#          >> "This" "That"
# -b to make the given word bold in the output.

no_case = False
bold = False


# atoi and natural_keys from
# https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside
def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    # alist.sort(key=natural_keys) sorts in human order
    # http://nedbatchelder.com/blog/200712/human_sorting.html
    # (See Toothy's implementation in the comments)
    return [atoi(c) for c in re.split(r'(\d+)', text)]


def find_word_in_text(text_io, words, filename):
    lines = text_io.readlines()
    for line in lines:
        if all(x in line for x in words):
            if bold:
                for word in words:
                    line = line.replace(word, '\033[1m' + word + '\033[0m')  # Bold the word in words
            print(line.strip())
            print(filename + '\n')


parser = argparse.ArgumentParser()

parser.add_argument("-b", "--bold", action='store_true', help="bold found words")

args = parser.parse_args()

if args.bold:
    bold = True

path = os.getcwd() + '/'
find_word = input()

word_list = re.findall("\"(.*?)\"", find_word)
files = glob.glob(path + '**/' + '*.txt', recursive=True)

files.sort(key=natural_keys)

for file in files:
    infile = open(file)
    find_word_in_text(infile, word_list, file.removeprefix(path))
