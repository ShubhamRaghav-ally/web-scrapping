import json
import csv

data_list = [[{'Id': '288', 'Name': 'Amana Toyota', 'Address1': 'NH 212,', 'Address2': 'PO: Muttil North,', 'Address3': 'Variyad,', 'Address4': 'Kalpetta,', 'CityId': '254', 'City': '', 'Pincode': '673122', 'Phone': '+91 98957 61121;+91 81292 78484', 'ServiceCenterNo': '+91 49566 00888;+91 79022 80000', 'TKMZoneId': '0', 'URL': 'http://www.amanatoyota.com', 'ServiceEmergNo': '+91 81118 88208', 'FacilityId': '3', 'Facility': '', 'Area': 'Kalpetta', 'Latitude': '11.64910000', 'Longitude': '76.12960000', 'IsUtrustAvailability': 'true', 'IsSatelliteDealer': 'false', 'HubDealerId': '', 'IsDeactivateDealer': 'false', 'IsTestDriveAlertEnabled': 'false', 'IsBuyNowAlertEnabled': 'false', 'IsBrochureAlertEnabled': 'false', 'IsGrievanceAlertEnabled': 'false', 'IsInsuranceAlertEnabled': 'false', 'IsFinanceAlertEnabled': 'false', 'IsBecomeDealerAlertEnabled': 'false', 'IsTFSINOutlet': 'false', 'IsTFSINAlertEnabled': 'false', 'IsEM60': 'true', 'Kms': '0'}],
[{'Id': '225', 'Name': 'Globe Toyota', 'Address1': 'Globe Automobiles Pvt. Ltd.,', 'Address2': 'NH 73 (New NH 7),', 'Address3': 'Village Mauja Kail,', 'Address4': 'Tehsil Jagadhari,', 'CityId': '209', 'City': '', 'Pincode': '135003', 'Phone': '1800 200 3150;+91 83980 00311', 'ServiceCenterNo': '+91 83980 00388', 'TKMZoneId': '0', 'URL': 'http://www.globetoyota.com', 'ServiceEmergNo': '+91 83980 00355', 'FacilityId': '3', 'Facility': '', 'Area': 'Tehsil Jagadhari', 'Latitude': '30.19040000', 'Longitude': '77.24380000', 'IsUtrustAvailability': 'true', 'IsSatelliteDealer': 'false', 'HubDealerId': '', 'IsDeactivateDealer': 'false', 'IsTestDriveAlertEnabled': 'false', 'IsBuyNowAlertEnabled': 'false', 'IsBrochureAlertEnabled': 'false', 'IsGrievanceAlertEnabled': 'false', 'IsInsuranceAlertEnabled': 'false', 'IsFinanceAlertEnabled': 'false', 'IsBecomeDealerAlertEnabled': 'false', 'IsTFSINOutlet': 'false', 'IsTFSINAlertEnabled': 'false', 'IsEM60': 'true', 'Kms': '0'}]]
for data in data_list:
    for d in data:
        d["Phone"] = d["Phone"].replace(";", ",")
        d["ServiceCenterNo"] = d["ServiceCenterNo"].replace(";", ",")

print("inner====>",data_list)

data_list = json.dumps(data_list)
filename = 'data.csv'
print(data_list)

with open('truee.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row using the keys from the first dictionary in the list
    header = list(data[0].keys())
    writer.writerow(header)

    # Write the data rows
    for d in data:
        # Loop through the values for each key and store them in an array or list
        for key in d.keys():
            if d[key] is not None and ';' in d[key]:

                if ';' in d[key]:
                    d[key] = d[key].split(';')
        row = list(d.values())
        writer.writerow(row)
    
