#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NYU NLP Homework 5: Feature selection for Maxent Noun Group tagger.
    by Ziyang Zeng (zz2960)
    Spring 2022
"""

import argparse
from typing import TypedDict, Union, List
import nltk
from fastprogress.fastprogress import progress_bar

stemmer = nltk.stem.SnowballStemmer('english')


class Word(TypedDict):
    word: str
    pos: str
    capitalized: bool
    tag: Union[str, None]


def parse_input(input_file: str) -> List[Union[List[Word], None]]:
    """
    Parses the input file and returns a list of lists of words.
    """
    with open(input_file, "r") as f:
        lines = f.readlines()
    sentences: List[Union[List[Word], None]] = []
    last_sentence: List[Word] = []
    print("Parsing input file lines...")
    for line in progress_bar(lines):
        line = line.strip()
        word_info = line.split("\t")
        if len(word_info) >= 2:
            word_str = word_info[0].strip()
            capitalized = word_str[0].isupper()
            pos = word_info[1].strip()
            if len(word_info) >= 3:
                tag = word_info[2].strip()
            else:
                tag = None
            word = Word(word=word_str, pos=pos,
                        capitalized=capitalized, tag=tag)
            last_sentence.append(word)
        else:
            if len(last_sentence) > 0:
                sentences.append(last_sentence)
            last_sentence = []
            sentences.append(None)
    if len(last_sentence) > 0:
        sentences.append(last_sentence)
    return sentences


class WordFeatures(TypedDict):
    word: str
    stem: str
    pos: str
    position: float
    previous_tag: Union[str, None]
    previous_pos: Union[str, None]
    previous_word: Union[str, None]
    previous_stem: Union[str, None]
    previous_2_pos: Union[str, None]
    previous_2_word: Union[str, None]
    previous_2_stem: Union[str, None]
    next_pos: Union[str, None]
    next_word: Union[str, None]
    next_stem: Union[str, None]
    next_2_pos: Union[str, None]
    next_2_word: Union[str, None]
    next_2_stem: Union[str, None]
    capitalized: bool
    tag: Union[str, None]


def get_word_features(sentence: List[Word]) -> List[WordFeatures]:
    """
    Returns a list of word features for a sentence.
    """
    word_features = []
    sentence_len = len(sentence)
    for i in range(sentence_len):
        word = sentence[i]
        position = i / sentence_len
        word_str = word["word"]
        word_stem = stemmer.stem(word_str)
        word_pos = word["pos"]
        word_capitalized = word["capitalized"]
        word_tag = word["tag"]
        if i >= 1:
            previous_tag = "@@"
            previous_word = sentence[i-1]
            previous_word_str = previous_word["word"]
            previous_word_pos = previous_word["pos"]
            previous_word_stem = stemmer.stem(previous_word_str)
        else:
            previous_tag = None
            previous_word_str = None
            previous_word_pos = None
            previous_word_stem = None
        if i >= 2:
            previous_2_word = sentence[i-2]
            previous_2_word_str = previous_2_word["word"]
            previous_2_word_pos = previous_2_word["pos"]
            previous_2_word_stem = stemmer.stem(previous_2_word_str)
        else:
            previous_2_word_str = None
            previous_2_word_pos = None
            previous_2_word_stem = None
        if i <= sentence_len - 2:
            next_word = sentence[i+1]
            next_word_str = next_word["word"]
            next_word_pos = next_word["pos"]
            next_word_stem = stemmer.stem(next_word_str)
        else:
            next_word_str = None
            next_word_pos = None
            next_word_stem = None
        if i <= sentence_len - 3:
            next_2_word = sentence[i+2]
            next_2_word_str = next_2_word["word"]
            next_2_word_pos = next_2_word["pos"]
            next_2_word_stem = stemmer.stem(next_2_word_str)
        else:
            next_2_word_str = None
            next_2_word_pos = None
            next_2_word_stem = None
        features = WordFeatures(word=word_str, stem=word_stem, pos=word_pos,
                                position=position,
                                previous_tag=previous_tag,
                                previous_pos=previous_word_pos,
                                previous_word=previous_word_str,
                                previous_stem=previous_word_stem,
                                previous_2_pos=previous_2_word_pos,
                                previous_2_word=previous_2_word_str,
                                previous_2_stem=previous_2_word_stem,
                                next_pos=next_word_pos,
                                next_word=next_word_str,
                                next_stem=next_word_stem,
                                next_2_pos=next_2_word_pos,
                                next_2_word=next_2_word_str,
                                next_2_stem=next_2_word_stem,
                                capitalized=word_capitalized,
                                tag=word_tag)
        word_features.append(features)
    return word_features


def main():
    parser = argparse.ArgumentParser(
        description="A feature selector for Maxent Noun Group tagger.")
    parser.add_argument("inputfile", help="input corpus file")
    parser.add_argument("outfile", help="feature selection output file")

    args = parser.parse_args()

    sentences = parse_input(args.inputfile)

    print("\nSelecting features...")
    with open(args.outfile, "w") as f:
        for sentence in progress_bar(sentences):
            if sentence is None:
                f.write("\n")
            else:
                word_features = get_word_features(sentence)
                for word_feature in word_features:
                    word_feature_str_list = []
                    for key, value in word_feature.items():
                        if value is None or key == "word" or key == "tag":
                            continue
                        word_feature_str_list.append(f"{key.upper()}={value}")
                    word_feature_str_list.insert(0, word_feature["word"])
                    if word_feature["tag"] is not None:
                        word_feature_str_list.append(word_feature['tag'])
                    f.write("\t".join(word_feature_str_list))
                    f.write("\n")
        print(f"{args.inputfile} -> {args.outfile}.")


if __name__ == '__main__':
    main()
