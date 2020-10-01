# import the csv module
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	#for index, column_header in enumerate(header_row):
	#	print(index, column_header)
# I believe this prints each tuple


# Fill the highs list with the second column in each row
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0],'%Y-%m-%d')
			high = (int(row[1]))
			low = (int(row[3]))
		
		except ValueError:
			print(current_date, 'missing data')
		
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
	
# Plot data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='pink')
plt.plot(dates, lows, c='green')
plt.fill_between(dates,highs, lows, facecolor='blue', alpha=0.1)

# Format then Show Plot
plt.xlabel('', fontsize=16)
plt.ylim(0, 100)
plt.ylabel('Temperatures (*F)', fontsize=16)
plt.title('July 2014 High and Low Temperatures in Sitka', fontsize=25)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()

plt.show()

# I want to run this as a program and have different plots of temperatures on the same graph.
