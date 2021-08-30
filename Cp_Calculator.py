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
# Normal force on each region represented by Cn_alpha
# Normal force acting on the body is neglegible for small alpha (<30 degrees).
# Body geometry is required for fin Cp calcs and drawing pictures
# Center of pressure on each region represented by x_bar
#
# Total force acting on rocket (Cp_alpha_rocket) is sum of forces acting on nose, shoulders, boattails,
#  and fins in body effect
# Rocket must have nose, one body section, and fins - others can be set to zero if not present
#
# Center of pressure for entire rocket (x_bar_rocket) is the sum of the moments acting on each
# component of the rocket (Cp_alpha_nose * x_bar_nose + ... + Cp_alpha_fins_in_body_effect * x_bar_fins)
# divided by Cp_alpha_rocket

# Basic structure
# General input: name of rocket, date, number stages, number of body sections, number of shoulders, number of
# boattails, number of fins (repeat for each stage)
# Create object of Rocket class
# Define two lists: one to collect Cp_alpha_component; one to collect x_bar_component
#
# Call module to calculate nose cone Cp - required
#   Pass object to module
#       Nose module requests input for nose length, diameter, and shape
#       Enter values to object
#   Return Cp_alpha_nose, x_bar_nose
# Enter Cp_nose and x_bar_nose values to lists
# Enter type of section to calculate (if none, enter 0)
# While type != 0