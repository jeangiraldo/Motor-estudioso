# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:28:11 2020

@author: CEC
"""

print("=============================================")
for each in json_data["route"]["legs"][0]["maneuvers"]:
    print((each["narrative"]) + " (" + str("(:.2f)".format((each["distance"])*1.61) + " km)"))
print("=============================================\n")
 elif json_status == 402:
        print("\n****************************************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("****************************************************************\n")
    else:
        print("\n************************************************************************")
        print("Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")