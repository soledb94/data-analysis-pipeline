import matplotlib.pyplot as plt

def graphs(measurement,info_mean,result):
        x=[f'{measurement} Mean-February',f'{measurement} Currently']
        y=[info_mean,result]
        plt.bar(x,y)
        plt.yticks(y)

        return plt.savefig("graph.jpg")