class p:
    def set(self, x, y,z):
        self.x=x
        self.y=y
        self.z=z
pt=p()
pt.set(5, 7,6)
print(getattr(pt, 'z', False))