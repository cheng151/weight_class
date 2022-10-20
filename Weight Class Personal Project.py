class MenWeight:
    """This class is for men's UFC weight-classes"""
    def __init__(self, m_weight):
        self.m_weight = m_weight

    def get_m_weight(self):
        """ Categortizing weight classes"""
        if self.m_weight <= 115:
            return ("You are strawweight.")
        elif self.m_weight <= 125:
            print("You are flyweight.")
        elif self.m_weight <= 135:
            print("You are bantamweight.")
        elif self.m_weight <= 145:
            print("You are featherweight.")
        elif self.m_weight <= 155:
            print("You are lightweight.")
        elif self.m_weight <= 165:
            print("You are super lightweight.")
        elif self.m_weight <= 170:
            print("You are welterweight.")
        elif self.m_weight <= 175:
            print("You are super welterweight.")
        elif self.m_weight <= 185:
            print("You are middleweight.")
        elif self.m_weight <= 195:
            print("You are super middleweight.")
        elif self.m_weight <= 205:
            print("You are light heavyweight.")
        elif self.m_weight <= 225:
            print("You are cruiserweight.")
        elif self.m_weight <= 265:
            print("You are heavyweight.")
        elif self.m_weight > 265:
            print("You are super heavyweight.")
        else:
            print("Please enter a valid weight.")

print(MenWeight(110))

### put user input in def main(): function