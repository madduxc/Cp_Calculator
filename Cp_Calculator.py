# Authors       : Charles D. Maddux
#               :
#               :
# Date          : August 29, 2021
# Description   : Program to take input of model rocket geometry and output Center of Pressure as
#                 measured from the tip of the nose cone.
# Notes from readings.
# Assumptions:  relative angle less than 10 degrees
#               velocity less 600 feet/sec (much less than speed of sound)
#               airflow is smooth with no rapid change
#               rocket thin compared to length (t/l </= ???)
#               nose comes smoothly to a point
#               rocket is an axially symmetric rigid body
#               fins are thin, flat plates
#
# Cp margin should be at least equal to the diameter of the largest body tube (inches)
# Cp margin defined?  (Cp - Cg) ?
# Normal force on each region represented by Cn_alpha
# Normal force acting on the body is negligible for small alpha (<30 degrees).
# Body geometry is required for fin Cp calcs and drawing pictures
# Center of pressure on each region represented by x_bar
#
# Total force acting on rocket (Cn_alpha_rocket) is sum of forces acting on nose, shoulders, boattails,
#  and fins in body effect
# Required: rocket must have nose, one body section, and fins - others can be set to zero if not present
#
# Center of pressure for entire rocket (x_bar_rocket) is the sum of the moments acting on each
# component of the rocket (Cn_alpha_nose * x_bar_nose + ... + Cn_alpha_fins_in_body_effect * x_bar_fins)
# divided by Cn_alpha_rocket

# Basic structure
# Print statement - purpose of the code, limitations, definitions
# General input: name of rocket, date, [number of stages], number of body sections, number of shoulders, number of
# boattails, number of fins (repeat for each stage)
# Create object of Rocket class
# Define two lists: one to collect Cn_alpha_component; one to collect x_bar_component
#
# Enter type of section to calculate (if none, enter 0)
#   0 = exit
#   1 = nose (required)
#   2 = body (required)
#   3 = shoulder
#   4 = boattail
#   5 = fins (required)
# While type != 0
#   Case 1:
#       Call nose module
#           Pass object to module
#               nose module requests input for nose length, diameter, and shape
#                   1 = Conical
#                   2 = Ogive (curved surface, pointed tip)
#                   3 = Parabolic (curved surface, rounded tip)
#                   4 = Capsule (Mercury, Gemini, Saturn)
#               enter values to object
#               Cn_nose = 2
#               look up x_bar_nose based on shape
#               capsule is a special case which requires additional input and calculation
#           Return Cn_alpha_nose, x_bar_nose
# Enter Cn_nose and x_bar_nose values to lists
#   Case 2:
#       Call body module
#           Pass object to module
#               Body module requests input for body segment length, diameter, and distance from ref
#               Enter values to object
#               Check sum to verify distance from ref = distance + length of previous
#               Check sum to verify diameter of previous object = body diameter
#           Return 0
#   Case 3 or Case 4:
#       Call shoulder/boattail module
#           Pass object to module
#               Shoulder/boattail module requests inputs for length, d1, d2, and dist from ref
#               Enter values to object
#               Look up nose diameter
#               Calculate Cn_s/b = 2 * ( (d2 / d_nose)^2 - (d1 / d_nose)^2)
#               Calculate x_bar_s/b = x_s/b + L/3 * (1 + (1 - d1/d2) / (1 - (d1/d2)^2))
#               Check sum to verify distance from ref = distance + length of previous
#               Check sum to verify diameter of previous object = d1
#           Return Cn_s/b, x_bar_s/b
#   Case 5:
#       Call fin module
#           Pass object to module
#               Fin module requests inputs for # fins (3, 4, or 6 only)

class Rocket():
    """
    object to define Rocket and its parameters, retrieve data, etc
    """
    def __init__(self, name, diameter, num_fins):
        """
        defines Rocket objects, retrieves private members and stores calculated values
        :param name:        (string) name of rocket
        :param diameter:    (float) diameter of the upper rocket body tube
        :param num_fins:    (int) number of fins attached to the lower body tube
        """
        self._name = name                   # string name of rocket
        self._diameter = diameter           # [in] diameter or rocket
        self._num_fins = num_fins           # [] number of fins
        self._components = []               # array of components analyzed
        self._x_bar = []                    # [in] array of x_bar values corresponding to components
        self._comp_Cn_alpha = []            # [] array of Cn_alpha values corresponding to components

    def get_name(self):
        """
        Returns the Rocket name property when called
        :return: Rocket._name
        """
        return self._name

    def get_diameter(self):
        """
        Returns the Rocket diameter property when called
        :return: Rocket._diameter
        """
        return self._diameter

    def get_num_fins(self):
        """
        Returns the Rocket number of fins property when called
        :return: Rocket._num_fins
        """
        return self._num_fins

    def add_component(self, comp):
        """
        Module to add a component to the Rocket component array
        :param comp: (string) name of component
        :return: none
        """
        self._components.append(comp)

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

def initialize_rocket():
    """
    function to set up basic rocket definition and call the initial Rocket class
    :return: none
    """
    # get input from user to initialize rocket
    rocket_name = input("Enter the rocket name that you would like to analyze: ")
    diam_input = input("Enter the diameter of the uppermost body tube (in inches): ")
    num_fins = input("Enter the number of fins on your rocket: ")
    # send information to Rocket class to initialize Rocket
    rocket = Rocket(rocket_name, diam_input, num_fins)
    return rocket

def find_nose(rocket):
    """
    module to find the Cn_alpha and x_bar of the nose cone
    :param rocket: (object) current class object being calculated
    :return: 0 or 1
    """


def find_Cna(rocket):
    """
    module to control data input and calculation of component Cn_alpha
    :param rocket: (object) current class object being calculated
    :return: Cn_alpha (float), x_bar (float)
    """
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
            if len(component) != 1:     # check for single-digit input
                err_val = 1             # set the error code
                print("Error: incorrect input type.  Please enter a valid number between  0 and 5.")
            # check for valid integer input
            elif ord(component) < 48 or ord(component) > 53:
                err_val = 1
                print("Error: incorrect input type.  Please enter a valid number between  0 and 5.")
        comp = ord(component) - 48
        ######### THIS IS WHERE THE MODULE CALLS LIVE ###########
        print(comp)
    # need to add validation that nose, body and fins have been entered
    return 0


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

if __name__ == "__main__":
    main()