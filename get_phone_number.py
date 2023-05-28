'''A Module For Grabbing Information On Phone Numbers (THIS INCLUDE MODULES: phonenumbers; opencage; folium)'''

import phonenumbers
import opencage
import folium

from phonenumbers import geocoder as gc




def Origin_Of_Phone_Num(FoneNumber= int):
    """Print Out The Name Of Origin Of The Phone Number"""
    
    the_phone_num = phonenumbers.parse(FoneNumber)
    location = gc.description_for_number(the_phone_num, 'en')
    print(location)



def Service_Provider_Of_Num(FoneNumber= int):
    '''Print Out The Service Provider Of The Phone Number'''
    
    from phonenumbers import carrier
    service_pro = phonenumbers.parse(FoneNumber)
    print(carrier.name_for_number(service_pro, 'en'))



def Get_Location_Of_Phone_Number(FoneNumber= int):
    '''Get The Location Of The Phone Number. 
    !!! YOU CAN GET IT YOUR SELF A API KEY BY MAKING AN OPENCAGE ACCOUNT FOR FREE ONLINE!!!'''

    the_phonenum = phonenumbers.parse(FoneNumber)
    location = gc.description_for_number(the_phonenum, 'en')

    #print out the location of the phone number
    from opencage.geocoder import OpenCageGeocode
    key = 'GET A OPENCAGE KEY'
    #use you opencage account to to copy your api key code into this variable
    geocoder = OpenCageGeocode(key)
    query = str(location)
    results = geocoder.geocode(query)
    print(results)

    #get the longnitude and latitude
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(lat, lng)

    #save the map location
    myMapp = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMapp)

    myMapp.save('Printed_Location.html')
    
    



