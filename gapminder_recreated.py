# Relations between gdp, child mortality, and population
# libraries
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
my_dpi=96


pd.set_option('max_columns', 10)  # number of countries in the csv

# list for the colors
bubble_colors = ["#9b59b6", "#3498db", "#95a5a6", 
                     "#e74c3c", "#34495e", "#2ec541", 
                     "#2ecc71","#9eccf1", "#21cf11", "#2eff71"]

# read csv files ---> to pandas dataframe
dfx = pd.read_csv('csv/gdppc10.csv', sep=';')   # GDP per capita
dfy = pd.read_csv('csv/chmort10.csv', sep=';', decimal=',')   # CHILD MORTALITY
dfz = pd.read_csv('csv/pop10.csv', sep=';')     # POPULATION


# for iterating years - it creates a list from the column headers
years = list(dfx.columns.values)


for j in range(1,50):
    # convert strings to floats
    ylst = [float(k) for k in dfy[years[j]]]
    
    # create figure object
    fig = plt.figure(figsize=(680/my_dpi, 480/my_dpi), dpi=my_dpi, edgecolor='grey')
    
    # bubble plot
    plt.scatter(x=dfx[years[j]], 
                y=dfy[years[j]],
                s=dfz[years[j]]/10,
                alpha=0.5,
                c=bubble_colors)
    
    # axis labels, title and fixed limits
    plt.xlabel('GDP per Capita')
    plt.ylabel('Child mortality')
    plt.title(years[j])
    plt.xlim(2000,55000)
    plt.ylim(0,250)
        
    # country labels
    x = dfx[years[j]]
    y = dfy[years[j]]
    for i, txt in enumerate(dfx['geo.name']):
        plt.annotate(txt, (x[i], y[i]))

    # legend
    countries = dfx['geo.name']
    l = []
    for i in range(0,len(dfx.index)):
        l.append(mpatches.Patch(color=bubble_colors[i],
                               alpha=0.5,
                               label=countries[i]))
        plt.legend(handles=l, loc=(0.7,0.3))
        
    # saving png files
    filename='gapmndr'+str(j)+'.png'
    plt.savefig(filename, dpi=96, pad_inches=2)
    plt.gca()