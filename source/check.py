import argparse


def checkArg1 (c):
    cities=["Madrid","Barcelona"]
    if c in cities:
        return c
    else:
        raise argparse.ArgumentTypeError("Country requested is not available")



def checkArg2 (m):
    measurements=["no2","pm25"]
    if m in measurements:
        return m
    else:
        raise argparse.ArgumentTypeError("Measurement requester is not available")