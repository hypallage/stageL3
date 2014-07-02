from Combinations import *

def createAllTracks(size):

	allTracks = []

	for train in xcombinations(list(xrange(1,size*2+1)), size*2):
		#print "TTT", train
		tracks = []
		for i in xrange(0,size*2,2):
			aTrack = train[i:i+2]
			tracks.append(aTrack)

		allTracks.append(tracks)
	#print allTracks
	"""
	aTrack = []
	aTrack.append((2,1))
	aTrack.append((4,3))
	allTracks.append(aTrack)
	#print allTracks
	"""
	return allTracks

def evalSol(sol,n):
	ident = list(xrange(1,n+1))
	val = 0

	#for s in sol and i in ident:
	for (s,i) in zip(sol,ident):
		val += abs(s-i)
	return val

def solveGreedyLateFirst(tracks, n):
	sol = []
	for i in xrange(1,n+1):
		#print tracks
		minVal = n*2
		minTrack = tracks[0]
		bestFound = False
		for track in tracks:
			if track[0] < i and not bestFound:
				if len(track) == 1:
					bestFound = True
				minTrack = track

			if abs(track[0] - i) < minVal and not bestFound:
				minVal = abs(track[0] - i)
				minTrack = track
			elif abs(track[0] - i) == minVal and track[0] < minTrack[0] and not bestFound:
				minVal = abs(track[0] - i)
				minTrack = track


		sol.append(minTrack[0])
		if len(minTrack) is 2:
			tracks.append([minTrack[1]])
		tracks.remove(minTrack)
		#print "tracks", tracks
	#print "Greedy Sol", sol
	return sol

def solveGreedy(tracks, n):
	#return list(xrange(4,0,-1))
	sol = []
	#print "tracks", tracks

	for i in xrange(1,n+1):
		minVal = n*2
		minTrack = tracks[0]
		for track in tracks:
			if abs(track[0] - i) < minVal:
				minVal = abs(track[0] - i)
				minTrack = track
			elif abs(track[0] - i) == minVal and track[0] < minTrack[0]:
				minVal = abs(track[0] - i)
				minTrack = track


		sol.append(minTrack[0])
		if len(minTrack) is 2:
			tracks.append([minTrack[1]])
		tracks.remove(minTrack)
		#print "tracks", tracks
	#print "Greedy Sol", sol
	return sol

def solveAccordingToOrder(tracks, trackOrder):
	sol = []
	seen = set()

	for order in trackOrder:
		order = order-1	#tracks begining to 1, list index to 0
		if order not in seen:
			seen.add(order)
			#print tracks, order
			sol.append(tracks[order][0])
		else:
			sol.append(tracks[order][1])
	return sol

def solveExaust(tracks):
	trackOrder = list(xrange(1,len(tracks)+1))
	trackOrder += trackOrder

	minSol = len(tracks)*4
	minOrder = None
	minTrain = None

	for order in xcombinations(trackOrder, len(tracks)*2):
		#print ''.join(a)
		#print "A", a

		#print "ord", order

		if order is not None:
			sol = solveAccordingToOrder(tracks, order)
			solVal = evalSol(sol,len(tracks)*2)
			#print "V", solVal
			if solVal < minSol:
				minSol = solVal
				minOrder = order
				minTrain = sol
	#print "best Exaust:", minSol, minOrder
	return (minSol, minTrain)

def main():
	#print solveExaust([[1,4],[2,5],[6,3]])


	nbTracks = 3
	allTracks = createAllTracks(nbTracks)

	for tracks in allTracks:
		savTrack = list(tracks)
		exau = solveExaust(tracks)
		#print tracks
		#solGreedy = solveGreedy(tracks,4)
		solGreedy = solveGreedyLateFirst(tracks,nbTracks*2)
		#print "eval Greedy:", evalSol(solGreedy,4)
		evalGreedy = evalSol(solGreedy,nbTracks*2)
		if(evalGreedy > exau[0]):
			print (evalGreedy, solGreedy), ">", exau, "for ", savTrack

def available (el,tracks):
 if tracks == []:
	return False
 else:
	a=tracks.pop()
	b=a.pop()
	if el==b:
		if a != []:
			tracks.append(a)
			return True
		else:
			return True
	else:
		a.append(b)
		c=available (el,tracks)
		tracks.append(a)
		return c

def diff (atrack):
 if atrack == []:
	return False
 else:
	b=atrack.pop()
	c=atrack.pop()
	if b<c:
		atrack.append(c)
		atrack.append(b)
		return 0
	else:
		atrack.append(c)
		atrack.append(b)
		return (b-c)

s=[2,5]

li=[[1,3],[4,2]]

print available (3,li)
print diff(s)

main()
