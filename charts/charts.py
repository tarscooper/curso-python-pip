import matplotlib.pyplot as plt

def generate_pie_chart():
    labels =['A','B','C']
    values =[300,500,700]

    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('pie.png')
    plt.show()
    plt.close()
