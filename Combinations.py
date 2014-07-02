def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc
                  
def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss
                  
                            
def subsets_set(x):
    """
    x : a frozenset (hashable)
    return: a list of all the subsets of x
    
    recursive method
    """
    if len(x) == 0:
        return [frozenset()]
    else:
        #s = [x] #list of lists, first element is x
        s = set()
        s.add(x)
        
        for elem in x:
            #tmp = x[:]  #copy
            tmp = set(x)
            tmp.remove(elem)
            tmp = frozenset(tmp)
            
            new_sub = subsets(tmp)
            for y in new_sub: # <-- can't just make it a set(), because lists aren't hashable.
                #if y not in s:
                #    s.append(y)
                s.add(y)
        return s    
    
#TODO: trouver plus efficace
def subsets_(x):
    """
    x : a set
    return: a list of all the subsets of x
    
    recursive method
    """
    if x == []:
        return [[]]
    else:
        s = [x] #list of lists, first element is x
        for elem in x:
            tmp = x[:]  #copy
            tmp.remove(elem)
            new_sub = subsets(tmp)
            for y in new_sub: # <-- can't just make it a set(), because lists aren't hashable.
                if y not in s:
                    s.append(y)
        return s
    

def listSoustraction(x, y):
    r = x[:]
    for i in y:
        r.remove(i)
    return r







def subsets(s = []):
  indices = []
  n = len(s)
  m = 0
 
  tmp = []
  while m < n:
    yield tmp
    if indices == []:
      indices = [0]
    else:
      if indices[-1] != n-1:
        indices[-1] += 1
      else:
        i = 0
        for i in range(len(indices)-2, -1, -1):
          if indices[i] + 1 < indices[i+1]:
            indices[i] += 1
            for j in range(i+1, len(indices)):
              indices[j] = indices[j-1]+1
            i = -1
            break
        if i == 0:
          if len(indices) == n:
            break
          indices = range(len(indices) + 1)
    tmp = []
    for i in indices:
      tmp.append(s[i])
 
def teste(el,liste):
 if liste==[]:
	return True
 else:
	t=liste.pop()
	liste.append(t)
	if el<t:
		return True
	else:
		return False


def place1el (el,listestack):
 if listestack == []:
	return [[el]]
 else:
	a=listestack.pop()
	if teste (el,a):
		a.append(el)
		listestack.append(a)
		return listestack
	else:
		b=place1el (el,listestack)
		b.append(a)
		return b

def decompose (permutation,listestack):
 if (permutation == []):
	return listestack
 else:
	a=permutation.pop()
	b=place1el (a,listestack)
	return decompose (permutation,b)

"""

for a in xcombinations([1,2,3,4,5,6,7,8,9], 9):
   b=list(a)
   e=decompose(b,[[]])
   d=len(e)
   if d<4:
	print a
	print e
"""


"""
s = range(1,5)

generator = subsets(s)
for i in generator:
  print i
  print listSoustraction(s,i)




s = [1,1,2,3]
print s
subS = subsets_list(s)
print subS

for sPrime in subS:
    print "s' : ", sPrime
    
#    sMinusSPrime = s - sPrime
    sMinusSPrime = listSoustraction(s, sPrime)

    print "s-s' : ", sMinusSPrime 
    print ""
"""

"""
for a in xcombinations(['1','2','3','4','5','6','7','8','9','10','11','12'], 2):
   print '-'.join(a)
"""

"""
for a in xcombinations(['1','2','3','1'], 4):
   print ''.join(a)
"""

"""
for a in xselections(['1','2','3'], 6):
   print ''.join(a)
"""

"""
for a in xuniqueCombinations(['1','2','3'], 2):
   print ''.join(a)
"""
