#! /usr/bin/python
#_*_ coding utf-8 _*_

import data as data


def main(path=data.path_file):
	list_houses = []
	with open(path, 'r') as file:

		count = 0
		for house in file:
			if count != 0:
				values = house.split(",")
				list_houses.append(create_dict(values[0],values[1]))
			count += 1

	create_file(order_list(list_houses))


def create_dict(house, number):
	dict = {'house': house.rstrip(), 'ng': int(number)}
	return dict


def order_list(list_houses):
	n_elements = len(list_houses)
	for i in range(n_elements):
	
		for index in range(n_elements -i -1):
			if list_houses[index]['ng'] < list_houses[index+1]['ng']:
				aux = list_houses[index]
				list_houses[index] = list_houses[index+1]
				list_houses[index+1] = aux

	return list_houses
 

def create_file(list_houses):
	file_houses = open(data.path_file_ordered,"w+")

	for dc in list_houses:
		file_houses.write("%s,%d\r\n"%(dc['house'],dc['ng']))

	file_houses.close()	

if __name__ == "__main__":	
	main()
