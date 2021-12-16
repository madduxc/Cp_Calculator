# Authors       : Charles D. Maddux
#               :
#               :
# Date          : August 29, 2021
# Description   : Program to take input of model rocket geometry and output Center of Pressure as
#                 measured from the tip of the nose cone.  See Notes.txt for full description

import math

class Rocket():
    """
    object to define Rocket and its parameters, retrieve data, etc
    """
    def __init__(self, name):
        """
        defines Rocket objects, retrieves private members and stores calculated values
        :param name:        (string) name of rocket
        :param diameter:    (float) diameter of the upper rocket body tube
        :param num_fins:    (int) number of fins attached to the lower body tube
        """
        self._name = name                   # string name of rocket
        self._diameter = []                 # [in] diameter of rocket body tubes (must be entered in order, nose-to-tail)
        self._length = 0                    # [in] total length of rocket
        self._num_fins = 0                  # number of fins
        self._components = {}               # {} dictionary of components analyzed and corresponding length
        self._x_bar = []                    # [in] array of x_bar values corresponding to components
        self._comp_Cn_alpha = []            # [] array of Cn_alpha values corresponding to components

    def get_name(self):
        """
        Returns the Rocket name property when called
        :return: Rocket._name
        """
        return self._name

    def add_diameter(self, dia):
        """
        Module to add a body tube diameter value to the Rocket diameter array
        :param dia: (float) diameter of a given component
        :return: none
        """
        self._diameter.append(dia)

    def get_diameter(self):
        """
        Returns the Rocket diameter property when called
        :return: Rocket._diameter
        """
        return self._diameter[0]

    def add_fins(self, num_fins):
        """
        Adds the number of fins to Rocket class object
        :param num_fins: (int)
        :return: none
        """
        self._num_fins = num_fins


    def get_num_fins(self):
        """
        Returns the Rocket number of fins property when called
        :return: Rocket._num_fins
        """
        return self._num_fins

    def add_component(self, comp, length):
        """
        Module to add a component to the Rocket component array
        :param comp: (string) name of component
        :param length: (float) length of component
        :return: none
        """
        self._components[comp] = length

    def get_components(self):
        """
        Returns the list of Rocket components when called
        :return: Rocket._components
        """
        return self._components

    def add_x_bar(self, x_bar):
        """
        Module to add a component x_bar value to the Rocket x_bar array
        :param x_bar: (float) distance (from tip of nose cone) to Cp of a given component
        :return: none
        """
        self._x_bar.append(x_bar)

    def get_x_bar(self):
        """
        Returns the list of Rocket x_bar values when called
        :return: Rocket._x_bar
        """
        return self._x_bar

    def add_Cn_alpha(self, Cn_alpha):
        """
        Module to add a component Cn_alpha value to the Rocket comp_Cn_alpha array
        :param Cn_alpha: (float) Normal force coefficient of a given component
        :return: none
        """
        self._comp_Cn_alpha.append(Cn_alpha)

    def get_Cn_alpha(self):
        """
        Returns the list of Rocket Cn_alpha values when called
        :return: Rocket.comp_Cn_alpha
        """
        return self._comp_Cn_alpha

    def add_length(self, comp_length):
        """
        module to add component length to overall rocket length
        :param comp_length: (float) length of rocket component
        :return: none
        """
        self._length += comp_length

    def get_length(self):
        """
        Returns the total length of Rocket
        :return: Rocket._length
        """
        return self._length


def initialize_rocket():
    """
    function to set up basic rocket definition and call the initial Rocket class
    :return: none
    """
    # get input from user to initialize rocket
    rocket_name = input("Enter the rocket name that you would like to analyze: ")
    # send information to Rocket class to initialize Rocket
    rocket = Rocket(rocket_name)
    return rocket


def find_nose(rocket):
    """
    module to find the Cn_alpha and x_bar of the nose cone
    :param rocket: (object) current class object being calculated
    :return: 0 or 1
    """
    # get shape
    len_nose = float(input("Enter the length from the forward tip of the nose cone to the top of the body tube: "))
    prompt = ("Input the shape of the rocket nose cone:",
              "     1 = Conical (straight surface, pointed tip)",
              "     2 = Ogive (curve surface, rounded tip",
              "     3 = Parabolic (curved surface, rounded tip",
              "     4 = Capsule (ex: Mercury, Gemini, Saturn")
    min_val = 1
    max_val = 4
    err_val = 1                     # initialize error code to set
    print_statement(prompt)
    ### ERROR LOOP ###
    while err_val != 0:             # validate input as single digit integer within valid range
        err_val = 0                 # clear error code - if no error, code will exit error loop
        shape_val = input("Nose Cone Shape (1 - 4): ")
        err_val = validate_input(shape_val, min_val, max_val, err_val)
    shape = ord(shape_val) - 48
    Cna_nose = 2                    # this is common to all nose cone shapes (except capsule)
    if shape == 1:
        x_bar = 2/3 * len_nose
    elif shape == 2:
        x_bar = 0.466 * len_nose
    elif shape == 3:
        x_bar = 0.5 * len_nose
    else:
        # this multiple inputs for distance and diameter in order to calculate the equivalent cone
        #       diameter at top of capsule (small diameter, x1, 0)
        #       distance to capsule shoulder
        #       length of capsule shoulder
        #       diameter at bottom of capsule (large diameter)
        #       distance to bottom of capsule
        #           calculate equivalent cone
        # calculate Cna
        # calculate x_bar
        x_bar = 0                   ################ to be updated later
    # update Rocket class with calculated values
    rocket.add_component("Nose", len_nose)
    rocket.add_Cn_alpha(Cna_nose)
    rocket.add_x_bar(x_bar)
    rocket.add_length(len_nose)

def find_body(rocket):
    """
    module to get rocket body tube length and diameter from user
    :param rocket: (object) current class object being calculated
    :return: 0 or 1
    """
    # this input would be nice to automate in the future
    body_no = input("Enter the body tube number (from nose to tail): ")
    body_num = "Body_" + body_no
    dist_to_body = rocket.get_length()
    len_body = float(input("Enter the length of the body tube (in inches): "))
    diam_body = float(input("Enter the diameter of the body tube (in inches): "))
    Cna_body = 0                    # standard input - body tube section does not contribute normal force
    x_bar = dist_to_body + (len_body / 2)
    rocket.add_diameter(diam_body)
    rocket.add_component(body_num, len_body)
    rocket.add_Cn_alpha(Cna_body)
    rocket.add_x_bar(x_bar)
    rocket.add_length(len_body)

def find_taper(rocket, taper_type):
    """
    module to get rocket shoulder/boattail length and diameter from user
    :param rocket: (object) current class object being calculated
    :return: 0 or 1
    """
    dist_to_taper = float(input("Enter the distance from the forward tip of the nose cone to the top of the taper section (in inches): "))
    len_taper = float(input("Enter the length of the taper section (in inches): "))
    diam1_taper = float(input("Enter the smaller diameter of the taper section (in inches): "))
    diam2_taper = float(input("Enter the larger diameter of the taper section (in inches): "))
    diam_nose = rocket.get_diameter()
    Cna_taper = 2 * ((diam2_taper / diam_nose)**2 - (diam1_taper / diam_nose)**2 )
    x_bar = dist_to_taper + (len_taper / 3) * (1 + (1 - diam1_taper / diam2_taper) / (1 - (diam1_taper / diam2_taper)**2))
    if taper_type == 1:
        rocket.add_component("Shoulder", len_taper)
    elif taper_type == 2:
        rocket.add_component("Boattail", len_taper)
    rocket.add_Cn_alpha(Cna_taper)
    rocket.add_x_bar(x_bar)
    rocket.add_length(len_taper)

def find_fins(rocket):
    """
    module to get distance to rocket fins, number, and dimensions from user, calculate area, Cna, and x_bar
    number of fins limited to 3, 4, or 6 fins by governing equations
    fin shape is limited to 3 or 4 points (to be revisited at a later date)
    :param rocket: (object) current class object being calculated
    :return: 0 or 1
    """
    dist_to_fins = float(input("Enter the distance from the forward tip of the nose cone to the upper tip of fins (in inches): "))
    num_fins = int(input("Enter the number of fins on your rocket (must be 3, 4, or 6): "))
    dim_a = float(input("Enter the length of the fin base (where the fin meets the body) in inches: "))
    dim_b = float(input("Enter the length of the fin along the tip in inches: "))
    dim_m = float(input("Enter the distance from the front of the fin (at the body) to the front tip in inches: "))
    dim_s = float(input("Enter the distance from the fin root to the tip in inches: "))
    # calculate chord (l) - adjacent = dim_s
    adj = dim_s
    opp = (dim_b / 2 + dim_m) - (dim_a / 2)
    chord =  math.sqrt(adj**2 + opp**2)
    # calculate Cn_alpha for fin
    diam = rocket.get_diameter()
    cna_fin_num = 4 * num_fins * (chord / diam)**2
    cna_fin_denom = 1 + math.sqrt(1 + ((2 * chord) / (dim_a + dim_b))**2)
    cna_fin = cna_fin_num / cna_fin_denom
    # calculate fin interference factor
    rad = diam / 2
    fin_factor = 1
    if num_fins == 3 or num_fins == 4:
        fin_factor = 1 + rad / (rad + chord)
    elif num_fins == 6:
        fin_factor = 1 + (0.5 * rad) / (rad + chord)
    # else:
    #    print("Error") # loop this
    Cna_fins = fin_factor * cna_fin
    # calculate x_bar_fin
    x_bar_fin_term_1 = (chord * (dim_a + 2 * dim_b)) / (3 * (dim_a + dim_b))
    x_bar_fin_term_2 = (1 / 6) * (dim_a + dim_b - ((dim_a * dim_b) / (dim_a + dim_b)))
    x_bar_fins = dist_to_fins + x_bar_fin_term_1 + x_bar_fin_term_2
    rocket.add_component("Fins", dist_to_fins)
    rocket.add_Cn_alpha(Cna_fins)
    rocket.add_x_bar(x_bar_fins)


def find_Cna(rocket):
    """
    module to control data input and calculation of component Cn_alpha
    :param rocket: (object) current class object being calculated
    :return: Cn_alpha (float), x_bar (float)
    """
    min_val = 0
    max_val = 5
    comp = 9                            # initialize component to non-valid digit
    ### INPUT LOOP ###
    while comp != 0:                    # enter the input loop for calling Cn_alpha
        err_val = 1                     # initialize error code to set
        component_call = ("Enter type of section to calculate (if none, enter 0):",
                          "     0 = Exit",
                          "     1 = Nose (1 required)",
                          "     2 = Body (At least 1 required)",
                          "     3 = Shoulder",
                          "     4 = Boattail",
                          "     5 = Fins (3, 4, or 6 required)")
        print_statement(component_call)
        ### ERROR LOOP ###
        while err_val != 0:             # validate input as single digit integer within valid range
            err_val = 0                 # clear error code - if no error, code will exit error loop
            component = input("Component Type (1 - 5): ")
            err_val = validate_input(component, min_val, max_val, err_val)
        comp = ord(component) - 48
        ######### THIS IS WHERE THE MODULE CALLS LIVE ###########
        if comp == 1:
            find_nose(rocket)
        elif comp == 2:
            find_body(rocket)
        elif comp == 3:
            find_taper(rocket, 1)
        elif comp == 4:
            find_taper(rocket, 2)
        elif comp == 5:
            find_fins(rocket)
    return 0

def validate_input(value, min_val, max_val, err_code):
    """
    Takes an unknown input and verifies that it is a single-digit integer within a given range
    Returns an error code: 0 for valid input; 1 for invalid input
    :param value: (int/float/string)
    :param err_code: (int)
    :param min_val: (int)
    :param max_val: (int)
    :return: err_code
    """
    if len(value) != 1:                 # check for single-digit input
        err_code = 1                    # set the error code
        print("Error: incorrect input type.  Please enter a valid number between  0 and 5.")
    # check for valid integer input
    elif ord(value) < (min_val + 48) or ord(value) > (max_val + 48):
        err_code = 1                     # set error code
        print("Error: incorrect input range.  Please enter a valid number between  0 and 5.")
    return err_code

def print_statement(statement):
    """
    module to print multi-line output stored in an array to the user screen
    :param statement: string array
    :return: none
    """
    for line in statement:
        print(line)

def main():
    """
    Primary function to introduce program, collect user input, and call modules for calculation
    """
    cna_description = ("Normal force on each region represented by Cn_alpha.",
                       "Center of pressure on each region represented by x_bar.",
                       "Total force acting on rocket (Cn_alpha_rocket) is sum of forces acting on nose, shoulders,",
                       "boattails, and fins in body effect.",
                       "Center of pressure for entire rocket (x_bar_rocket) is the sum of the moments acting on each",
                       "component of the rocket (Cn_alpha_nose * x_bar_nose + ... + Cn_alpha_fins_in_body_effect * x_bar_fins)",
                       "divided by Cn_alpha_rocket.\n",
                       "Required: rocket must have nose, one body section, and fins.")
    greeting = ("Welcome to the Model Rocket Cp Calculator.\n",)
    description = ("This programs takes inputs of model rocket geometry as measured from the tip of the nose cone",
                   "and calculates the aerodynamic center of pressure. The Cp Margin is defined as (Cp - Cg).",
                   "This value should be greater than or equal to the diameter of the main rocket body tube (in inches)\n")
    assumptions =  ("Basic Program Assumptions: ",
                    "       relative angle less than 10 degrees",
                    "       velocity less 600 feet/sec (much less than speed of sound)",
                    "       airflow is smooth with no rapid change",
                    "       rocket thin compared to length (t/l </= ???)",
                    "       nose comes smoothly to a point",
                    "       rocket is an axially symmetric rigid body",
                    "       fins are thin, flat plates\n")
    print_statement(greeting)
    print_statement(description)
    print_statement(assumptions)
    rocket_1 = initialize_rocket()
    print_statement(cna_description)
    print(rocket_1.get_name())
    find_Cna(rocket_1)
    print(rocket_1.get_name())
    print(rocket_1.get_length())
    print(rocket_1.get_components())
    print(rocket_1.get_Cn_alpha())
    print(rocket_1.get_x_bar())


if __name__ == "__main__":
    main()