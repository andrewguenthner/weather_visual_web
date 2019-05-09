# weather_visual_web

A showcase of the world's weather in 2018 using meteorological data from reanalyses.

Reanalysis is an often overlooked but extremely useful form of weather data.  It 
involves taking multiple sources of weather observations, putting them into a short-
term forecast model (such models are generally accurate for the purposes of large-
scale weather characteristics), and deriving what the weather must have been like
across a uniform grid in space and time in order to explain the observations.  Weather
agencies use reanalysis to provide a nicely formatted "starting point" for their 
forecast models, but in this project we use that data for the purposes of weather
visualization.  

The beauty of reanalyzed data is that is an ideal data set.  Generally speaking it is
uniformly gridded in space and time, while being free of missing or physically unrealistic
values.  Whereas a sample of weather stations will make for a nice enough data table, a
reanalysis is much nicer for the purposes of making maps and other graphical ways of 
representing the weather.  

2018 was an interesting year for weather.  Before it recedes too far into the past, I 
chose to combine my data science skills and love of weather into a project that shows
what we can do with reanalyzed data.

Requirements:  The web pages and images in the "images" directory are sufficient for 
static functionality.  In order to use the interactive tables, the remaining top-level
folders must be installed.  To reproduce all of the data processing that went into the
creation of the project, two raw NetCDF files from the European Union Copernicus project 
are needed.  These files are 100 MB and about 3 GB respectively, so they have not been
included in the GitHub repository.  They can, however, be fetched from the Copernicus
Climate Data Store by signing up for a free account and using their download service.  To
do so, you would need to query the ERA5 monthly means dataset for 2-m temperature, 10-m
wind speed, total cloud cover, and total precipitation, for each month of the year, using
the experimental NetCDF format.  You would need two files, one for 2018 data only and
one for 1981-2010 inclusive, to provide the climatology.  Everything else needed to
reproduce the data processing is in the folder, including raw source files and three
Jupyter notebooks.  

In order to reproduce the images, you would need to use the Climate Data Store's API.  This
API is in beta, so the exact procedures may change, however, the variables to be queried and
the sources are the same as those mentioned above.  The download service currently offers the
option of generating the query scripts (which are written in Python) for you based on your
selections.  The project folder "src" also includes a sub-folder with the queries used.  Note
that, in order to keep the requests to the server reasonable, the requests for creating the 
images were run 4 months at a time.  For each of the eight example queries, you would need
to run the query once with the given months, and then replace the month numbers with two new
sets to generate the remaining eight months worth of images.  Because the service is cloud-based
and still in beta, it is often available only intermittently, and sometimes generates errors
unrelated to your code, requiring you to re-submit the query.  As a result, if you want to 
generate these images yourself, please allow plenty of time (all 96 images may take several
hours).  

The data returned is gridded at 0.25 degree intervals.  To facilitate access to the data, the
site allows you to view interactive tables and download .csv files with the same information.
These data, however, are gridded at 3 degree intervals.  Thus you will lose some resolution if you
try to regenerate the images from the .csv data.  With 3-degree intervals, you get 7200 data points
per grid, which amounts to almost 700,000 data points to work with.  The full-resolution data would
involve about 100,000,000 data points -- not really suited for table browsing.  To make the tables
more interesting, I have merged each grid point with the name of the city having the highest population with the grid cell (with only cities of over 15,000 people included).  The country name
is also included, but corresponds to the country the city is located in, not necessarily the 
country where most of the grid cell is located.  This information gives you a rough way to
filter the table data by country.  The interactive viewer will also let you sort filtered or 
unfiltered columns, so that, for example, you can view a list of Canadian cities sorted by
absolute temperature from coldest to warmest.  

The data set uses four key variables:
  temperature at 2-m height (in deg C)
  monthly precipitation, normalized to mm per day (so that longer months are comparable to
  shorter ones).
  wind speeds, in m/s
  cloud cover, in %
For each variable, the departure from the 1980-2010 30-year mean is also included.  This mean
is a monthly average of the daily average quantity in question.  For temperatures, wind speeds,
and cloud cover, the departure is a simple difference from the mean.  For precipitation, it is
the percentage of the mean.  To avoid issues with division by zero, a very small number is added
to the precipitation total for each location, so that zero / "zero" shows up as zero, rather
than undefined. 