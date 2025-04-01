import argparse
import re
from collections import Counter
import string

def load_stop_words():
    return {
        "the", "and", "is", "in", "it", "to", "of", "a", "an", "for", "on", 
        "that", "this", "with", "as", "by", "or", "are", "be", "at", "was", 
        "were", "have", "has", "had", "i", "you", "he", "she", "we", "they"
    }

def analyze_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    
    sentences = re.split(r'[.!?]+(?:\s+|$)', text)
    num_sentences = len([s for s in sentences if s.strip()])

    
    translator = str.maketrans('', '', string.punctuation)
    words = [
        word.translate(translator).lower() 
        for word in text.split() 
        if word.translate(translator)
    ]
    total_words = len(words)

    
    stop_words = load_stop_words()
    filtered_words = [word for word in words if word not in stop_words]
    word_freq = Counter(filtered_words).most_common(5)

    avg_length = sum(len(word) for word in words) / total_words if total_words else 0

    return {
        'total_words': total_words,
        'top_words': word_freq,
        'avg_word_length': round(avg_length, 2),
        'num_sentences': num_sentences
    }

def main():
    parser = argparse.ArgumentParser(description='Analyze text file statistics.')
    parser.add_argument('file', help='Path to the text file')
    args = parser.parse_args()

    results = analyze_file(args.file)

    print(f"File Analysis Report:")
    print(f"Total words: {results['total_words']}")
    print(f"Top 5 frequent words (excluding stop words):")
    for word, freq in results['top_words']:
        print(f"  - {word}: {freq} occurrences")
    print(f"Average word length: {results['avg_word_length']} characters")
    print(f"Number of sentences: {results['num_sentences']}")

if __name__ == "__main__":
    main()