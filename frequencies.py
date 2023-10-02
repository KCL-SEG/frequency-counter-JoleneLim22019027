"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from collections import Counter

def frequencies(items):
    frequencies = {}
    for a in items:
        if a not in frequencies:
            frequencies[a] = items.count(a)
    return frequencies
