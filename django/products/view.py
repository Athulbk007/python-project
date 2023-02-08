from products.models import mobiles

# print(len(mobiles))
# for mob in mobiles:
#     print(mob.get("name"))

# print([m.get("name") for m in mobiles])
# samsung_mobiles = [mob.get("name") for mob in mobiles if mob.get("brand") == "samsung"]
# print(samsung_mobiles)

# max of price
print(max(mobiles, key=lambda m: m.get("price")))
# min of sort
print(min(mobiles, key=lambda m: m.get("price")))
# sort of price
print(sorted(mobiles, key=lambda m: m.get("price"), reverse=True))
