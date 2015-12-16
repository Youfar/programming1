# Smith-Waterman algorithm 
# optimal local alignment of two sequences 
from optparse import OptionParser
import os

usage = "usage: %prog [options] keyword"
parser = OptionParser(usage)

parser.add_option("-a", dest = "matchScore", type="int", default=1)
parser.add_option("-b", dest = "mismatchScore", type="int", default=-1)
(options, args) = parser.parse_args()

matchAward = options.matchScore
mismatchPenalty = options.mismatchScore
#MATCH_AWARD = 1
#MISMATCH_PENALTY = -1
GAP_PENALTY = -2

#decide match or gap
def match_score(a, b):
	if a == b:
		return matchAward
	elif a == '-' or b == '-':
		return GAP_PENALTY
	else:
		return mismatchPenalty
		
def smith_waterman(str1, str2):
	"""
	calculate the max score alignment
	"""
	#get length of strings
	n = len(str1)
	m = len(str2)

	#initialization
	max_score = 0
	sub = [[0 for i in range(m+1)] for i in range(n+1)]
	pointer = [[0 for i in range(m+1)] for i in range(n+1)]

	for i in range(n+1):
		sub[i][0] = 0
	for j in range(m+1):
		sub[0][j] = 0

	#calculate subproblem solutions
	for i in range (1,n+1):
		for j in range(1,m+1):

			case1 = sub[i-1][j-1] + match_score(str1[i-1], str2[j-1])
			case2 = sub[i][j-1] + GAP_PENALTY
			case3 = sub[i-1][j] + GAP_PENALTY

			sub[i][j] = max(0, case1, case2, case3)
		
			if sub[i][j] == 0:
				pointer[i][j] = 0
			if sub[i][j] == case3:
				pointer[i][j] = 1
			if sub[i][j] == case2:
				pointer[i][j] = 2
			if sub[i][j] == case1:
				pointer[i][j] = 3
			if sub[i][j] >= max_score:#dengyuhao
				max_score = sub[i][j]
				max_i = i
				max_j = j


	#traceback
	alignment1 = ""
	alignment2 = ""

	i = max_i
	j = max_j

	while pointer[i][j] != 0:
		if pointer[i][j] == 3:
			alignment1 += str1[i-1]
			alignment2 += str2[j-1]
			i -= 1
			j -= 1
		elif pointer[i][j] == 2:
			alignment1 += '-'
			alignment2 += str2[j-1]
			j -= 1
		elif pointer[i][j] == 1:
			alignment1 += str1[i-1]
			alignment2 += '-'
			i -= 1

	return max_score, alignment1, alignment2

def main():
	
	#usage = "usage: %prog [options] keyword"
	#parser = OptionParser(usage)

	#parser.add_option("-a", dest = "matchScore", type="int", default=1)
	#parser.add_option("-b", dest = "mismatchScore", type="int", default=-1)
	#(options, args) = parser.parse_args()

	#matchAward = options.matchScore
	#mismatchPenalty = options.mismatchScore
	str1 = "GCCCTAGCG"
	str2 = "GCGCAATG"

	match_score, alignment1, alignment2 = smith_waterman(str1, str2)
	print "Total penaltys:", match_score
	print "Optimal alignment", "".join(alignment1)
	print "Optimal alignment", "".join(alignment2)

if __name__ == "__main__":
	main()
