def check_collisions(d):
    hash_map = {}
    for key in d:
        h = hash(key)
        if h in hash_map:
            hash_map[h].append(key)
        else:
            hash_map[h] = [key]
    return {h: keys for h, keys in hash_map.items() if len(keys) > 1}
collision_dict = {8: 'value1', 2**64: 'value2'}
print(collision_dict)
collisions = check_collisions(collision_dict)
print("Collisions found:")
for h, keys in collisions.items():
    print(f"Hash: {h}")
    for key in keys:
        print(f" - Key: {key}")
