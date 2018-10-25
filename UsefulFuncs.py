import numpy as np

def RiemannSum(y,x):
    return 0.5*(y[1:]+y[:-1])*(x[1:]-x[:-1])

def Chi2(x,mu):
    return np.sum((x-mu)**2/mu)

def BinIt(data,bins,weight):

    binvalue = np.zeros(len(bins)-1,dtype=float)
    binerror = np.zeros(len(bins)-1,dtype=float)

    
    entry = np.digitize(data,bins)
    j = 0
    
    for i, item in enumerate(entry):
        if item == 0 or item == len(bins):
            j+=1
            continue
        binvalue[item-1] += weight[i]
        binerror[item-1] += weight[i]*weight[i]
    
    if j != 0:
        print str(j) + " data points outside of bins"

    return binvalue, np.sqrt(binerror)

    
def steppedBins(binvalue,bins):
    """Convert left/right edges and bin center values to a stepped path"""
    left_edges, right_edges = bins[:-1:], bins[1::]
    edges = np.concatenate((left_edges, [right_edges[-1]]))
    x = np.zeros((2*len(edges)))
    y = np.zeros((2*len(edges)))

    x[0::2], x[1::2] = edges, edges
    y[1:-1:2], y[2::2] = binvalue, binvalue
    
    return x, y