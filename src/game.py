class Game:
    def __init__(self, home, visit, home_points, visit_points):
        self.home = home
        self.visit = visit
        self.home_points = home_points
        self.visit_points = visit_points
    
    def set_home(self, home):
        self.home = home
    
    def set_visit(self, visit):
        self.visit = visit

    def set_home_points(self, points):
        self.home_points = points

    def set_visit_points(self, points):
        self.visit_points = points

    def get_home(self):
        return self.home

    def get_visit(self):
        return self.visit

    def get_home_points(self):
        return self.home_points

    def get_visit_points(self):
        return self.visit_points

    def __str__(self):
        return self.home + " " + self.visit + " " + str(self.home_points) + " " + str(self.visit_points)
