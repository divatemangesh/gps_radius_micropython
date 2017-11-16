'''
This is python function library for  GPS LOCK
for micropython framework.
Author:- Mangesh Divate
dependancies:- pyb,math,time
email:- divatemangesh12@gmail.com
'''
#set the unlock  GPS location and tolerance area (radius)
center_x =#
center_y =#
radius
#---------------------------------------------------------------
#center_x,center_y is location where PRODUCT will be unlocked
#radius is area of tolerance
#x,y is current location
def in_circle_sqrt_meth(center_x, center_y, radius, x, y):
    dist = math.sqrt((center_x - x) ** 2 + (center_y - y) ** 2)
    return dist <= radius


def in_circle_sqr_meth(center_x, center_y, radius, x, y):
    square_dist = (center_x - x) ** 2 + (center_y - y) ** 2
    return square_dist <= radius ** 2

#we can use both function but squring takes less  clock cycles than squreroot
#-----------------------------------------------------------------
def gps_cord():
    #intitilise serial communication and get cordinates from gps reciver and
    #store cordinates in "cord" veriables(Comma seprated value)
    #split cordinates and save latitude and longitude in seprate variable
    #i.e.'c_lat' and 'c-lang'
    #return 3 variable (c_cord,c_lat,c_long)
    return c_cord,c_lat,c_long,E/W,N/S
#------------------------------------------------------------------
def cord compare():
     cir_result = in_circle_sqr_meth(center_x, center_y, radius, x, y):

    if cir_result == True:
        print("GPS lock allowing it to be unlocked")
