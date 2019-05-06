import cdstoolbox as ct


@ct.application(title='ag_0504_clim_monthly_anomaly', 
                description='Use 1981-2010 means to find anomaly for months in 2018')
@ct.output.figure()
@ct.output.figure()
@ct.output.figure()
@ct.output.figure()

def ag_0504_clim_monthly_anomaly():
    """
    Application main steps:

    - retrieve the baseline data
    - retrieve the 2018 data
    - compute the anomaly
    - plot the anomaly
    - the test version will show the baseline mean also
    """

    clim_data1 = ct.catalogue.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'product_type':'monthly_averaged_reanalysis',
        'variable':
             '2m_temperature',
        'year':[
            '1981','1982','1983',
            '1984','1985','1986',
            '1987','1988','1989',
            '1990','1991','1992',
            '1993','1994','1995',
            '1996','1997','1998',
            '1999','2000','2001',
            '2002','2003','2004',
            '2005','2006','2007',
            '2008','2009','2010'
        ],
        'month':'09',
        'time':'00:00',
        'format':'grib'
    })
    
    clim_data2 = ct.catalogue.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'product_type':'monthly_averaged_reanalysis',
        'variable':
             '2m_temperature',
        'year':[
            '1981','1982','1983',
            '1984','1985','1986',
            '1987','1988','1989',
            '1990','1991','1992',
            '1993','1994','1995',
            '1996','1997','1998',
            '1999','2000','2001',
            '2002','2003','2004',
            '2005','2006','2007',
            '2008','2009','2010'
        ],
        'month':'10',
        'time':'00:00',
        'format':'grib'
    })

    clim_data3 = ct.catalogue.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'product_type':'monthly_averaged_reanalysis',
        'variable':
             '2m_temperature',
        'year':[
            '1981','1982','1983',
            '1984','1985','1986',
            '1987','1988','1989',
            '1990','1991','1992',
            '1993','1994','1995',
            '1996','1997','1998',
            '1999','2000','2001',
            '2002','2003','2004',
            '2005','2006','2007',
            '2008','2009','2010'
        ],
        'month':'11',
        'time':'00:00',
        'format':'grib'
    })

    clim_data4 = ct.catalogue.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'product_type':'monthly_averaged_reanalysis',
        'variable':
             '2m_temperature',
        'year':[
            '1981','1982','1983',
            '1984','1985','1986',
            '1987','1988','1989',
            '1990','1991','1992',
            '1993','1994','1995',
            '1996','1997','1998',
            '1999','2000','2001',
            '2002','2003','2004',
            '2005','2006','2007',
            '2008','2009','2010'
        ],
        'month':'12',
        'time':'00:00',
        'format':'grib'
    })

    data1 = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'product_type':'monthly_averaged_reanalysis',
            'variable':'2m_temperature',
            'year':'2018',
            'month':'09',
            'time':'00:00',
            'format':'grib'
        })

    data2 = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'product_type':'monthly_averaged_reanalysis',
            'variable':'2m_temperature',
            'year':'2018',
            'month':'10',
            'time':'00:00',
            'format':'grib'
        })
    
    data3 = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'product_type':'monthly_averaged_reanalysis',
            'variable':'2m_temperature',
            'year':'2018',
            'month':'11',
            'time':'00:00',
            'format':'grib'
        })
    
    data4 = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'product_type':'monthly_averaged_reanalysis',
            'variable':'2m_temperature',
            'year':'2018',
            'month':'12',
            'time':'00:00',
            'format':'grib'
        })    
    
    clim_mean1 = ct.climate.climatology_mean(clim_data1,
                                           '1981-09',
                                           '2010-09')
    anom_data1 = ct.operator.sub(data1, clim_mean1)
    
    clim_mean2 = ct.climate.climatology_mean(clim_data2,
                                           '1981-10',
                                           '2010-10')
    anom_data2 = ct.operator.sub(data2, clim_mean2)
    
    clim_mean3 = ct.climate.climatology_mean(clim_data3,
                                           '1981-11',
                                           '2010-11')
    anom_data3 = ct.operator.sub(data3, clim_mean3)
  
    clim_mean4 = ct.climate.climatology_mean(clim_data4,
                                           '1981-12',
                                           '2010-12')
    anom_data4 = ct.operator.sub(data4, clim_mean4)

    fig1 = ct.cdsplot.geomap(anom_data1, title = '', 
             pcolormesh_kwargs = {'cmap': 'coolwarm',
                                  'vmin' : -6, 
                                  'vmax' : 6})

    fig2 = ct.cdsplot.geomap(anom_data2, title = '', 
             pcolormesh_kwargs = {'cmap': 'coolwarm',
                                  'vmin' : -6, 
                                  'vmax' : 6})

    fig3 = ct.cdsplot.geomap(anom_data3, title = '', 
             pcolormesh_kwargs = {'cmap': 'coolwarm',
                                  'vmin' : -6, 
                                  'vmax' : 6})    

    fig4 = ct.cdsplot.geomap(anom_data4, title = '', 
             pcolormesh_kwargs = {'cmap': 'coolwarm',
                                  'vmin' : -6, 
                                  'vmax' : 6})        
    
    return fig1, fig2, fig3, fig4
