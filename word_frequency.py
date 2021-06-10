STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
import string
def print_word_freq(file):
    with open(file) as file:
        text = file.readlines()
    
    for words in text:
        words = words.lower()
        words = words.split()
    words_to_keep = ""
    for words in text:
        if words == STOP_WORDS:
            words == None
    for words in text:
        a = { words } 
    for words in a:
        if words in a:
            a[words] = a[words] + 1
    print (sorted(a.items(), key=lambda x: x[1], reverse=True))
    # for words in sorted:
	#     print(words[0], words[1])

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
