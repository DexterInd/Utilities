import svgwrite
import json,ast
from pprint import pprint
from PIL import Image

def getImageSize(image_filename):
	im = Image.open(image_filename)
	width, height = im.size
	return width,height


def setColumnWidth(nbcolumns):
	'''
	Set column width for a 1024 width image
	'''
	global columnWidth
	columnWidth = imagesize[x] / nbcolumns
	columnWidth = 250
	print "Setting columnWidth to ",columnWidth

imagesize=(1900,1900)
columnWidth=0
titlesize=(225,60)
blocksize=(200,100)
legendsize=(200,40)
x = 0
y = 1
print titlesize[0]

with open("gopigo/scratch_commands.json") as data_file:
	data = data_file.read()
	parsed_commands = json.loads(data)

	# use ast to remove all unicode encoding
	parsed_commands = ast.literal_eval(json.dumps(parsed_commands))

svg_document = svgwrite.Drawing(filename = "gopigo.svg",
								size = ("{}px".format(imagesize[x]), "{}px".format(imagesize[y])),
								debug=True)

# Get top sections


posV=30
print("{} Top Items".format(len(parsed_commands)))
for top,content in parsed_commands.iteritems():
	posH=50
	print("***")
	pprint(top)
	print("***")
	print(parsed_commands[top]["TopSection"])
	svg_document.add(svg_document.text(parsed_commands[top]["TopSection"], insert = (posH, posV)))
	#pprint(parsed_commands[top]["Sections"])

	nbcolumns = len(parsed_commands[top]["Columns"])
	print("Number of Columns: {}".format(nbcolumns))
	if nbcolumns > 0:
		setColumnWidth(nbcolumns)
		maxcolumnheight=0

		for column in parsed_commands[top]["Columns"]:
			columnheight=0
			print("---")
			posV=60	
	
			#pprint(column)
			# go into each set of sections
			for block in column['column']:
				#pprint(block)
				pprint (block["SectionTitle"])
				svg_document.add(svg_document.text(block["SectionTitle"],insert=(posH,posV)))
				posV+=10
				columnheight+=titlesize[y]
				for b in block["Block"]:
					pprint(b["image"])
					print("at {}/{}".format(posH,posV))
					image_filename="gopigo/{}".format(b["image"])
					imagewidth,imageheight=getImageSize(image_filename)
					img=svg_document.image(image_filename,insert=(posH,posV),size=(imagewidth,imageheight))
					img.fit("left","top","meet")
					svg_document.add(img)
					posV+=(imageheight+10)
					columnheight+=blocksize[y]
					try:
						pprint(b["legend"])
						columnheight+=legendsize[y]
					except:
						pass
				if columnheight > maxcolumnheight:
					maxcolumnheight = columnheight
				posV+=30
			print maxcolumnheight
			posH+=columnWidth
		svg_document.add(svg_document.rect(insert=(10,29),size=(posH,posV),fill="white",opacity=0.10,stroke="black",rx=30,stroke_width="1"))
	posV+=100








		#svg_document.add(svg_document.text("Hello World",
		#							   insert = (210, 110)))
#svg_document.add(svg_document.rect(insert = (290,310),
#									size=(197,37)))



print(svg_document.tostring())

svg_document.save()
