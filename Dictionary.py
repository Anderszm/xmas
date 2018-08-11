from pprint import pprint

# dictionary:

# key: value --> User: Their eligible matches


#This will be what's fed into the function you create
#don't worry about creating the dict, I'll handle that on the server side
#just use this as the input
inputdict = {
	"Brian": ["Zach", "Caitlin", "Katy", "Tami", "Jim"],
	"Zach": ["Brian", "Caitlin", "Katy", "Tami", "Jim"],
	"Caitlin": ["Brian", "Caitlin", "Katy", "Tami", "Jim"],
	"Katy": ["Brian", "Zach", "Caitlin", "Tami", "Jim"],
	"Tami": ["Brian", "Zach", "Caitlin", "Katy", "Jim"],
	"Jim": ["Brian", "Zach", "Caitlin", "Katy", "Tami"]
}

#This will be what the output should look like
outputdict = {
	"Brian": "Tami",
	"Zach": "Caitlin",
	"Caitlin": "Jim",
	"Katy": "Brian",
	"Tami": "Zach",
	"Jim": "Katy"
}
	

def drawNames(groupdict):
	
	#how one loops through a dictionary
	for key, value in groupdict.items():
		print(f"Person: {key}")
		print("   List of matches:")
		for val in value:
			print(f"   {val}")
	
	#do some magic to get to output
	
	return outputdict
	


finaldict = drawNames(inputdict)			
print()
print("Return Dictionary for me:")
pprint(finaldict)

