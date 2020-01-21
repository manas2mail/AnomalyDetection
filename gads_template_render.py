# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 01:58:40 2020

@author: 703239908
"""


import datetime
from jinja2 import Template
import pandas as pd

#returns the html body with populated values
def fnManin(ra_shop, engine_model, keyword):
    
    #framing the combination
    combination = ra_shop +'_'+ engine_model +'_'+ keyword
    
    #framing the image names
    timeseriessplot = (combination + '_'+'timeseriessplot.png').replace(" ", "")
    stackedbarplot_fm = (combination + '_'+ 'stackedbarplot_fm.png').replace(" ", "")
    stackedbarplot_ogp = (combination + '_'+'stackedbarplot_ogp.png').replace(" ", "")    
        
    #storing email body values in dict of dict           
    data =  {
              'ACSC_CF34-8E_HPT NUT': {
                'anomaly_date': datetime.date(2019, 8, 1),
                'target_mean': 0.24,
                'anomaly_mean': 1.0,
                'non_alert_mean': 0.08,
                'historical_alert_mean': 0,
                'standard_mean': 0.08,
                'reference_value': 0.24,
                'alert_type': 'new alert',
                'N_anomaly': 34,
                'N_standard': 166
              },
              'Cal_GENX-1B_DEFLECTOR, HPC - REAR': {
                'anomaly_date': datetime.date(2019, 4, 28),
                'target_mean': 1.73,
                'anomaly_mean': 2.0,
                'non_alert_mean': 1.61,
                'historical_alert_mean': 2.0,
                'standard_mean': 1.69,
                'reference_value': 1.73,
                'alert_type': 'new alert',
                'N_anomaly': 15,
                'N_standard': 109
              },
              'Cal_GENX-2B_HARNESS, ELECTRICAL': {
                'anomaly_date': datetime.date(2019, 12, 23),
                'target_mean': 0.1,
                'anomaly_mean': 0.54,
                'non_alert_mean': 0.06,
                'historical_alert_mean': 0,
                'standard_mean': 0.06,
                'reference_value': 0.1,
                'alert_type': 'new alert',
                'N_anomaly': 13,
                'N_standard': 187
              },
              'Celma_CF34-10E_HARNESS ASSY': {
                'anomaly_date': datetime.date(2019, 10, 29),
                'target_mean': 0.07,
                'anomaly_mean': 0.24,
                'non_alert_mean': 0.05,
                'historical_alert_mean': 0,
                'standard_mean': 0.05,
                'reference_value': 0.07,
                'alert_type': 'new alert',
                'N_anomaly': 17,
                'N_standard': 148
              },
              'Celma_CF34-10E_SELF CLOSING VALVE - LRU': {
                'anomaly_date': datetime.date(2019, 6, 3),
                'target_mean': 0.7,
                'anomaly_mean': 1.0,
                'non_alert_mean': 0.63,
                'historical_alert_mean': 0,
                'standard_mean': 0.63,
                'reference_value': 0.7,
                'alert_type': 'new alert',
                'N_anomaly': 23,
                'N_standard': 104
              },
              'Celma_CF6-80C_BELLCRANK-ACTR': {
                'anomaly_date': datetime.date(2019, 11, 6),
                'target_mean': 0.18,
                'anomaly_mean': 0.89,
                'non_alert_mean': 0.13,
                'historical_alert_mean': 0,
                'standard_mean': 0.13,
                'reference_value': 0.18,
                'alert_type': 'new alert',
                'N_anomaly': 9,
                'N_standard': 118
              },
              'Celma_CF6-80C_RING-DAMPENING': {
                'anomaly_date': datetime.date(2019, 11, 1),
                'target_mean': 0.22,
                'anomaly_mean': 0.44,
                'non_alert_mean': 0.18,
                'historical_alert_mean': 0.44,
                'standard_mean': 0.2,
                'reference_value': 0.22,
                'alert_type': 'new alert',
                'N_anomaly': 9,
                'N_standard': 191
              },
              'Celma_CF6-80C_WASHER-FLAT': {
                'anomaly_date': datetime.date(2019, 3, 21),
                'target_mean': 1.58,
                'anomaly_mean': 4.16,
                'non_alert_mean': 0.37,
                'historical_alert_mean': 0,
                'standard_mean': 0.37,
                'reference_value': 1.58,
                'alert_type': 'new alert',
                'N_anomaly': 63,
                'N_standard': 135
              },
              'Celma_CFM56-5B_BUSHING - HPC VSV': {
                'anomaly_date': datetime.date(2019, 11, 29),
                'target_mean': 21.14,
                'anomaly_mean': 51.27,
                'non_alert_mean': 17.25,
                'historical_alert_mean': 43.5,
                'standard_mean': 19.14,
                'reference_value': 21.14,
                'alert_type': 'new alert',
                'N_anomaly': 11,
                'N_standard': 166
              },
              'Celma_CFM56-5B_PANEL - ACOUSTIC': {
                'anomaly_date': datetime.date(2019, 12, 5),
                'target_mean': 0.6,
                'anomaly_mean': 1.85,
                'non_alert_mean': 0.51,
                'historical_alert_mean': 0,
                'standard_mean': 0.51,
                'reference_value': 0.6,
                'alert_type': 'new alert',
                'N_anomaly': 13,
                'N_standard': 187
              },
              'Celma_CFM56-7B_CASE - FAN CONTAINMENT': {
                'anomaly_date': datetime.date(2019, 12, 3),
                'target_mean': 0.36,
                'anomaly_mean': 0.78,
                'non_alert_mean': 0.35,
                'historical_alert_mean': 0,
                'standard_mean': 0.35,
                'reference_value': 0.36,
                'alert_type': 'new alert',
                'N_anomaly': 9,
                'N_standard': 191
              },
              'Celma_CFM56-7B_KIT WEIGHT BALANCE': {
                'anomaly_date': datetime.date(2019, 11, 23),
                'target_mean': 0.5,
                'anomaly_mean': 0.88,
                'non_alert_mean': 0.27,
                'historical_alert_mean': 0.9,
                'standard_mean': 0.45,
                'reference_value': 0.5,
                'alert_type': 'new alert',
                'N_anomaly': 26,
                'N_standard': 174
              },
              'Celma_CFM56-7B_RING - ACTUATING VBV': {
                'anomaly_date': datetime.date(2019, 12, 19),
                'target_mean': 0.04,
                'anomaly_mean': 0.33,
                'non_alert_mean': 0.03,
                'historical_alert_mean': 0.2,
                'standard_mean': 0.04,
                'reference_value': 0.04,
                'alert_type': 'new alert',
                'N_anomaly': 6,
                'N_standard': 194
              },
              'Celma_CFM56-7B_RING - ACTUATION, HPC STATOR 2': {
                'anomaly_date': datetime.date(2019, 12, 20),
                'target_mean': 0.6,
                'anomaly_mean': 1.2,
                'non_alert_mean': 0.57,
                'historical_alert_mean': 0,
                'standard_mean': 0.57,
                'reference_value': 0.6,
                'alert_type': 'new alert',
                'N_anomaly': 10,
                'N_standard': 190
              },
              'Celma_GENX-1B_SHIELD, HEAT - HPTR': {
                'anomaly_date': datetime.date(2019, 11, 11),
                'target_mean': 0.04,
                'anomaly_mean': 0.29,
                'non_alert_mean': 0.03,
                'historical_alert_mean': 0,
                'standard_mean': 0.03,
                'reference_value': 0.04,
                'alert_type': 'new alert',
                'N_anomaly': 7,
                'N_standard': 118
              },
              'Hungary_CFM56-5B_BLANKET - INSULATION ETC.': {
                'anomaly_date': datetime.date(2019, 11, 22),
                'target_mean': 0.28,
                'anomaly_mean': 1.0,
                'non_alert_mean': 0.26,
                'historical_alert_mean': 0,
                'standard_mean': 0.26,
                'reference_value': 0.28,
                'alert_type': 'new alert',
                'N_anomaly': 8,
                'N_standard': 192
              },
              'Hungary_CFM56-7B_HOSE': {
                'anomaly_date': datetime.date(2020, 1, 4),
                'target_mean': 0.02,
                'anomaly_mean': 0.33,
                'non_alert_mean': 0.01,
                'historical_alert_mean': 0,
                'standard_mean': 0.01,
                'reference_value': 0.02,
                'alert_type': 'new alert',
                'N_anomaly': 6,
                'N_standard': 194
              },
              'McAllen_CF34-8E_LPT BLADE S4': {
                'anomaly_date': datetime.date(2019, 10, 18),
                'target_mean': 5.1,
                'anomaly_mean': 22.11,
                'non_alert_mean': 3.86,
                'historical_alert_mean': 0,
                'standard_mean': 3.86,
                'reference_value': 5.1,
                'alert_type': 'new alert',
                'N_anomaly': 9,
                'N_standard': 124
              },
              'McAllen_CF34-8E_LPT BLADE S5': {
                'anomaly_date': datetime.date(2019, 11, 5),
                'target_mean': 3.89,
                'anomaly_mean': 24.43,
                'non_alert_mean': 2.42,
                'historical_alert_mean': 0,
                'standard_mean': 2.42,
                'reference_value': 3.89,
                'alert_type': 'new alert',
                'N_anomaly': 7,
                'N_standard': 98
              },
              'P62_CFM56-7B_SEAL - HPC STG 4 INTERSTAGE': {
                'anomaly_date': datetime.date(2019, 11, 22),
                'target_mean': 0.85,
                'anomaly_mean': 4.8,
                'non_alert_mean': 0.75,
                'historical_alert_mean': 0,
                'standard_mean': 0.75,
                'reference_value': 0.85,
                'alert_type': 'new alert',
                'N_anomaly': 5,
                'N_standard': 195
              },
              'Wales_CFM56-5B_BELLCRANK - HPC VSV': {
                'anomaly_date': datetime.date(2019, 11, 3),
                'target_mean': 0.22,
                'anomaly_mean': 0.7,
                'non_alert_mean': 0.17,
                'historical_alert_mean': 0.6,
                'standard_mean': 0.19,
                'reference_value': 0.22,
                'alert_type': 'new alert',
                'N_anomaly': 10,
                'N_standard': 190
              },
              'Wales_CFM56-7B_DISK - HPC STG 3': {
                'anomaly_date': datetime.date(2019, 10, 22),
                'target_mean': 0.45,
                'anomaly_mean': 0.92,
                'non_alert_mean': 0.39,
                'historical_alert_mean': 0,
                'standard_mean': 0.39,
                'reference_value': 0.45,
                'alert_type': 'new alert',
                'N_anomaly': 13,
                'N_standard': 101
              },
              'Wales_CFM56-7B_FAIRING - STRUT 10': {
                'anomaly_date': datetime.date(2019, 9, 23),
                'target_mean': 0.2,
                'anomaly_mean': 0.6,
                'non_alert_mean': 0.16,
                'historical_alert_mean': 0,
                'standard_mean': 0.16,
                'reference_value': 0.2,
                'alert_type': 'new alert',
                'N_anomaly': 10,
                'N_standard': 102
              },
              'Wales_CFM56-7B_SEAL - HPC CDP': {
                'anomaly_date': datetime.date(2019, 10, 17),
                'target_mean': 0.44,
                'anomaly_mean': 0.93,
                'non_alert_mean': 0.37,
                'historical_alert_mean': 0,
                'standard_mean': 0.37,
                'reference_value': 0.44,
                'alert_type': 'new alert',
                'N_anomaly': 14,
                'N_standard': 105
              },
              'Wales_CFM56-7B_SHAFT - HPC': {
                'anomaly_date': datetime.date(2019, 10, 28),
                'target_mean': 0.48,
                'anomaly_mean': 0.9,
                'non_alert_mean': 0.44,
                'historical_alert_mean': 0,
                'standard_mean': 0.44,
                'reference_value': 0.48,
                'alert_type': 'new alert',
                'N_anomaly': 10,
                'N_standard': 96
              },
              'Wales_CFM56-7B_SHAFT - HPT REAR': {
                'anomaly_date': datetime.date(2019, 10, 28),
                'target_mean': 0.45,
                'anomaly_mean': 0.9,
                'non_alert_mean': 0.41,
                'historical_alert_mean': 0,
                'standard_mean': 0.41,
                'reference_value': 0.45,
                'alert_type': 'new alert',
                'N_anomaly': 10,
                'N_standard': 109
              },
              'Wales_CFM56-7B_SHROUD ASSY-SEGMENT': {
                'anomaly_date': datetime.date(2019, 10, 27),
                'target_mean': 0.42,
                'anomaly_mean': 2.45,
                'non_alert_mean': 0.31,
                'historical_alert_mean': 0,
                'standard_mean': 0.31,
                'reference_value': 0.42,
                'alert_type': 'new alert',
                'N_anomaly': 11,
                'N_standard': 189
              },
              'Wales_CFM56-7B_SPOOL - HPC STG 1-2': {
                'anomaly_date': datetime.date(2019, 10, 22),
                'target_mean': 0.43,
                'anomaly_mean': 0.92,
                'non_alert_mean': 0.38,
                'historical_alert_mean': 0,
                'standard_mean': 0.38,
                'reference_value': 0.43,
                'alert_type': 'new alert',
                'N_anomaly': 12,
                'N_standard': 108
              },
              'Wales_CFM56-7B_SPOOL - HPC STG 4-9': {
                'anomaly_date': datetime.date(2019, 10, 22),
                'target_mean': 0.44,
                'anomaly_mean': 1.0,
                'non_alert_mean': 0.38,
                'historical_alert_mean': 0,
                'standard_mean': 0.38,
                'reference_value': 0.44,
                'alert_type': 'new alert',
                'N_anomaly': 11,
                'N_standard': 102
              },
              'Wales_CFM56-7B_TURBINE REAR FRAME': {
                'anomaly_date': datetime.date(2019, 11, 21),
                'target_mean': 0.04,
                'anomaly_mean': 0.4,
                'non_alert_mean': 0.02,
                'historical_alert_mean': 0,
                'standard_mean': 0.02,
                'reference_value': 0.04,
                'alert_type': 'new alert',
                'N_anomaly': 10,
                'N_standard': 190
              },
              'Wales_GE90-90_LINK - THRUST ENGINE MOUNT': {
                'anomaly_date': datetime.date(2019, 10, 15),
                'target_mean': 0.28,
                'anomaly_mean': 0.6,
                'non_alert_mean': 0.26,
                'historical_alert_mean': 0,
                'standard_mean': 0.26,
                'reference_value': 0.28,
                'alert_type': 'new alert',
                'N_anomaly': 10,
                'N_standard': 159
              },
              'Wales_GP7200_TUBE-PRESSURE, BEARING #5': {
                'anomaly_date': datetime.date(2019, 11, 4),
                'target_mean': 0.39,
                'anomaly_mean': 0.82,
                'non_alert_mean': 0.36,
                'historical_alert_mean': 0,
                'standard_mean': 0.36,
                'reference_value': 0.39,
                'alert_type': 'new alert',
                'N_anomaly': 11,
                'N_standard': 181
              }
            }
              
              
    df = pd.DataFrame(data)
    print(df)
    
    df.to_csv(r'data.csv')
    
    #fetching dict values based on combination
    data = data[combination]
    
    # fetching data values to build email body
    anomaly_date = data['anomaly_date']
    target_mean = data['target_mean']
    anomaly_mean = data['anomaly_mean']
    non_alert_mean = data['non_alert_mean'] 
    historical_alert_mean = data['historical_alert_mean']
    standard_mean = data['standard_mean']
    reference_value = data['reference_value']
    alert_type = data['alert_type']
    N_anomaly = data['N_anomaly']
    N_standard = data['N_standard']
    
    
#    alert_type = data['alert_type']
#    if(alert_type == 'new alert'):
#        email_subject = 'NEW Anomaly Detected on ' + engine_model +' '+ keyword + ' at ' + ra_shop
#    else:
#        email_subject = 'Anomaly EXTENDED for ' + engine_model +' '+ keyword + ' at ' + ra_shop


    #creating template
    main = Template(''' <html> <head> <style>table.table1, table.table1 th, table.table1 td{border: 1px solid black; border-collapse: collapse; font-weight: normal; padding-bottom:3px; padding-left:5px; padding-top:3px; padding-right:5px;}table.table2 td{padding: 10px;}</style> </head> <body> <br><p>An anomalous signal has been detected starting on <b>{{anomaly_date}}</b> in the scrap on the <span style="color:red;font-weight:bold;">{{engine_model}} {{keyword}}</span> at <span style="color:red;font-weight:bold;">{{ra_shop}}</span> resulting in an <b>increase</b> in scrap from <b>{{standard_mean}}({{N_standard}})</b> to <b>{{anomaly_mean}}({{N_anomaly}})</b>. </p><p> <table class="table1"> <tr> <th>Shop</th> <th>Engine Model</th> <th>Keyword</th> <th>Anomaly Date</th> <th>Historical Alert Mean</th> <th>Non Alert Mean</th> <th>Alert Mean</th> <th>Population Mean</th> <th>Reference Value</th> </tr><tr> <th>{{ra_shop}}</th> <th>{{engine_model}}</th> <th>{{keyword}}</th> <th>{{anomaly_date}}</th> <th>{{historical_alert_mean}}</th> <th>{{non_alert_mean}}</th> <th>{{anomaly_mean}}</th> <th>{{target_mean}}</th> <th>{{reference_value}}</th> </tr></table> </p><p> <span style="font-weight:bold; text-decoration: underline;"> Time Series Plot - Non Transformed</span> <br><img src=static/{{timeseriessplot}}> <br></p><p> <table class="table2"> <tr> <td><span style="font-weight:bold; text-decoration: underline;"> Top Scrap Causes </span></td></tr><tr> <td><img src=static/{{stackedbarplot_fm}}></td></tr><tr> <td><span style="font-weight:bold; text-decoration: underline;"> Top Part Numbers </span></td></tr><tr> <td><img src=static/{{stackedbarplot_ogp}}></td></tr></table> </p></body> </html> ''')
    
    #rendering data
    html = main.render(ra_shop = ra_shop, engine_model = engine_model, keyword = keyword, standard_mean = standard_mean,  N_standard = N_standard, anomaly_mean = anomaly_mean, N_anomaly = N_anomaly, anomaly_date = anomaly_date, target_mean = target_mean, 
                           timeseriessplot = timeseriessplot, stackedbarplot_fm = stackedbarplot_fm, stackedbarplot_ogp=stackedbarplot_ogp,
                           historical_alert_mean = historical_alert_mean, non_alert_mean = non_alert_mean, reference_value = reference_value, alert_type = alert_type )
    
    return html


html= fnManin("1", "1", "2")
    
    


