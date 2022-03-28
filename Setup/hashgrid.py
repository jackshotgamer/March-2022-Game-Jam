from Setup import vector


class HashGrid:
    def __init__(self, bucket_size=230):
        self.bucket_size = bucket_size
        self.buckets = {}
        # objects that are located inside which buckets
        self.liquids = {}

    def get_liquids_pos(self, point):
        return self.buckets.get(point, [])

    def get_liquids_box(self, bounds):
        var = []
        for bound in self.iter_2d_bounds(bounds):
            if bound in self.buckets:
                var.extend(self.buckets[bound])
        return tuple(set(var))

    def remove_liquid(self, obj):
        if obj in self.liquids:
            op = self.liquids[obj]
            for list_ in op:
                list_.remove(obj)
            del self.liquids[obj]
            """
            liquids = {
               A: [[A, B, C], [A, C]]
            }
            pos1, pos2: 
            A: [[A, B, C], [A]]
            """

    def add_liquid(self, obj, bounds):
        for pos in self.iter_2d_bounds(bounds):
            """
            'test' = (100, 100) - (300, 300)
            bucket = buckets[...].append(obj)
            liquids.append(bucket)
            """
            self.liquids.setdefault(obj, []).append((bucket := self.buckets.setdefault(pos, [])).append(obj) or bucket)

    def to_bucket_index(self, point):
        return vector.Vector(int(point[0] / self.bucket_size), int(point[1] / self.bucket_size))

    def iter_2d_bounds(self, bounds):
        lower_left = self.to_bucket_index([min(bounds[0].x, bounds[1].x), min(bounds[0].y, bounds[1].y)])
        upper_right = self.to_bucket_index([max(bounds[0].x, bounds[1].x), max(bounds[0].y, bounds[1].y)])
        for num1 in range(lower_left.x, upper_right.x + 1):
            for num2 in range(lower_left.y, upper_right.y + 1):
                yield vector.Vector(num1, num2)

# hashg = HashGrid()
# hashg.add_liquid('E', (vector.Vector(0, 0), vector.Vector(1620, 911)))
# print(*hashg.get_liquids_box((vector.Vector(0, 0), vector.Vector(1620, 911))))
# hashg.remove_liquid('E')
# var = hashg.get_liquids_box((vector.Vector(0, 0), vector.Vector(1620, 911)))
# print(*(var if var else 'None'))
# print(hashg.buckets)
# print(len(hashg.buckets))
# print(hashg.liquids)
# print(len(hashg.liquids['E']))
