import matplotlib
matplotlib.use('TkAgg')
import pylidc as pl
import matplotlib.pyplot as plt
from skimage.measure import find_contours


qu = pl.query(pl.Scan).filter(pl.Scan.slice_thickness <= 1)
scan = qu.first()
sid = scan.patient_id
qu = pl.query(pl.Scan).filter(pl.Scan.patient_id == sid)
qu[0].annotations[0]._nodule_id
qu[0].annotations[0].estimate_diameter()

count  = 0
while count < 10:
	print(qu[0].annotations[count].estimate_diameter())

nods  =qu[0].cluster_annotations()
len(nods)

for i,nod in enumerate(nods):
	print "Nodule", i+1, "has", len(nod), "annotations."
	for j,ann in enumerate(nod):
		print "-- Annotation", j+1, "centroid:", ann.centroid()
