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

def minimum(el,tracks):
 if tracks == []:
	return [0,0]
 else:
	a=tracks.pop(0)
	b=a.pop(0)
	try: 
		c=a.pop(0)
		if c>b:			
			trackmin=minimum(el,tracks)
			a.insert(0,c)
			a.insert(0,b)
			tracks.insert(0,a)
			return trackmin
		else:
			if el>=c:
				trackmin=minimum(el,tracks)
				val=trackmin.pop(0)
				trackmin.insert(0,val)
				if val==0:
					a.insert(0,c)
					a.insert(0,b)
					return a
				else:
					if val<b:
						a.insert(0,c)
						a.insert(0,b)
						tracks.insert(0,a)
						return trackmin
					else:
						a.insert(0,c)
						a.insert(0,b)
						tracks.insert(0,trackmin)
						return a
			else:
				trackmin=minimum(el,tracks)
				a.insert(0,c)
				a.insert(0,b)
				tracks.insert(0,a)
				return trackmin
	except IndexError:
		trackmin=minimum(el,tracks)
		a.insert(0,b)
		tracks.insert(0,a)
		return trackmin

def available (el,tracks):
 if tracks == []:
	return False
 else:
	a=tracks.pop(0)
	b=a.pop(0)
	if el==b:
		if a != []:
			tracks.insert(0,a)
			return True
		else:
			return True
	else:
		a.insert(0,b)
		c=available (el,tracks)
		tracks.insert(0,a)
		return c

def solve(tracks,n):
	sol=[]
	track=[]
	trackcroi=[]
	trackdecr=[]
	for a in tracks:
			b=a.pop(0)
			c=a.pop(0)
			a.insert(0,c)
			a.insert(0,b)
			if b<c:
				trackcroi.insert(0,a)
			else:
				trackdecr.insert(0,a)
	for (i) in xrange(1,n+1):
		if available(i,trackcroi):
		 	sol.append(i)
		else:
			if track==[]:
				track=minimum(i,trackdecr)
				a=track.pop(0)
				sol.append(a)
			else:
				a=track.pop(0)
				sol.append(a)
	return sol

def main1():
	nbTracks = 8
	allTracks = createAllTracks(nbTracks)

	for tracks in allTracks:
		#savTrack = list(tracks)
		copie=[]
		print tracks
		for a in tracks:
			copie.append(list(a))
		savTrack = []
		for a in tracks:
			savTrack.append(list(a))
		exau = solveExaust(tracks)
		#solGreedy = solveGreedy(tracks,4)
		solGreedy = solve(savTrack,nbTracks*2)
		#print "eval Greedy:", evalSol(solGreedy,4)
		evalGreedy = evalSol(solGreedy,nbTracks*2)
		if(evalGreedy > exau[0]):
			print (evalGreedy, solGreedy), ">", exau, "for ", copie

tracks=[[3, 4], [6, 1], [5, 2]]

main1()
