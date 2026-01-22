#!/usr/bin/env python3
"""Pick a random puzzle word from the vocabulary."""

import json
import random

# Words to exclude from puzzle selection
STOP_WORDS = {
    'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
    'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
    'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
    'could', 'should', 'may', 'might', 'must', 'shall', 'can', 'need',
    'it', 'its', 'this', 'that', 'these', 'those', 'they', 'them',
    'their', 'he', 'him', 'his', 'she', 'her', 'hers', 'we', 'us', 'our',
    'you', 'your', 'i', 'me', 'my', 'who', 'whom', 'which', 'what',
    'where', 'when', 'why', 'how', 'all', 'each', 'every', 'both',
    'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
    'only', 'own', 'same', 'so', 'than', 'too', 'very', 'just', 'also',
    'now', 'here', 'there', 'then', 'once', 'any', 'if', 'into', 'about',
    'after', 'before', 'above', 'below', 'between', 'under', 'again',
    'further', 'while', 'during', 'through', 'against', 'up', 'down',
    'out', 'off', 'over', 'because', 'until', 'unless', 'although',
    'being', 'get', 'got', 'getting', 'make', 'made', 'take', 'taken',
    'come', 'came', 'go', 'went', 'gone', 'see', 'saw', 'seen', 'know',
    'knew', 'known', 'think', 'thought', 'want', 'use', 'used', 'using',
    'find', 'found', 'give', 'gave', 'given', 'tell', 'told', 'say', 'said',
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
    'first', 'second', 'third', 'last', 'new', 'old', 'good', 'bad', 'great',
    'little', 'big', 'small', 'large', 'long', 'short', 'high', 'low',
    'many', 'much', 'well', 'back', 'even', 'still', 'way', 'thing', 'things',
    'part', 'place', 'case', 'week', 'company', 'system', 'program', 'question',
    'work', 'government', 'number', 'night', 'point', 'home', 'water', 'room',
    'mother', 'area', 'money', 'story', 'fact', 'month', 'lot', 'right', 'study',
    'book', 'eye', 'job', 'word', 'business', 'issue', 'side', 'kind', 'head',
    'house', 'service', 'friend', 'father', 'power', 'hour', 'game', 'line',
    'end', 'member', 'law', 'car', 'city', 'community', 'name', 'president',
    'team', 'minute', 'idea', 'kid', 'body', 'information', 'nothing', 'ago',
    'lead', 'social', 'whether', 'able', 'hand', 'enough', 'far', 'ask', 'late',
    'run', 'keep', 'let', 'begin', 'seem', 'help', 'show', 'hear', 'play',
    'move', 'live', 'believe', 'bring', 'happen', 'write', 'provide', 'sit',
    'stand', 'lose', 'pay', 'meet', 'include', 'continue', 'set', 'learn',
    'change', 'put', 'hold', 'turn', 'start', 'might', 'close', 'something',
    'stop', 'already', 'either', 'yet', 'within', 'likely', 'often', 'ever'
}

MIN_WORD_LENGTH = 4


def is_good_puzzle_word(word):
    """Check if a word would make a good puzzle."""
    if len(word) < MIN_WORD_LENGTH:
        return False
    if word in STOP_WORDS:
        return False
    if not word.isalpha():
        return False
    return True


def main():

    filepath='vectors.json'
    with open(filepath, 'r') as f:
        vectors = json.load(f)
    vocab = list(vectors.keys())

    good_words = [w for w in vocab if is_good_puzzle_word(w)]

    print(f"Vocabulary: {len(vocab)} words")
    print(f"Good puzzle words: {len(good_words)} words")
    print()
    print("Here are 10 random puzzle word suggestions:")
    print("-" * 40)

    picks = random.sample(good_words, min(10, len(good_words)))
    for i, word in enumerate(picks, 1):
        print(f"  {i:2}. {word}")

    print("-" * 40)
    print("Pick one and update TARGET_WORD in index.html!")


if __name__ == '__main__':
    main()
