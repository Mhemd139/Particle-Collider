from functions_geometrics import euclidean_distance



class Particle:
    def __init__(self , position , direction, speed , radius , color):
        self.pos = position
        self.dir = direction
        self.speed = speed
        self.radius = radius
        self.color = color
        self.collision_status = False
    
    def guidance(self , box, particles):
        self.boundary_update_dir(box)


        #update direction if collision occured
        for particle in particles:
            if particle.pos != self.pos and self.collision_check(particle):
                if self.collision_status == False:
                    self.collision_status = True
                    self.collision_update_dir(particle)
                    break
                else:
                    break
            else:
                self.collision_status = False

    def boundary_update_dir(self, box):
        if self.pos[0] <= box[0] + self.radius and self.dir[0] < 0:
            self.dir = (self.dir[0] * -1, self.dir[1])
        elif self.pos[0] >= box[1] - self.radius and self.dir[0] > 0:
            self.dir = (self.dir[0] * -1, self.dir[1])
        if self.pos[1] <= box[2] + self.radius and self.dir[1] < 0:
            self.dir = (self.dir[0], self.dir[1] * -1)
        elif self.pos[1] >= box[3] - self.radius and self.dir[1] > 0:
            self.dir = (self.dir[0], self.dir[1] * -1)

    def collision_update_dir(self,particle):
        x = self.pos[0] - particle.pos[0]
        y = self.pos[1] - particle.pos[1]
        if abs(x)>=abs(y):
            self.dir = (x/abs(x) , y/abs(x))
        else:
            self.dir = (x/abs(y) , y/abs(y))

    def collision_check(self,particle):
        if euclidean_distance(particle.pos , self.pos)<=self.radius +particle.radius:
            return True
        return False
        

    def update_pos(self):
        self.speed +=0.1
        pos_x = self.pos[0] + self.dir[0] * self.speed
        pos_y = self.pos[1] + self.dir[1] * self.speed
        self.pos = (pos_x, pos_y)
