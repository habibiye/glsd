# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
import requests
from django.shortcuts import HttpResponse
# Create your views here.
#@login_required
# def spectrum(request):
#     # AVAIL_SPECTURUM_REQUEST
#     #height = str(request.GET['h'])
#     #latitude = str(request.GET['lat'])
#     #longitude = str(request.GET['long'])
#     #serial = str(request.GET['ser'])
#     #model = str(request.GET['mod'])
#     #regulator = str(request.GET['reg'])
#     height = str(60.0)
#     latitude = str(14.68694444)
#     longitude = str(8.88277778)
#     serial = '250xbcadefg1'
#     model = '5928a'
#     regulator = 'FCC110'
#     message = {"jsonrpc":"2.0",
#         "method":"csirce.getSpectrum",
#         "id":"8bb1-eace-a4d9-5bc2",
#         "params":{
#             "apiVersion":"1.2",
#             "type":"AVAIL_SPECTRUM_REQ",
#             "uniqueID":{
#                 "databaseID":"CSIR",
#                 "apiKey":"9bf05b92-5442-491b-a52a-a1f1b719b4bb",
#             },
#             "antenna":{
#                 "heightType":"AGL",
#                 "height":height,
#             },
#             "location":{
#                 "point":{
#                     "center":{
#                         "latitude":latitude,
#                         "longitude":longitude,
#                     }
#                 }
#             },
#             "deviceDesc":{
#                 "serialNumber":serial,
#                 "modelid":model,
#                 "regulatorid":regulator,
#             },
#         }
#     }
#     url = 'https://glsdceapis.meraka.csir.co.za:8443/CSIRCE'
#     response = requests.post(url, data=json.dumps(message)).json()
#     print(response)
#     try:
#         specs = response['spectrumSpecs']['spectrumSchedules']['spectra']['profiles']
#     except KeyError:
#         return HttpResponse('<p>'+str(datetime.now())+":"+repr(response)+'</p>')
#     return render(request, 'paws/spec.html', {'results':specs})
# def chan(request):
#     height = str(request.GET['h'])
#     latitude = str(request.GET['lat'])
#     longitude = str(request.GET['long'])
#     message = {
#         "method":"csire.getwebChannels",
#         "id":"req-id-01",
#         "params":{
#             "apiVersion":"1.2",
#             "type":"AVAIL_CHAN_REQ",
#             "uniqueID":{
#                 "databaseID":"CSIR",
#                 "apiKey":"",
#             },
#             "location":{
#                 "point":{
#                     "center":{
#                         "latitude":latitude,
#                         "longitude":longitude,
#                     }
#                 }
#             },
#             "antennaHeight_AGL":height,
#             "propagationModel": "ITU-R P.1546 B",
#             "wsdPower": "4 W",

#             },
#             "jsonrpc":"2.0",
#     }
#     response = requests.get('https://glsdceapis.meraka.csir.co.za:8443/CSIRCE')
#     specs = response['result']['channels']
#     return render(request, 'paws/spec.html', {'result':specs})
# def intermediate(request):
#     print(request.GET)
#     height = str(request.GET['h'])
#     latitude = str(request.GET['lat'])
#     longitude = str(request.GET['long'])
#     message = {
#         "method":"csire.getwebChannels",
#         "id":"req-id-01",
#         "params":{
#             "apiVersion":"1.2",
#             "type":"AVAIL_CHAN_REQ",
#             "uniqueID":{
#                 "databaseID":"CSIR",
#                 "apiKey":"",
#             },
#             "location":{
#                 "point":{
#                     "center":{
#                         "latitude":latitude,
#                         "longitude":longitude,
#                     }
#                 }
#             },
#             "antennaHeight_AGL":height,
#             "propagationModel":"ITU-R P.1546 B",
#             "wsdPower": "4 W",

#             },
#             "jsonrpc":"2.0",
#     }
#     response = requests.get('https://glsdceapis.meraka.csir.co.za:8443/CSIRCE')
#     specs = response['intermediateValues']
#     return render(request, 'paws/spec.html', {'result': specs})
def chan(request):
    message = {
        "method": "csirce.getWebChannels",
        "id": "371506",
        "params": {
            "apiVersion": "1.2",
            "type": "AVAIL_CHAN_REQ",
            "uniqueID": {
                "databaseID": "AAITE",
                "apiKey":"9bf05b92-5442-491b-a52a-a1f1b719b4bb",
            },
            "location": {
                "point": {    
                    "center": {
                        "latitude": -25.0,
                        "longitude": 29.0
                    }
                }
            },
            "antennaHeight_AGL": 10.2,
            "propagationModel": "ITU-R P.1546 B",
            "wsdPower": "4 W"
        },
        "jsonrpc": "2.0"
    }
    url = 'https://glsdceapis.meraka.csir.co.za:8443/CSIRCE'
    response = requests.post(url, data=json.dumps(message)).json()
    print(response)
    try:
        specs = response['result']['channels']
    except KeyError:
        return HttpResponse('<p>'+str(datetime.now())+":"+repr(response)+'</p>')
    return render(request, 'paws/display_chan.html', {'results':specs})
    
def intermediate(request):
    message = {
        "jsonrpc": "2.0",
        "method": "csirce.incumbentDataset",
        "id": "371506",
        "params": {
            "type": "ICALC_REQ",
            "apiVersion": "1.2",
            "timeStamp": "2017-11-01T10:12:45Z",
            "uniqueID": {
                    "databaseID": "AAITE",
                    "apiKey":"9bf05b92-5442-491b-a52a-a1f1b719b4bb",
            },
        "incumbentdDataset":[{'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'FURI(AA)', 'longtiude': '14.68694444', 'frequency': '178', 'antennaHeight_AGL': '60', 'latitude': '8.88277778', 'path': 'Land', 'maxERP': '5', 'recordNumber': '1', 'channel': '5', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'FURI(AA)', 'longtiude': '14.68694444', 'frequency': '192', 'antennaHeight_AGL': '60', 'latitude': '8.88277778', 'path': 'Land', 'maxERP': '5', 'recordNumber': '2', 'channel': '7', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'HARAR', 'longtiude': '9.28861111', 'frequency': '192', 'antennaHeight_AGL': '60', 'latitude': '42.12444444', 'path': 'Land', 'maxERP': '1', 'recordNumber': '3', 'channel': '7', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'DIRE DAWA', 'longtiude': '41.83444444', 'frequency': '178', 'antennaHeight_AGL': '60', 'latitude': '9.5875', 'path': 'Land', 'maxERP': '0.25', 'recordNumber': '4', 'channel': '5', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'JIJIGA', 'longtiude': '42.7025', 'frequency': '192', 'antennaHeight_AGL': '60', 'latitude': '9.3525', 'path': 'Land', 'maxERP': '0.2', 'recordNumber': '5', 'channel': '11', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'NAZIRETH', 'longtiude': '8.55222222', 'frequency': '178', 'antennaHeight_AGL': '60', 'latitude': '39.23333333', 'path': 'Land', 'maxERP': '1', 'recordNumber': '6', 'channel': '11', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'DESSIE', 'longtiude': '39.61361111', 'frequency': '220', 'antennaHeight_AGL': '60', 'latitude': '11.11972222', 'path': 'Land', 'maxERP': '1', 'recordNumber': '7', 'channel': '9', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'JIMMA', 'longtiude': '36.86694444', 'frequency': '220', 'antennaHeight_AGL': '60', 'latitude': '7.71888889', 'path': 'Land', 'maxERP': '0.5', 'recordNumber': '8', 'channel': '5', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'NEKEMTE ', 'longtiude': '9.11027778', 'frequency': '206', 'antennaHeight_AGL': '60', 'latitude': '36.6325', 'path': 'Land', 'maxERP': '0.5', 'recordNumber': '9', 'channel': '9', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'SHASHEMENE', 'longtiude': '7.12666667', 'frequency': '206', 'antennaHeight_AGL': '60', 'latitude': '38.62166667', 'path': 'Land', 'maxERP': '1', 'recordNumber': '10', 'channel': '5', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'DILA', 'longtiude': '38.39416667', 'frequency': '178', 'antennaHeight_AGL': '60', 'latitude': '6.43694444', 'path': 'Land', 'maxERP': '0.5', 'recordNumber': '11', 'channel': '11', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'GONDAR', 'longtiude': '12.63027778', 'frequency': '178', 'antennaHeight_AGL': '60', 'latitude': '37.46777778', 'path': 'Land', 'maxERP': '0.5', 'recordNumber': '12', 'channel': '7', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'BAHIRDAR', 'longtiude': '11.59416667', 'frequency': '192', 'antennaHeight_AGL': '60', 'latitude': '37.35861111', 'path': 'Land', 'maxERP': '0.4', 'recordNumber': '13', 'channel': '5', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'MEKELE', 'longtiude': '39.54361111', 'frequency': '185', 'antennaHeight_AGL': '60', 'latitude': '13.55638889', 'path': 'Land', 'maxERP': '1', 'recordNumber': '14', 'channel': '7', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'AXUM', 'longtiude': '38.80083333', 'frequency': '206', 'antennaHeight_AGL': '60', 'latitude': '14.1175', 'path': 'Land', 'maxERP': '1', 'recordNumber': '15', 'channel': '9', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'ASSOSA', 'longtiude': '34.57722222', 'frequency': '220', 'antennaHeight_AGL': '60', 'latitude': '10.06444444', 'path': 'Land', 'maxERP': '1', 'recordNumber': '16', 'channel': '11', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'GODE', 'longtiude': '43.01444444', 'frequency': '206', 'antennaHeight_AGL': '60', 'latitude': '6.1025', 'path': 'Land', 'maxERP': '1', 'recordNumber': '17', 'channel': '9', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'ADI REMEST', 'longtiude': '37.3225', 'frequency': '586', 'antennaHeight_AGL': '100', 'latitude': '13.74166667', 'path': 'Land', 'maxERP': '3', 'recordNumber': '18', 'channel': '35', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'ANKOBER', 'longtiude': '39.73416667', 'frequency': '578', 'antennaHeight_AGL': '80', 'latitude': '9.68805556', 'path': 'Land', 'maxERP': '3', 'recordNumber': '19', 'channel': '34', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'ASSOSA', 'longtiude': '34.57722222', 'frequency': '786', 'antennaHeight_AGL': '60', 'latitude': '10.06444444', 'path': 'Land', 'maxERP': '3', 'recordNumber': '20', 'channel': '60', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'DEBARK', 'longtiude': '37.97944444', 'frequency': '762', 'antennaHeight_AGL': '80', 'latitude': '13.20972222', 'path': 'Land', 'maxERP': '3', 'recordNumber': '21', 'channel': '57', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'DESSIE', 'longtiude': '39.61361111', 'frequency': '690', 'antennaHeight_AGL': '100', 'latitude': '11.11972222', 'path': 'Land', 'maxERP': '3', 'recordNumber': '22', 'channel': '48', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'DILA', 'longtiude': '38.39416667', 'frequency': '538', 'antennaHeight_AGL': '100', 'latitude': '6.43694444', 'path': 'Land', 'maxERP': '3', 'recordNumber': '24', 'channel': '29', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'KEBRIDAHAR ', 'longtiude': '6.74083333', 'frequency': '698', 'antennaHeight_AGL': '100', 'latitude': '44.26805556', 'path': 'Land', 'maxERP': '3', 'recordNumber': '26', 'channel': '24', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'FICHE', 'longtiude': '38.63833333', 'frequency': '706', 'antennaHeight_AGL': '100', 'latitude': '9.77888889', 'path': 'Land', 'maxERP': '3', 'recordNumber': '27', 'channel': '50', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'FURI', 'longtiude': '38.68694444', 'frequency': '642', 'antennaHeight_AGL': '80', 'latitude': '8.88277778', 'path': 'Land', 'maxERP': '3', 'recordNumber': '28', 'channel': '42', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'GORE', 'longtiude': '35.53444444', 'frequency': '706', 'antennaHeight_AGL': '100', 'latitude': '8.15166667', 'path': 'Land', 'maxERP': '3', 'recordNumber': '29', 'channel': '50', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'JIJIGA', 'longtiude': '42.7025', 'frequency': '650', 'antennaHeight_AGL': '80', 'latitude': '9.3525', 'path': 'Land', 'maxERP': '3', 'recordNumber': '30', 'channel': '43', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'JIMMA', 'longtiude': '36.86694444', 'frequency': '666', 'antennaHeight_AGL': '80', 'latitude': '7.71888889', 'path': 'Land', 'maxERP': '3', 'recordNumber': '31', 'channel': '45', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'JINKA', 'longtiude': '36.68444444', 'frequency': '674', 'antennaHeight_AGL': '80', 'latitude': '5.70138889', 'path': 'Land', 'maxERP': '3', 'recordNumber': '32', 'channel': '46', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'KUNI', 'longtiude': '40.86555556', 'frequency': '546', 'antennaHeight_AGL': '60', 'latitude': '8.99972222', 'path': 'Land', 'maxERP': '3', 'recordNumber': '33', 'channel': '35', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'MAICHEW', 'longtiude': '39.56277778', 'frequency': '738', 'antennaHeight_AGL': '100', 'latitude': '12.83305556', 'path': 'Land', 'maxERP': '3', 'recordNumber': '34', 'channel': '54', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'NEFAS MEWCHA', 'longtiude': '38.39027778', 'frequency': '474', 'antennaHeight_AGL': '100', 'latitude': '11.70194444', 'path': 'Land', 'maxERP': '3', 'recordNumber': '35', 'channel': '21', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'SHEBEL ', 'longtiude': '34.58777778', 'frequency': '530', 'antennaHeight_AGL': '80', 'latitude': '8.45472222', 'path': 'Land', 'maxERP': '3', 'recordNumber': '36', 'channel': '28', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'TENDAHO', 'longtiude': '40.94166667', 'frequency': '650', 'antennaHeight_AGL': '60', 'latitude': '11.67194444', 'path': 'Land', 'maxERP': '3', 'recordNumber': '37', 'channel': '43', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'WELDIA', 'longtiude': '39.60944444', 'frequency': '506', 'antennaHeight_AGL': '60', 'latitude': '11.85388889', 'path': 'Land', 'maxERP': '3', 'recordNumber': '38', 'channel': '25', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'NEKEMTE ', 'longtiude': '9.11027778', 'frequency': '610', 'antennaHeight_AGL': '100', 'latitude': '38.6325', 'path': 'Land', 'maxERP': '3', 'recordNumber': '39', 'channel': '38', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'GODE', 'longtiude': '43.01444444', 'frequency': '530', 'antennaHeight_AGL': '60', 'latitude': '6.1025', 'path': 'Land', 'maxERP': '3', 'recordNumber': '40', 'channel': '28', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'MEKELE', 'longtiude': '39.54361111', 'frequency': '738', 'antennaHeight_AGL': '100', 'latitude': '13.55638889', 'path': 'Land', 'maxERP': '3', 'recordNumber': '41', 'channel': '54', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'AXUM', 'longtiude': '38.80083333', 'frequency': '714', 'antennaHeight_AGL': '100', 'latitude': '14.1175', 'path': 'Land', 'maxERP': '3', 'recordNumber': '42', 'channel': '51', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'DIRE DAWA', 'longtiude': '41.83444444', 'frequency': '642', 'antennaHeight_AGL': '60', 'latitude': '9.5875', 'path': 'Land', 'maxERP': '3', 'recordNumber': '43', 'channel': '42', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'MEGA', 'longtiude': '38.32305556', 'frequency': '730', 'antennaHeight_AGL': '100', 'latitude': '4.09305556', 'path': 'Land', 'maxERP': '3', 'recordNumber': '44', 'channel': '53', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'Choke Terara', 'longtiude': '37.83972222', 'frequency': '562', 'antennaHeight_AGL': '80', 'latitude': '10.64861111', 'path': 'Land', 'maxERP': '3', 'recordNumber': '45', 'channel': '32', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'ABIY ADI', 'longtiude': '38.98972222', 'frequency': '498', 'antennaHeight_AGL': '60', 'latitude': '13.62694444', 'path': 'Land', 'maxERP': '3', 'recordNumber': '46', 'channel': '24', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'AMENTILA', 'longtiude': '13.36444444', 'frequency': '626', 'antennaHeight_AGL': '80', 'latitude': '39.70777778', 'path': 'Land', 'maxERP': '3', 'recordNumber': '47', 'channel': '40', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'DERBA', 'longtiude': '5.8225', 'frequency': '578', 'antennaHeight_AGL': '80', 'latitude': '37.83944444', 'path': 'Land', 'maxERP': '3', 'recordNumber': '48', 'channel': '34', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'WARDER', 'longtiude': '6.96972222', 'frequency': '682', 'antennaHeight_AGL': '60', 'latitude': '45.34472222', 'path': 'Land', 'maxERP': '2', 'recordNumber': '49', 'channel': '47', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'FILTU', 'longtiude': '5.13666667', 'frequency': '634', 'antennaHeight_AGL': '80', 'latitude': '40.52416667', 'path': 'Land', 'maxERP': '0.5', 'recordNumber': '50', 'channel': '41', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'ADIGRAT', 'longtiude': '14.2475', 'frequency': '714', 'antennaHeight_AGL': '100', 'latitude': '39.41555556', 'path': 'Land', 'maxERP': '3', 'recordNumber': '51', 'channel': '51', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'GINIR', 'longtiude': '7.14944444', 'frequency': '666', 'antennaHeight_AGL': '100', 'latitude': '40.71416667', 'path': 'Land', 'maxERP': '3', 'recordNumber': '52', 'channel': '45', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'DELLOMENA', 'longtiude': '6.41361111', 'frequency': '626', 'antennaHeight_AGL': '60', 'latitude': '39.84527778', 'path': 'Land', 'maxERP': '2', 'recordNumber': '53', 'channel': '40', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'FIK', 'longtiude': '8.13194444', 'frequency': '714', 'antennaHeight_AGL': '60', 'latitude': '42.29944444', 'path': 'Land', 'maxERP': '2', 'recordNumber': '54', 'channel': '51', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'MAJI', 'longtiude': '6.15027778', 'frequency': '594', 'antennaHeight_AGL': '80', 'latitude': '35.59638889', 'path': 'Land', 'maxERP': '2', 'recordNumber': '55', 'channel': '36', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'GUBA', 'longtiude': '11.2525', 'frequency': '490', 'antennaHeight_AGL': '60', 'latitude': '35.30472222', 'path': 'Land', 'maxERP': '3', 'recordNumber': '56', 'channel': '23', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'YABELLO', 'longtiude': '4.88722222', 'frequency': '706', 'antennaHeight_AGL': '60', 'latitude': '38.08638889', 'path': 'Land', 'maxERP': '1', 'recordNumber': '57', 'channel': '50', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'SAMRE ', 'longtiude': '13.17916667', 'frequency': '682', 'antennaHeight_AGL': '80', 'latitude': '39.21472222', 'path': 'Land', 'maxERP': '3', 'recordNumber': '58', 'channel': '47', 'programme': 'PAL'}, {'status': 'Operational', 'polarization': 'VERT', 'countryCode': 'ET', 'siteName': 'Bella/Ghimbi/BILLA', 'longtiude': '7.34194444', 'frequency': '698', 'antennaHeight_AGL': '80', 'latitude': '35.57722222', 'path': 'Land', 'maxERP': '3', 'recordNumber': '59', 'channel': '24', 'programme': 'PAL'}]
        }
    }

    url = 'https://glsdceapis.meraka.csir.co.za:8443/CSIRCE'
    response = requests.post(url, data=json.dumps(message)).json()
    print(response)
    try:
        specs = response['spectrumSpecs']['spectrumSchedules']['spectra']['profiles']
    except KeyError:
        return HttpResponse('<p>'+str(datetime.now())+":"+repr(response)+'</p>')
    return render(request, 'paws/spec.html', {'results':specs})
    
def spectrum(request):
    #     #height = str(request.GET['h'])
    #     #latitude = str(request.GET['lat'])
    #     #longitude = str(request.GET['long'])
    #     #serial = str(request.GET['ser'])
    #     #model = str(request.GET['mod'])
    #     #regulator = str(request.GET['reg'])
    message = {
        "jsonrpc": "2.0",
        "method": "csirce.getSpectrum",
        "id": "371506",
        "params": {
            "apiVersion":"1.2",
            "type": "AVAIL_SPECTRUM_REQ",
            "uniqueID": {
                "databaseID": "AAITE",
                "apiKey":"9bf05b92-5442-491b-a52a-a1f1b719b4bb",
            },
            "antenna": {
                "heightType": "AGL",
                "height": 10.2
            },
            "location": {
                "point": {
                    "center": {
                        "latitude": -25.0,
                        "longitude": 29.0
                    }
                }
            },
            "deviceDesc": {
                "serialNumber": "SN504",
                "modelId": "MN110",
                "regulatorId": "FCC110"
            }
        }
    }
    url = 'https://glsdceapis.meraka.csir.co.za:8443/CSIRCE'
    response = requests.post(url, data=json.dumps(message)).json()
    #print(response)
    try:
        specs = response['result']['spectrumSpecs'][0]['spectrumSchedules'][0]['spectra'][0]['profiles']
        print(type(specs))
    except KeyError:
        return HttpResponse('<p>'+str(datetime.now())+":"+repr(response)+'</p>')
    return render(request, 'paws/display_spectrum.html', {'results':specs})
        
def results(request):
    return HttpResponse('<p>Sent</p>')
