# coding: utf8

import csv
import subprocess


class Diagram(object):


	DIA_CMD_SVG = ["blockdiag", 
					"-Tsvg", 
					"input.diag"]

	DIA_CMD_PDF = ["blockdiag", 
					"-Tpdf", 
					"input.diag"]

	DIA_SETUP = ["blockdiag {\n",
				"node_width = 200;\n",
				"node_height = 40;\n",
				"span_width = 60;\n",
				"span_height = 30;\n",
				"default_fontsize = 11;\n",
				"default_shape = roundedbox;\n",
				"default_linecolor = '#222222';\n",
				"orientation = landscape;\n",
#				"edge_layout = flowchart;\n",
#				"default_textcolor = #RRGGBB\n"
#				"default_group_color = '#BBBBBB'\n"
				]
	DIA_COLORS = ["lightblue", 
					"lightcoral",
					"lightgreen",
					"#C68E17", 
					"#AAAAAA"]

	nodes = []
	first_node = None

	def __init__(self):
		self.first_node = Node(SETUP["first_node_name"], 0,0)
		self.fill()
		self.make_diagram()
		self.make_base()
		self.make_color()
		self.export_list()
		self.export_graph()
		self.export_sub_graph()

	def fill(self, filename = "input.csv"):
		with open(filename, 'r') as csvfile:
			listing = csv.reader(csvfile, delimiter=',', quotechar='|')
			for row in listing:
				try:
					info = row[4]+ "\t" + row[5]+ "\t" + row[6] + "\t" + row[7]+ "\t" + row[8] + "\t" + row[9]
					node = Node(row[3],row[0],row[1], info)
					print(node)
					self.nodes.append(node)
				except:
					pass

	def make_diagram(self):
		for node in self.nodes:
			if node.previous_id == 0:
				self.first_node.next_nodes.append(node)
			else:
				for previous_node in self.nodes:
					if node.previous_id == previous_node.node_id:
						previous_node.next_nodes.append(node)

	def make_base(self):
		self.first_node.recursive_base([0], 0)

	def make_color(self):
		i = 0
		for node in self.first_node.next_nodes:
			node.recursive_color(self.DIA_COLORS[i])
			i += 1


	def export_list(self, filename1 = "hlist.txt", filename2 = "list.txt"):
		with open(filename1, 'w') as f:
			self.first_node.recursive_hlist(f)
		with open(filename2, 'w') as f:
			self.first_node.recursive_list(f)
  
	def export_graph(self, filename = "input"):
		with open(filename + ".diag", 'w') as f:
			for i in self.DIA_SETUP:
				f.write(i)
			self.first_node.recursive_format(f)
			f.write("\n")
			self.first_node.recursive_graph(f)
			f.write("}")
		#subprocess.call(self.DIA_CMD_PDF)
		subprocess.call(self.DIA_CMD_SVG)
		subprocess.call(["convert", "input.svg", "diagramme.png"])
		subprocess.call(["rm", filename + ".svg"])
		subprocess.call(["rm", filename + ".diag"])

	def export_sub_graph(self):
		list_subgraphe = []
		for second_node in self.first_node.next_nodes:
			with open(second_node.name, "w") as f:
				list_subgraphe.append(second_node.name)
				for i in self.DIA_SETUP:
					f.write(i)
				second_node.recursive_format(f)
				f.write("\n")
				second_node.recursive_graph(f)
				f.write("}")
		for filename in list_subgraphe:
			#subprocess.call(["blockdiag", "-Tpdf", filename])
			subprocess.call(["blockdiag", "-Tsvg", filename])
			subprocess.call(["convert", filename + ".svg", filename + ".png"])
			subprocess.call(["rm", filename + ".svg"])
			subprocess.call(["rm", filename])




class Node(object):


	def __init__(self, name, node_id, previous_id, info = ""):
		self.name = name
		self.node_id = int(node_id)
		self.previous_id = int(previous_id)
		self.next_nodes = []
		self.level = ""
		self.indice = 0
		self.dia_color = "#EEEEEE"
		self.appr = info

	def __str__(self):
		return self.name

	def recursive_base(self, base, i):
		if i != 0:
			indice = ""
			for x in range(0,i):
				indice += str(base[x])+"."
			self.level = indice[:-1]
			self.indice = i
		i += 1
		if len(base) <= i:
			base.append(0)
		for node in self.next_nodes:
			node.recursive_base(base, i)
		i -= 1
		base[i] = 0
		base[i-1] += 1

	def recursive_list(self, f):
		f.write(self.level + " - "+self.name + "\t" + self.appr + "\n" )
		for node in self.next_nodes:
			node.recursive_list(f)


	def recursive_hlist(self, f):
		for i in range(0, self.indice):
			f.write("     ")
		if self.indice != 0:
			f.write(self.level + " - ")
		if self.appr != ['*','*','*']:
			f.write(self.name + "\t"+ self.appr + "\n")
		else:
			f.write(self.name + '\n')
		for node in self.next_nodes:
			node.recursive_hlist(f)

	def recursive_format(self, f):
		f.write(str(self.node_id)+' [label = "'+self.name+'", color = "'+self.dia_color+'"];\n')
		for node in self.next_nodes:
			node.recursive_format(f)

	def recursive_graph(self, f):
		if self.next_nodes == []:
			f.write(str(self.node_id))
		for node in self.next_nodes:
			f.write(str(self.node_id))
			f.write(" -> ")
			node.recursive_graph(f)
		f.write("\n\t")

	def recursive_color(self, color = SETUP["first_node_color"]):
		self.dia_color = color
		for node in self.next_nodes:
			node.recursive_color(color)

Diagram()