"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from collections import Counter

def frequencies(items):
    frequencies = {}
    theItems = [str(a) for a in items]
    frequencies = Counter(theItems)
    return frequencies
