import requests


resp = requests.get("https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/08-14-2020.csv")


print(resp.text)

