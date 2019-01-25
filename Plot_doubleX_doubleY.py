import numpy as np
import matplotlib.pyplot as plt
import math


# ------- Define the functions (or read the data in files) ------- 

X = np.array(range(10))+1	# X-axis
Yr = 40 - np.array(2*X)		# Function plotted on the right Y-axis
Yl = np.array(X**2)			# Function plotted on the left Y-axis
errYr = 0.2*Yr				# error on Yr
errYl = 0.1*Yl				# error on Yl


# ------- Create the figure ------- 

plt.clf()
fig = plt.figure(1, figsize=(1,1))	
fig, axr = plt.subplots(sharex=True, sharey=True)


# ------- Draw a fill_between plot in blue corresponding to the right axis------- 

axr.plot(X, Yr, color='steelblue', linewidth=5.0)
axr.fill_between(X, Yr-errYr, Yr+errYr, color='lavender')


# ------- Define the left axis parameters------- 

axl = axr.twinx()  
axl.tick_params(length=8, width=1, labelsize=22, color='black', labelcolor='black', axis='y')
axl.axis([-1, 11, -5, 120])
axl.yaxis.tick_left()
axl.yaxis.set_label_position("left")
axl.set_ylabel('Left title', fontsize=25)


# ------- Define the right axis parameters------- 

axr.tick_params(length=8, width=1, labelsize=22, color='steelblue', labelcolor='steelblue', axis='y')
axr.tick_params(length=8, width=1, labelsize=22, color='black', labelcolor='black', axis='x', top=False, bottom=True)
axr.axis([-1, 11, 10, 50])
axr.yaxis.tick_right()
axr.yaxis.set_label_position("right")
axr.yaxis.label.set_color('steelblue')
axr.set_ylabel('Right title', fontsize=25)
axr.set_xlabel('Bottom Title', fontsize=25)


# ------- Draw the scatter points corresponding to the left axis on top ------- 

axl.scatter(X, Yl, s = 80, color='black') #, facecolors='none')
axl.errorbar(X, Yl, yerr=errYl, ecolor='black', linestyle="None")


# ------- Define the parameters and redefine the ticks to plot for the top axis ------- 

axt = axl.twiny()  
axt.set_xlim(axl.get_xlim())
axt.xaxis.set_ticks_position("top")
axt.xaxis.set_label_position("top")

new_tick_locations = [0.5, 2.5, 4.5, 6.5, 8.5]	
def tick_function(X):
	V = np.log10(X)
	return ["%.1f" % z for z in V]

axt.set_xticks(new_tick_locations)
axt.set_xticklabels(tick_function(new_tick_locations))
axt.tick_params(length=8, width=1, labelsize=22, color='black', labelcolor='black', axis='x')
axt.set_xlabel('Top Title', fontsize=25) 
	

# ------- Save the plot ------- 

plt.savefig('Plot_doubleX_doubleY.pdf', bbox_inches='tight')


