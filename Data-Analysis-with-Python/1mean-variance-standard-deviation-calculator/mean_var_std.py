import numpy as np

def calculate(list):
  #error condition
  if len(list) < 9:
    raise ValueError('List must contain nine numbers.')
    
  #build array from list
  list = list[0:9]
  arr = np.array(list)
  arr = np.reshape(arr, (3,3))

  ###build statistical elements
  calculations = {}
  
  #mean
  axis1 = arr.mean(axis=0).tolist()
  axis2 = arr.mean(axis=1).tolist()
  flattened = arr.mean()
  calculations['mean'] = [axis1, axis2, flattened]
  
  #variance
  axis1 = arr.var(axis=0).tolist()
  axis2 = arr.var(axis=1).tolist()
  flattened = arr.var()
  calculations['variance'] = [axis1, axis2, flattened]

  #standard deviation
  axis1 = arr.std(axis=0).tolist()
  axis2 = arr.std(axis=1).tolist()
  flattened = arr.std()
  calculations['standard deviation'] = [axis1, axis2, flattened]
  
  #max
  axis1 = arr.max(axis=0).tolist()
  axis2 = arr.max(axis=1).tolist()
  flattened = arr.max()
  calculations['max'] = [axis1, axis2, flattened]
  
  #min
  axis1 = arr.min(axis=0).tolist()
  axis2 = arr.min(axis=1).tolist()
  flattened = arr.min()
  calculations['min'] = [axis1, axis2, flattened]

  #sum
  axis1 = arr.sum(axis=0).tolist()
  axis2 = arr.sum(axis=1).tolist()
  flattened = arr.sum()
  calculations['sum'] = [axis1, axis2, flattened]
  
  return calculations