import os
import pandas as pd
from jj_data_connector.ga4 import GA4Report, Metrics, Dimensions

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'sa_ga4_demo.json'
property_id = '307310528'

# creating GA4Report object instance
ga4 = GA4Report(property_id)

# variables
dimension_list = ['date', 'browser']
metric_list = ['totalUsers', 'bounceRate']
date_range1 = ('2022-03-01', '2022-03-31')
date_range2 = ('2022-04-01', '2022-04-30')

# run the GA4 report
report = ga4.run_report(
    dimension_list, 
    metric_list, 
    date_ranges=[date_range1, date_range2],
    row_limit=10,
    offset_row=10
)

report['row_count']

# report.keys()
print(report['response'])

report['headers']
report['rows']
df = pd.DataFrame(columns=report['headers'], data=report['rows'])
print(df)

# export to CSV and Excel files
df.to_csv('demo1.csv', index=False)
df.to_excel('demo1.xlsx', index=False)
