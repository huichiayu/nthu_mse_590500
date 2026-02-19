# Make and write the daily book header files

for i in range(1,25):
    f = open(f"day_{i}.md", "w")
    f.write(f"Day {i}\n=======================\nThis section contains the course materials for day {i}.")
    f.close