import random


class Bat:
    def __init__(self, pos, img, speed, depth):
        self.pos = list(pos)
        self.img = img
        self.speed = speed
        self.depth = depth
    
    def update(self):
        self.pos[0] += self.speed
        
    def render(self, surf, offset=(0, 0)):
        render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)
        surf.blit(self.img, (render_pos[0] % (surf.get_width() + self.img.get_width()) - self.img.get_width(), render_pos[1] % (surf.get_height() + self.img.get_height()) - self.img.get_height()))
        
class Bats:
    def __init__(self, images, count=3):
        self.bats = []
        
        for i in range(count):
            self.bats.append(Bat((random.random() * 99999, random.random() * 99999), random.choice(images), random.random() * 0.5 + 2, random.random() * 0.6 + 2.5))
        
        self.bats.sort(key=lambda x: x.depth)
    
    def update(self):
        for bat in self.bats:
            bat.update()
    
    def render(self, surf, offset=(0, 0)):
        for bat in self.bats:
            bat.render(surf, offset=offset)