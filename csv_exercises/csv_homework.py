import csv

solar_sys = []

with open("galaxies.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        solar_sys.append(line)
# print(solar_sys)

solar_stats = []
maximum = []
minimum = []

for item in range(1,len(solar_sys)):
    # solar_stats.append((f"(galaxy = {int(solar_sys[item][0])}, system = {int(solar_sys[item][1])}"))
    solar_stats.append((int(solar_sys[item][0]), int(solar_sys[item][1])))
    
#print(solar_stats)   
maximum.append(max(solar_stats))
minimum.append(min(solar_stats))
print(f"Galaxiy {minimum[0][0]} has a min velocity of {minimum[0][1]}km/sec")
print(f"Galaxiy {maximum[0][0]} has a max velocity of {maximum[0][1]}km/sec")