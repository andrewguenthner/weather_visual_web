import cdstoolbox as ct


@ct.application(title='ag_0502_clim4', 
                description='Simple trial of temperature')
@ct.output.figure()
@ct.output.figure()
@ct.output.figure()
@ct.output.figure()
def ag_0502_clim4():
    """
    Application main steps:

    - retrieve the climatology data
    - show the result on three maps
    """

    data1 = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'product_type':'monthly_averaged_reanalysis',
            'variable':'10m_wind_speed',
            'year':'2018',
            'month':'09',
            'time':'00:00',
            'format':'grib'
        })

    data2 = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'product_type':'monthly_averaged_reanalysis',
            'variable':'10m_wind_speed',
            'year':'2018',
            'month':'10',
            'time':'00:00',
            'format':'grib'
        })
    
    data3 = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'product_type':'monthly_averaged_reanalysis',
            'variable':'10m_wind_speed',
            'year':'2018',
            'month':'11',
            'time':'00:00',
            'format':'grib'
        })
    
    data4 = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'product_type':'monthly_averaged_reanalysis',
            'variable':'10m_wind_speed',
            'year':'2018',
            'month':'12',
            'time':'00:00',
            'format':'grib'
        })
    
    fig1 = ct.cdsplot.geomap(data1, title = '', 
             pcolormesh_kwargs = {'cmap': 'Blues',
                                  'vmin' : 0, 
                                  'vmax' : 15})
    fig2 = ct.cdsplot.geomap(data2, title = '', 
             pcolormesh_kwargs = {'cmap': 'Blues',
                                  'vmin' : 0, 
                                  'vmax' : 15})
    fig3 = ct.cdsplot.geomap(data3, title = '', 
             pcolormesh_kwargs = {'cmap': 'Blues',
                                  'vmin' : 0, 
                                  'vmax' : 15})
    fig4 = ct.cdsplot.geomap(data4, title = '', 
             pcolormesh_kwargs = {'cmap': 'Blues',
                                  'vmin' : 0, 
                                  'vmax' : 15})
    return fig1, fig2, fig3, fig4
