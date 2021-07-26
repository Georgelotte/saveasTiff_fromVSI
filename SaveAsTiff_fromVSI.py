from ij import IJ

#Run Olympus viewer 
IJ.run("Options", " ")
IJ.run("Viewer", "open=")
imp = IJ.getImage()

#Save as tiff
if IJ.saveAs(imp, "Tiff", ""):
    imp.close()
else:
    imp.close()
