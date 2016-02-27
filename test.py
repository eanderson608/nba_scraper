from datetime import date, timedelta as td

start_date = "20160222"
end_date = "20160224"

start_year = int(start_date[:4])
start_month = int(start_date[4:6])
start_day = int(start_date[6:])

end_year = int(end_date[:4])
end_month = int(end_date[4:6])
end_day = int(end_date[6:])

d1 = date(start_year, start_month, start_day)
d2 = date(end_year, end_month, end_day)

delta = d2 - d1

dates = []

for i in range(delta.days + 1):
    date = d1 + td(days=i)
    dates.append(str(date).replace("-", ""))

print(dates)


	