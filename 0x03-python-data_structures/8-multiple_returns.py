#!/usr/bin/python3
"""More returns!"""
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
