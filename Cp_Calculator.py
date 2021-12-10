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
# General input: name of rocket, date, number stages, number of body sections, number of shoulders, number of
# boattails, number of fins (repeat for each stage)
# Create object of Rocket class
# Define two lists: one to collect Cn_alpha_component; one to collect x_bar_component
#
# Call module to calculate nose cone Cp - required
#   Pass object to module
#       Nose module requests input for nose length, diameter, and shape
#           1 = Conical
#           2 = Ogive (curved surface, pointed tip)
#           3 = Parabolic (curved surface, rounded tip)
#           4 = Capsule (Mercury, Gemini, Saturn)
#       Enter values to object
#       Cn_nose = 2
#       Look up x_bar_nose based on shape
#           Capsule is a special case which requires additional input and calculation
#   Return Cn_alpha_nose, x_bar_nose
# Enter Cn_nose and x_bar_nose values to lists
# Enter type of section to calculate (if none, enter 0)
#   0 = exit
#   1 = body
#   2 = shoulder
#   3 = boattail
#   4 = fins
# While type != 0
#   Case 1:
#       Call body module
#           Pass object to module
#               Body module requests input for body segment length, diameter, and distance from ref
#               Enter values to object
#               Check sum to verify distance from ref = distance + length of previous
#               Check sum to verify diameter of previous object = body diameter
#           Return 0
#   Case 2 or Case 3:
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
#   Case 4:
#       Call fin module
#           Pass object to module
#               Fin module requests inputs for # fins (3, 4, or 6 only)

class Rocket():
    """
    object to define Rocket and its parameters, retrieve data, etc
    """
    def __init__(self, name):
        """
        adf
        :param name:
        """
        self._name = name

def print_statement(statement):
    """
    module to print multi-line output stored in an array to the user screen
    :param statement: string array
    :return: none
    """
    for lines in statement:
        print(lines)


def main():
    """
    Primary function to introduce program, collect user input, and call modules for calculation
    """
    greeting = ("Welcome to the Model Rocket Cp Calculator.\n")
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
                    "       fins are thin, flat plates")
    print(greeting)
    print_statement(description)
    print_statement(assumptions)
    Rocket("Test_Mission")

if __name__ == "__main__":
    main()