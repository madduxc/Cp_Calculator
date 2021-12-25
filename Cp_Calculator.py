# Authors       : Charles D. Maddux
#               :
#               :
# Date          : August 29, 2021
# Description   : Program to take input of model rocket geometry and output Center of Pressure as
#                 measured from the tip of the nose cone.  See Notes.txt for full description
#               References:
#               1.  TR-33. "Model Rocket Technical Report: Calculating the Center of Pressure of a Model
#                   Rocket."  James Barrowman.  EstesEducator.com

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
        self._Cna = 0                       # calculated Cn_alpha for complete rocket
        self._xBar = 0                      # [in] calculated x_Bar for complete rocket
        self._Cg_Heavy = 0                  # [in] user input for center of gravity location with largest engine used
        self._Cp_Margin = -1                # xBar - Cg_Heavy

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
        Returns the Rocket nose diameter property when called
        :return: Rocket._diameter[0]
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

    def set_Cna(self, cna_rocket):
        """
        Enters calculated Cn_alpha for complete rocket to Rocket class
        :param cna_rocket: (float)
        :return: none
        """
        self._Cna = cna_rocket

    def get_Cna(self):
        """
        Returns calculated Cn_alpha for complete rocket from Rocket class
        :return: Cna
        """
        return self._Cna

    def set_xBar(self, xBar):
        """
        Enters calculated xBar for complete rocket to Rocket class
        :param xBar: (float)
        :return: none
        """
        self._xBar = xBar

    def get_xBar(self):
        """
        Returns calculated xBar for complete rocket from Rocket class
        :return: xBar
        """
        return self._xBar

    def set_CgMax(self, Cg_max):
        """
        Enters user input Cg for complete rocket at maximum engine weight to Rocket class
        :param Cg_max: (float)
        :return: none
        """
        self._Cg_Heavy = Cg_max

    def get_CgMax(self):
        """
        Returns Cg for complete rocket at maximum engine weight from Rocket class
        :return: _Cg_Heavy
        """
        return self._Cg_Heavy

    def set_Margin(self, margin):
        """
        Enters calculated Margin of Safety between Center of Pressure and Center of Gravity at it heaviest engine load
        :param margin: (float)
        :return: none
        """
        self._Cp_Margin = margin

    def get_Margin(self):
        """
        Returns calculated Cp Margin from Rocket class
        :return: _Cp_Margin
        """
        return self._Cp_Margin

###########################################  END Rocket CLass  #####################################################

#######################################  Begin Standalone Modules  #################################################

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
    Module to find the Cn_alpha and x_bar of the nose cone
    :param rocket: (object) current class object being calculated
    :return: 0 (no errors) or 1 (errors)
    """
    # get shape
    len_nose = float(input("Enter the length from the forward tip of the nose cone to the top of the body tube: "))
    prompt = ("Input the shape of the rocket nose cone:",
              "     1 = Conical (straight surface, pointed tip)",
              "     2 = Ogive (curve surface, rounded tip",
              "     3 = Parabolic (curved surface, rounded tip",
              "     4 = Capsule (ex: Mercury, Gemini, Saturn")
    min_val = 1                             # set lower limit for input validation
    max_val = 4                             # set upper limit for input validation
    err_val = 1                             # initialize error code to set
    print_statement(prompt)
    ### ERROR LOOP ###
    while err_val != 0:                     # validate input as single digit integer within valid range
        err_val = 0                         # clear error code - if no error, code will exit error loop
        shape_val = input("Nose Cone Shape (1 - 4): ")
        err_val = validate_input(shape_val, min_val, max_val, err_val)
    shape = ord(shape_val) - 48             # convert to integer value
    Cna_nose = 2                            # this is common to all nose cone shapes per Ref. 1, Sect 4
    if shape == 1:
        x_bar = 2/3 * len_nose              # for conical nose per Ref 1, Sect 4
    elif shape == 2:
        x_bar = 0.466 * len_nose            # for ogive nose per Ref 1, Sect 4
    elif shape == 3:
        x_bar = 0.5 * len_nose              # for parabolic nose per Ref 1, Sect 4
    else:
        x_bar = calculate_capsule(len_nose)
    # update Rocket class with calculated values
    rocket.add_component("Nose", len_nose)
    rocket.add_Cn_alpha(Cna_nose)
    rocket.add_x_bar(x_bar)
    rocket.add_length(len_nose)
    return 0

def calculate_capsule(length):
    """
    Module to calculate Cna and xBar of Capsule-shaped nose piece
    :param length: (float)
    :return: Cna_nose, xBar_nose
    """
    capsule_err = 1  # set error flag
    while capsule_err != 0:
        capsule_err = 0  # clear error flag
        diam_1_capsule = float(input("Enter the diameter of the base of the capsule in inches (body tube diameter): "))
        diam_2_capsule = float(
            input("Enter the diameter at the top of the capsule in inches (not including escape tower): "))
        if diam_1_capsule <= diam_2_capsule:
            capsule_err = 1  # set error flag
            print("Error: Diameter at base of capsule must be larger than diameter at top of capsule.")
    # perform slope-intercept calculation with axis origin at top/center of capsule body
    x_1 = length  # equations per Ref 1, Sect 4 for capsule nose
    x_2 = 0  # top of module based at origin
    y_1 = diam_1_capsule / 2  # y1 = radius of module at body tube
    y_2 = diam_2_capsule / 2  # y2 = radius of module at top of capsule
    slope_m = (y_2 - y_1) / (x_2 - x_1)
    b_1 = y_1 - slope_m * x_1  # check sum 1
    b_2 = y_2 - slope_m * x_2  # check sum 2
    # verify values calculated correctly at each point
    if b_1 != b_2:
        print("Error in Capsule inputs.")
        return 1
    delta_l = b_1 / slope_m  # length = absolute value of x intercept
    len_equiv_capsule = length + delta_l  # x_bar calculated based on length of equivalent cone length
    x_bar_equiv = 2 / 3 * len_equiv_capsule  # x_bar of this equivalent conical nose
    x_bar = x_bar_equiv - delta_l  # subtract equivalent length
    return x_bar


def find_body(rocket):
    """
    module to get rocket body tube length and diameter from user
    :param rocket: (object) current class object being calculated
    :return: 0 or 1
    """
    # this input would be nice to automate in the future
    body_no = input("Enter the body tube number (from nose to tail): ")
    body_num = "Body_" + body_no            # create unique key for dictionary entry in case multiple body tubes are present
    len_body = float(input("Enter the length of the body tube (in inches): "))
    diam_body = float(input("Enter the diameter of the body tube (in inches): "))
    # Cna_body = 0                          # standard input - body tube section does not contribute normal force per Ref 1, Sect 4
    # update components, body diameter, and rocket length
    rocket.add_diameter(diam_body)
    rocket.add_component(body_num, len_body)
    rocket.add_length(len_body)
    body_err = 1                            # initialize error flag
    while body_err != 0:
        body_err = 0                        # clear error code - if no error, code will exit error loop
        fins = input("Does this body tube have fins attached? (1 = yes; 2 = no): ")
        body_err = validate_input(fins, 1, 2, body_err)
    fins = ord(fins) - 48  # convert to integer value
    if fins == 1:
        find_fins(rocket, diam_body, body_no)
    return 0

def find_taper(rocket, taper_type):
    """
    module to get rocket shoulder/boattail length and diameter from user
    :param rocket: (object) current class object being calculated
    :return: 0 or 1
    """
    dist_to_taper = rocket.get_length()
    len_taper = float(input("Enter the length of the taper section in inches: "))
    small_diam_taper = float(input("Enter the smaller diameter of the taper section in inches: "))
    large_diam_taper = float(input("Enter the larger diameter of the taper section in inches: "))
    # determine shoulder or boattail, set correct diameter definition, and update component
    if taper_type == 1:
        diam1_taper = small_diam_taper      # small dia to the top
        diam2_taper = large_diam_taper      # large dia to the bottom
        rocket.add_component("Shoulder", len_taper)
    elif taper_type == 2:
        diam1_taper = large_diam_taper      # large dia to the top
        diam2_taper = small_diam_taper      # small dia to the bottom
        rocket.add_component("Boattail", len_taper)
    # calculate Cna and xBar
    diam_nose = rocket.get_diameter()       # diameter of first body tube defined
    Cna_taper = 2 * ((diam2_taper / diam_nose)**2 - (diam1_taper / diam_nose)**2 )
    x_bar = dist_to_taper + (len_taper / 3) * (1 + (1 - diam1_taper / diam2_taper) / (1 - (diam1_taper / diam2_taper)**2))
    # update Cna, x_bar, and rocket length
    rocket.add_Cn_alpha(Cna_taper)
    rocket.add_x_bar(x_bar)
    rocket.add_length(len_taper)
    return 0

def find_fins(rocket, diam=0, fin_num=1):
    """
    module to get distance to rocket fins, number, and dimensions from user, calculate area, Cna, and x_bar
    number of fins limited to 3, 4, or 6 fins by governing equations
    fin shape is limited to 3 or 4 points (to be revisited at a later date)
    :param rocket: (object) current class object being calculated
    :return: 0 or 1
    """
    # add basic assumptions - 3 or 4 point fin, tip parallel to root
    dist_to_fins = float(input("Enter the distance from the forward tip of the nose cone to the upper tip of fins (in inches): "))
    #                                        # this value is different than rocket length
    num_fins = int(input("Enter the number of fins on your rocket (must be 3, 4, or 6): "))
    #                                       # should add validation
    dim_a = float(input("a: Enter the length of the fin root (where the fin meets the body) in inches: "))
    # add validation here that dist_to_fins + dim_a <= length of rocket
    dim_b = float(input("b: Enter the length of the fin along the tip in inches: "))
    dim_m = float(input("m: Enter the distance from the front of the fin root to the front of the tip in inches: "))
    dim_s = float(input("s: Enter the length from the fin root to the tip in inches: "))
    # calculate chord (l) - adjacent = dim_s
    adj = dim_s                             # adjacent edge of triangle
    opp = (dim_b / 2 + dim_m) - (dim_a / 2) # opposite edge of triangle based at intersection of chord and fin root
    chord =  math.sqrt(adj**2 + opp**2)     # calculate long leg of right triangle
    # calculate Cn_alpha for fin
    if diam == 0:
        diam = rocket.get_diameter()
    # calculate Cna of fins per Ref 1, Section 4
    cna_fin_num = 4 * num_fins * (dim_s / diam)**2                              # numerator of Cna equation
    cna_fin_denom = 1 + math.sqrt(1 + ((2 * chord) / (dim_a + dim_b))**2)       # denominator of Cna equation
    cna_fin = cna_fin_num / cna_fin_denom
    # calculate fin interference factor per Ref 1, Sect 4
    rad = diam / 2
    fin_factor = 1                          # initialize var outside of loop
    if num_fins == 3 or num_fins == 4:
        fin_factor = 1 + rad / (rad + dim_s)
    elif num_fins == 6:
        fin_factor = 1 + (0.5 * rad) / (rad + dim_s)
    else:
        print("Error entering the number of fins.")
        return 1
    Cna_fins = fin_factor * cna_fin
    # calculate x_bar_fin per Ref 1, Sect 4
    x_bar_fin_term_1 = (dim_m * (dim_a + 2 * dim_b)) / (3 * (dim_a + dim_b))
    x_bar_fin_term_2 = (1 / 6) * (dim_a + dim_b - ((dim_a * dim_b) / (dim_a + dim_b)))
    x_bar_fins = dist_to_fins + x_bar_fin_term_1 + x_bar_fin_term_2
    # add component, Cna, and x_bar to Rocket
    fin_id = "Fins_" + fin_num
    rocket.add_component(fin_id, dist_to_fins)
    rocket.add_Cn_alpha(Cna_fins)
    rocket.add_x_bar(x_bar_fins)
    return 0

def find_xbar(rocket):
    """
    Calculates Cn_alpha and xBar for complete rocket and enters values to Rocket class
    :param rocket: (object)
    :return:
    """
    cna_list = rocket.get_Cn_alpha()        # retrieve list of values for component Cn_alphas
    x_bar_list = rocket.get_x_bar()         # retrieve list of values for component x_bars
    num_comp = len(x_bar_list)              # find number of components
    cna_total = 0                           # initialize vars outside of loop
    x_bar_total = 0
    # calculate values for numerator (Cn_alpha) and denominator of xBar
    for elem in range(0, num_comp):
        cna_total += cna_list[elem]         # calculate Cn_alpha for complete rocket
        x_bar_total += cna_list[elem] * x_bar_list[elem]
    x_bar = x_bar_total / cna_total         # calculate xBar for complete rocket
    rocket.set_Cna(cna_total)
    rocket.set_xBar(x_bar)
    return 0

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
        component_call = ("Components must be entered in order from the nose to the tail one at a time.  If two sets of",
                          "fins are attached to a single body tube, enter it as two separate tubes with a fin set attached",
                          "to each.\n",
                          "Enter type of section to calculate (if none, enter 0):",
                          "     0 = Exit",
                          "     1 = Nose (1 required)",
                          "     2 = Body (At least 1 required)",
                          "     3 = Shoulder",
                          "     4 = Boattail",
                          "     5 = Fins (3, 4, or 6 required)")
        cg_call = ("Enter the distance from the tip of the nose to the Cg location in inches of the rocket configured ",
                   "with the largest motor expected, or enter '0' to skip Cp Margin calculation.")


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
    find_xbar(rocket)                       # call function to calculate Cna and x_bar for entire rocket
    # section to calculate Cp Margin - probably move to separate function
    print_statement(cg_call)                # get input from user
    cg_val = float(input("Cg Value (or 0):"))
    if cg_val != 0:
        xBar = rocket.get_xBar()            # retrieve xBar from class object
        Cp_margin = xBar - cg_val           # calculate cp margin. Should also check against body diameter
        rocket.set_CgMax(cg_val)
        rocket.set_Margin(Cp_margin)
    return 0

def print_results(rocket):
    """
    Output results of Cp Calculations to screen for a given Rocket class object
    :param rocket: (object)
    :return: none
    """
    comps = rocket.get_components()
    print("\n\nxBar and Cn_alpha Results for", rocket.get_name())
    print("Values calculated for:")
    for elem in comps:
        print(elem)
    print("Overall Rocket Length:", rocket.get_length(), " in.")
    print("Cn_alpha:", round(rocket.get_Cna(), 3))
    print("x_bar:", round(rocket.get_xBar(), 2))
    cg = rocket.get_CgMax()
    if cg != 0:
        cp_margin = rocket.get_Margin()
        diam = rocket.get_diameter()        # this is the nose diameter.  Needs to be updated to largest diameter
        print("Cp Margin: ", round(cp_margin,2))
        if cp_margin > 0 and cp_margin <= diam:
            print("This margin is idea for safety of flight.")
        elif cp_margin > 0:
            print("This margin is acceptable, but may not be ideal for safety of flight.")
        else:
            print("This margin is not acceptable for safety of flight.")

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
    # To Do:    develop unittests that simulate input for each module (in process - nose complete)
    #           develop full test cases that include each combination (if possible) and compare to hand calcs
    #           add data validation for the remaining inputs
    #           integrate with GUI
    #           add option to save information to a file

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
    print_results(rocket_1)
    # print("Rocket Name: ", rocket_1.get_name())
    # print("Rocket Length: ", rocket_1.get_length(), " in.")
    # print(rocket_1.get_components())
    # print("Cn_alpha: ", rocket_1.get_Cn_alpha())
    # print("x_bar: ", rocket_1.get_x_bar())
    # print(round(total_x, 2))


if __name__ == "__main__":
    main()