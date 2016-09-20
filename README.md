## Summary  
This visualization was generated using the PISA dataset, which is an international metric of student achievement. The map component shows, at glance, how different countries compare in math, reading, or science. When the user clicks on a country, the scatterplot will populate with that country's data broken down by socioeconomic quintile. Up to 5 countries can be selected at once on the scatterplot, allowing the user to see how the richest and poorest students from various countries compare.  

## Design  
### Map Rationale  
I chose to use a chloropleth map to compare the various countries, rather than a bar chart or scatter plot, for two primary reasons. First, with about 65 countries included in the dataset, it would be a challenge for the user to see which point or bar represented which country. This could be solved with hover-text, as I used in the map, but I felt that the map allowed a more intuitive user interface. You don't need to hover over the United States, for example, to see how it compares to China.  
The other reason I chose the map, is that it makes it very obvious which countries are not represented in the dataset: all of Africa, most of the Middle East, and India. During my exploratory data analysis, which I performed in R, I didn't notice how many countries were un-represented. It was only after I plotted it on the map that this became evident. So I decided to stick with the map to allow the reader the same observation.  
For the color scale and legend, I experimented with various choices off the Color Brewer pallettes. My final selections offered the most visual distinction between the score groups while still maintaining a monochromatic theme. The score groups were calcualted using d3's quantile function, and I rounded all values on the legend and hovertext for clarity.
### Scatter Plot Rationale
My scatter plot plan did go through a few iterations, but they all occured before I actually got any code working. Mike from Udacity offered some very helpful feedback on my plan, which led to the difference between my inital idea and what I actually ended up producing.  
My inial plan was to have the map cover the entire screen, and have the scatterplot popup when a country was clicked. I was thinking that the user could click two countries and look at two small scatterplot windows side by side. I also planned to use the entire dataset, rather than aggregating by quintile and plotting median scores.  
Mike pointed out that the popup window idea wasn't the most user friendly, and that calling a 20MB dataset each time a country was clicked was probably not a great idea either. He suggested aggregating the data by quintiles. I made a few sample plots in R and found that not only did this strategy reduce my dataset to a fraction of the original size, it was also a lot easier to interpret.  
I decided to allow the user to compare up to 5 countries on the scatterplot. More than that would make it difficult to read, and also require the legend to take up too much space.

##Feedback
* Mike Yi (Udacity Coach) - Discussed in the previous section
* Kevin Lohman - observed that the map and plot don't dynamically update when the window is re-sized. This is great feedback, but I felt it went beyond the scope of this project. I may incorporate it at some point in the future. He also thought it would be better if, instead of clearing the scatterplot when the user changes the subject, the scatterplot refreshed with the different subject data for the countries selected. I agreed that this would be preferable and I added in the code to accomplish it.
* Ashutosh Singh (Udacity Forum Mentor) - suggested either replacing the points on the scatterplot with lines, or adding lines to connect the points. I decided to add lines to connect the points, and after adding them in, agreed that it really did make the plot easier to interpret.


##Resources
http://www.r-tutor.com/r-introduction/data-frame/data-import
https://stat.ethz.ch/R-manual/R-devel/library/base/html/nrow.html
https://stat.ethz.ch/R-manual/R-devel/library/utils/html/read.table.html
http://www.r-tutor.com/r-introduction/data-frame/data-frame-row-slice
http://www.statmethods.net/stats/correlations.html
http://rprogramming.net/rename-columns-in-r/
http://docs.ggplot2.org/0.9.3.1/geom_bar.html
http://stackoverflow.com/questions/1330989/rotating-and-spacing-axis-labels-in-ggplot2
http://stackoverflow.com/questions/21982987/mean-per-group-in-a-data-frame
https://www.oecd.org/pisa/pisaproducts/PISA%202012%20Technical%20Report_Chapter%2016.pdf
https://stat.ethz.ch/R-manual/R-devel/library/utils/html/write.table.html
https://bl.ocks.org/mbostock/5577023
http://stackoverflow.com/questions/1458349/installing-jquery
http://learnjsdata.com/read_data.html
http://bl.ocks.org/biovisualize/1016860
http://stackoverflow.com/questions/10805184/d3-show-data-on-mouseover-of-circle
https://github.com/d3/d3-selection/blob/master/README.md#selection_on
http://stackoverflow.com/questions/11043026/variable-as-the-property-name-in-a-javascript-object-literal
http://stackoverflow.com/questions/4711036/assign-an-initial-value-to-radio-button-as-checked
http://bl.ocks.org/d3noob/7030f35b72de721622b8
http://stackoverflow.com/questions/10689055/create-an-empty-data-frame
http://stackoverflow.com/questions/11561856/add-new-row-to-dataframe
http://www.snippetexample.com/2014/09/add-new-row-dataframe-r/
https://www.r-bloggers.com/quartiles-deciles-and-percentiles/
http://www.w3schools.com/jsref/met_win_open.asp
https://discussions.udacity.com/t/how-to-pass-parameters-to-d3-json-or-otherwise-intellegently-organize-code/187255/2
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/quantile.html
http://www.d3noob.org/2013/01/selecting-filtering-subset-of-objects.html
http://bl.ocks.org/kobben/8576867
http://www.d3noob.org/2013/07/arranging-more-than-one-d3js-graph-on.html
http://www.barelyfitz.com/screencast/html-training/css/positioning/
http://stackoverflow.com/questions/623172/how-to-get-image-size-height-width-using-javascript
http://stackoverflow.com/questions/4910054/how-to-get-the-height-of-a-element-including-padding-and-borders-using-javascrip
http://stackoverflow.com/questions/351409/appending-to-array
http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
http://www.d3noob.org/2013/01/how-to-rotate-text-labels-for-x-axis-of.html
https://ariya.io/2014/02/javascript-array-slice-vs-splice
http://stackoverflow.com/questions/9050345/selecting-last-element-in-javascript-array
http://www.w3schools.com/css
http://stackoverflow.com/questions/5842194/css-aligning-elements-inside-a-div
https://stats.oecd.org/glossary/detail.asp?ID=5401
http://www.oecd.org/pisa/pisaproducts/datavisualizationcontest.htm
http://www.oecd.org/pisa/pisaproducts/pisadataanalysismanualspssandsassecondedition.htm
http://stackoverflow.com/questions/3330193/early-exit-from-function
https://www.dashingd3js.com/svg-paths-and-d3js
http://bl.ocks.org/d3noob/38744a17f9c0141bcd04
