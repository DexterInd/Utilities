import svgwrite
import json,ast
from pprint import pprint
from PIL import Image
import sys

def getImageSize(image_filename):

	#Image.open is a lazy file open. It only loads image header
	im = Image.open(image_filename)
	width, height = im.size
	print("{} is {}".format(image_filename,im.size))
	return width,height


def setColumnWidth(nbcolumns):
	'''
	Set column width for a 1024 width image
	'''
	global columnWidth
	columnWidth = imagesize[x] / nbcolumns
	columnWidth = 250
	print ("Setting columnWidth to {}".format(columnWidth))

imagesize=(1900,1900)
columnWidth=0
titlesize=(225,60)
legendsize=(200,40)
breathingspace=30
x = 0
y = 1

robot=str(sys.argv[1]).lower()
if not robot in ["gopigo3","gopigo","brickpi","grovepi","pivotpi" ]:
	print("Robot not recognised: {}".format(sys.argv[1]))
	exit()



with open("{}/scratch_commands.json".format(robot)) as data_file:
	data = data_file.read()
	parsed_commands = json.loads(data)

	# use ast to remove all unicode encoding
	parsed_commands = ast.literal_eval(json.dumps(parsed_commands))

svg_document = svgwrite.Drawing(filename = "{}.svg".format(robot),
								size = ("{}px".format(imagesize[x]), "{}px".format(imagesize[y])),
								debug=True)

# Get top sections



vOffset=breathingspace
print("{} Top Items".format(len(parsed_commands)))
# create a top level section
for (top,content) in parsed_commands.items(): 
	posH=50
	posV=0
	maxcolumnheight=0
	print(parsed_commands[top]["TopSection"])
	boxV=vOffset
	svg_document.add(svg_document.text(parsed_commands[top]["TopSection"], insert = (posH, boxV)))
	
	#pprint(parsed_commands[top]["Sections"])

	nbcolumns = len(parsed_commands[top]["Columns"])
	#print("Number of Columns: {}".format(nbcolumns))
	if nbcolumns > 0:
		setColumnWidth(nbcolumns)
		maxcolumnheight=0

		# Create a column
		for column in parsed_commands[top]["Columns"]:
			print("---")
			posV=breathingspace+vOffset

			# go into each set of blocks
			for block in column['column']:
				title = svg_document.text(block["BlockTitle"],insert=(posH,posV),style = "font-size:18px;")
				svg_document.add(title)
				posV+=10
				for b in block["Block"]:
					image_filename="{}/{}".format(robot,b["image"])
					imagewidth,imageheight=getImageSize(image_filename)
					img=svg_document.image(image_filename,insert=(posH,posV),size=(imagewidth,imageheight))
					img.fit("left","top","meet")
					svg_document.add(img)
					posV+=(imageheight+10)
					# try:
					# 	#pprint(b["legend"])
					# 	legend=svg_document.text(b["legend"],insert=(posH,posV),style = "font-size:8px;")
					# 	posV+=(legendsize[y])
					# except:
					# 	pass
				columnheight = posV-vOffset
				if (columnheight) > maxcolumnheight:
					maxcolumnheight = columnheight
				posV+=30
			posH+=columnWidth
		print("Box at {} size {}".format((10,boxV),(posH,maxcolumnheight)))
		svg_document.add(svg_document.rect(insert=(10,boxV),size=(posH,(maxcolumnheight)),fill="white",opacity=0.10,stroke="black",rx=30,stroke_width="1"))
	vOffset+=(maxcolumnheight+30)









		#svg_document.add(svg_document.text("Hello World",
		#							   insert = (210, 110)))
#svg_document.add(svg_document.rect(insert = (290,310),
#									size=(197,37)))



#print(svg_document.tostring())

svg_document.save()
