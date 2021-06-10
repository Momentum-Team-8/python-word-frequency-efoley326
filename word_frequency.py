STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
import string
def print_word_freq(file):
    with open(file) as one_today:
        text = one_today.readwords()
    
    for words in text:
        words = words.lower()
        words = words.split()
        words = words.strip('''!()-[]{};:'"\, <>./?@#$%^&*_~-''')
    words_to_keep = ""
    for words in file:
        if words == STOP_WORDS:
            words == None
    return words_to_keep


def count_words(dict):
    for word in print_word_freq:
        a = { word } 
    for word in a:
        if word in a:
            a[word] = a[word] + 1
    sort_a = sorted(a.items(), key=lambda x: x[1], reverse=True)
    for i in sort_a:
	    print(i[0], i[1])


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
