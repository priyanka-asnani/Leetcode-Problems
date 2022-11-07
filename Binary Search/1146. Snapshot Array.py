class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.dict = {}
        self.snapshots = []
        

    def set(self, index: int, val: int) -> None:
        self.dict[index] = val

    def snap(self) -> int:
        self.snapshots.append(self.dict.copy())
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snapshots[snap_id]:
            return self.snapshots[snap_id][index]
        else: return 0
        
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)