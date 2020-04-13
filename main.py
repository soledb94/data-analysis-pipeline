import argparse
import pandas as pd
import source.pdf_creation as pdf
from source.check import *
from source.dataset import *
from source.request import *
from source.graph import *
from source.pdf_creation import *


def parse():
    parser=argparse.ArgumentParser(description="Pass a country and a measurement")
    parser.add_argument("-c",dest="city",help="Pass a city to get the info",type=checkArg1)
    parser.add_argument("-m",dest="measurement",help="Pass a measurement to get the info",type=checkArg2)
    args=parser.parse_args()
    return args


def main():
    args=parse()
    city=args.city
    measurement=args.measurement
    print(args)
    data=dataSet()
    filtered=filters(data,city,measurement)
    info=information(filtered)
    info_mean=mean_information(filtered)
    request=getFromOpenaq(city,measurement)
    result=getResult(request,city,measurement)
    graphs(measurement,info_mean,result)
    createPDF(info,city)



if __name__=="__main__":
    main()








