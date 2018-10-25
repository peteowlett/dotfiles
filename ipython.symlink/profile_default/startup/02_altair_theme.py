def dark_enhanced():
    return {'config':
	    {'title': {'color': 'black'}, #NOT WORKING
		'axis': {'titleColor': 'black', #axis titles
		    'domainColor': 'black', #domain color colors the bar on axis labels
		    'gridColor': 'black', #grid color is most of the grid except the right hand side
		    'labelColor': 'black', #text labels of the axes
		    'tickColor': 'black'} #tick marks
		}}

try:
    import altair as alt
    alt.themes.register('dark_enhanced', dark_enhanced)
    alt.themes.enable('dark_enhanced')
except:
    print('Failed to load Altair style')
