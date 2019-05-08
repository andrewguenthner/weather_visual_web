import cdstoolbox as ct


@ct.application(title='ag_0504_clim_monthly_anomaly_clds', 
                description='Use 1981-2010 means to find anomaly for months in 2018')
@ct.output.figure()
@ct.output.figure()
@ct.output.figure()
@ct.output.figure()


def ag_0504_clim_monthly_anomaly_clds():
    """
    Application main steps:

    - retrieve the baseline data
    - retrieve the 2018 data
    - add a small value (1e-9) to baseline to prevent divide by zero error
    - compute the anomaly
    - plot the anomaly
    """

    clim_data1 = ct.catalogue.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'product_type':'monthly_averaged_reanalysis',
        'variable':
             'total_precipitation',
        'year':[
            '1980','1981','1982','1983',
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
        'month':'01',
        'time':'00:00',
        'format':'grib'
    })
    
    clim_data2 = ct.catalogue.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
     {
       'product_type':'monthly_averaged_reanalysis',
        'variable':
             'total_precipitation',
        'year':[
            '1980','1981','1982','1983',
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
        'month':'02',
        'time':'00:00',
        'format':'grib'
    })

    clim_data3 = ct.catalogue.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'product_type':'monthly_averaged_reanalysis',
        'variable':
             'total_precipitation',
        'year':[
            '1980','1981','1982','1983',
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
        'month':'03',
        'time':'00:00',
        'format':'grib'
    })

    clim_data4 = ct.catalogue.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
         'product_type':'monthly_averaged_reanalysis',
        'variable':
             'total_precipitation',
        'year':[
            '1980','1981','1982','1983',
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
        'month':'04',
        'time':'00:00',
        'format':'grib'
    })


    data1 = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'product_type':'monthly_averaged_reanalysis',
            'variable':'total_precipitation',
            'year':'2018',
            'month':'01',
            'time':'00:00',
            'format':'grib'
        })

    data2 = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'product_type':'monthly_averaged_reanalysis',
            'variable':'total_precipitation',
            'year':'2018',
            'month':'02',
            'time':'00:00',
            'format':'grib'
        })
    
    data3 = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'product_type':'monthly_averaged_reanalysis',
            'variable':'total_precipitation',
            'year':'2018',
            'month':'03',
            'time':'00:00',
            'format':'grib'
        })
    
    data4 = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'product_type':'monthly_averaged_reanalysis',
            'variable':'total_precipitation',
            'year':'2018',
            'month':'04',
            'time':'00:00',
            'format':'grib'
        })
    
    clim_mean1 = ct.climate.climatology_mean(clim_data1,
                                           '1981-01',
                                           '2010-01')
    clim_mean_a1 = ct.operator.add(clim_mean1, 0.000000001)                                       
    anom_data1 = ct.operator.div(data1, clim_mean_a1)
    
    clim_mean2 = ct.climate.climatology_mean(clim_data2,
                                           '1981-02',
                                           '2010-02')
    clim_mean_a2 = ct.operator.add(clim_mean2, 0.000000001)                                       
    anom_data2 = ct.operator.div(data2, clim_mean_a2)
    
    clim_mean3 = ct.climate.climatology_mean(clim_data3,
                                           '1981-03',
                                           '2010-03')
    clim_mean_a3 = ct.operator.add(clim_mean3, 0.000000001)                                       
    anom_data3 = ct.operator.div(data3, clim_mean_a3)
    
    clim_mean4 = ct.climate.climatology_mean(clim_data4,
                                           '1981-04',
                                           '2010-04')
    clim_mean_a4 = ct.operator.add(clim_mean4, 0.000000001)                                       
    anom_data4 = ct.operator.div(data4, clim_mean_a4)
    
    fig1 = ct.cdsplot.geomap(anom_data1, title = '', 
             pcolormesh_kwargs = {'cmap': 'RdYlGn',
                                  'vmin': 0,
                                  'vmax': 2})

    
    fig2 = ct.cdsplot.geomap(anom_data2, title = '', 
             pcolormesh_kwargs = {'cmap': 'RdYlGn',
                                  'vmin': 0,
                                  'vmax': 2})

    
    fig3 = ct.cdsplot.geomap(anom_data3, title = '', 
             pcolormesh_kwargs = {'cmap': 'RdYlGn',
                                  'vmin': 0,
                                  'vmax': 2})

    
    
    fig4 = ct.cdsplot.geomap(anom_data4, title = '', 
             pcolormesh_kwargs = {'cmap': 'RdYlGn',
                                  'vmin': 0,
                                  'vmax': 2})
    
    
    return fig1, fig2, fig3, fig4