import argparse
import source.functions as f
#from source.generapdf import crearPdf

def checkArg1 (c):
    cities=["Madrid","Barcelona"]
    if c in cities:
        return c
    else:
        err: "Country requested is not available"
        raise argparse.ArgumentTypeError(err)


def checkArg2 (m):
    measurements=["no2","pm25"]
    if m in measurements:
        return m
    else:
        err="Measurement requester is not available"
        raise argparse.ArgumentTypeError(err)


def parse():
    parser=argparse.ArgumentParser(description="Pass a country and a measurement")
    parser.add_argument("--city",help="Pass a city to get the info")
    parser.add_argument("--measurement",dest="measurement",help="Pass a measurement to get the info ")
    args=parser.parse_args()
    return args

def main():
    args=parse()
    city=args.city
    measurement=args.measurement
    f.saluda()
    return args

main()








