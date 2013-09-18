import sys

def read_matrix(path):
	# matrix = [[1,2,3],[4,-100,6],[7,8,9]]
	matrix = [ map(int,line.split(' ')) for line in open (path,'r') if line.strip() != "" ]
	return matrix

def sum_matrix(left_upper, right_lower,matrix):
	i,j = left_upper
	k,l = right_lower
	return sum([sum(row[j:l+1]) for row in matrix[i:k+1]])

def get_the_max_for_elem(i,j,matrix):
	the_max = matrix[i][j]
	res_matrix = [[matrix[i][j] for l in range(len(matrix[0])-j)] for k in range(len(matrix)-i)]
	for k in range(len(res_matrix)):
		for l in range(len(res_matrix[0])):
			temp = sum_matrix((i,j),(k+i,l+j),matrix)
			if temp > the_max:
				the_max = temp
	return the_max

def main(path):
	matrix = read_matrix(path)
	the_max = matrix[0][0]
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			temp = get_the_max_for_elem(i,j,matrix)
			if temp > the_max:
					the_max = temp
	print the_max

if __name__ == '__main__':
	path = sys.argv[1]
	main(path)
