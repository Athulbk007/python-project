from collections import Counter
from json import load

with open("db.json", "r", encoding="utf=8") as f:
    data = load(f)
# print(len(data))
# movie names
# print([m.get("title") for m in data])
# # movies release in 2002
# print([m.get("title") for m in data if m.get("year") == "2002"])


# list movies in generes comedy
# print([d.get('title') for d in data if 'Comedy' in d.get('genres')])

# # max run in time movie
# lengthy_movie = max(data, key=lambda m: int(m.get('runtime')))
# print(lengthy_movie)
#
# # min run in time movie
# short_movie = min(data, key=lambda m: int(m.get('runtime')))
# print(short_movie)

# year wise movie count
mc = {}
for m in data:
    year = m.get('year')
    if year in mc:
        mc[year] += 1
    else:
        mc[year] = 1
# print(mc)

# which year most movie released
print(max(mc,key=lambda k: mc.get(k)))
# print(max(mc,key=lambda t:t[1]))