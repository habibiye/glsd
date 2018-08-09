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
    if request.method == 'GET':
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
            "incumbentDataset":[{'recordNumber': 1, 'countryCode': 'ET', 'siteName': 'FURI(AA)', 'programme': 'PAL', 'latitude': 8.88277778, 'longtiude': 14.68694444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 178.0, 'channel': 5, 'maxERP': 5.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 2, 'countryCode': 'ET', 'siteName': 'FURI(AA)', 'programme': 'PAL', 'latitude': 8.88277778, 'longtiude': 14.68694444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 192.0, 'channel': 7, 'maxERP': 5.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 3, 'countryCode': 'ET', 'siteName': 'HARAR', 'programme': 'PAL', 'latitude': 42.12444444, 'longtiude': 9.28861111, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 192.0, 'channel': 7, 'maxERP': 1.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 4, 'countryCode': 'ET', 'siteName': 'DIRE DAWA', 'programme': 'PAL', 'latitude': 9.5875, 'longtiude': 41.83444444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 178.0, 'channel': 5, 'maxERP': 0.25, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 5, 'countryCode': 'ET', 'siteName': 'JIJIGA', 'programme': 'PAL', 'latitude': 9.3525, 'longtiude': 42.7025, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 192.0, 'channel': 11, 'maxERP': 0.2, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 6, 'countryCode': 'ET', 'siteName': 'NAZIRETH', 'programme': 'PAL', 'latitude': 39.23333333, 'longtiude': 8.55222222, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 178.0, 'channel': 11, 'maxERP': 1.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 7, 'countryCode': 'ET', 'siteName': 'DESSIE', 'programme': 'PAL', 'latitude': 11.11972222, 'longtiude': 39.61361111, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 220.0, 'channel': 9, 'maxERP': 1.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 8, 'countryCode': 'ET', 'siteName': 'JIMMA', 'programme': 'PAL', 'latitude': 7.71888889, 'longtiude': 36.86694444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 220.0, 'channel': 5, 'maxERP': 0.5, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 9, 'countryCode': 'ET', 'siteName': 'NEKEMTE ', 'programme': 'PAL', 'latitude': 36.6325, 'longtiude': 9.11027778, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 206.0, 'channel': 9, 'maxERP': 0.5, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 10, 'countryCode': 'ET', 'siteName': 'SHASHEMENE', 'programme': 'PAL', 'latitude': 38.62166667, 'longtiude': 7.12666667, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 206.0, 'channel': 5, 'maxERP': 1.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 11, 'countryCode': 'ET', 'siteName': 'DILA', 'programme': 'PAL', 'latitude': 6.43694444, 'longtiude': 38.39416667, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 178.0, 'channel': 11, 'maxERP': 0.5, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 12, 'countryCode': 'ET', 'siteName': 'GONDAR', 'programme': 'PAL', 'latitude': 37.46777778, 'longtiude': 12.63027778, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 178.0, 'channel': 7, 'maxERP': 0.5, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 13, 'countryCode': 'ET', 'siteName': 'BAHIRDAR', 'programme': 'PAL', 'latitude': 37.35861111, 'longtiude': 11.59416667, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 192.0, 'channel': 5, 'maxERP': 0.4, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 14, 'countryCode': 'ET', 'siteName': 'MEKELE', 'programme': 'PAL', 'latitude': 13.55638889, 'longtiude': 39.54361111, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 185.0, 'channel': 7, 'maxERP': 1.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 15, 'countryCode': 'ET', 'siteName': 'AXUM', 'programme': 'PAL', 'latitude': 14.1175, 'longtiude': 38.80083333, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 206.0, 'channel': 9, 'maxERP': 1.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 16, 'countryCode': 'ET', 'siteName': 'ASSOSA', 'programme': 'PAL', 'latitude': 10.06444444, 'longtiude': 34.57722222, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 220.0, 'channel': 11, 'maxERP': 1.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 17, 'countryCode': 'ET', 'siteName': 'GODE', 'programme': 'PAL', 'latitude': 6.1025, 'longtiude': 43.01444444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 206.0, 'channel': 9, 'maxERP': 1.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 18, 'countryCode': 'ET', 'siteName': 'ADI REMEST', 'programme': 'PAL', 'latitude': 13.74166667, 'longtiude': 37.3225, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 586.0, 'channel': 35, 'maxERP': 3.0, 'antennaHeight_AGL': 100.0, 'path': 'Land'}, {'recordNumber': 19, 'countryCode': 'ET', 'siteName': 'ANKOBER', 'programme': 'PAL', 'latitude': 9.68805556, 'longtiude': 39.73416667, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 578.0, 'channel': 34, 'maxERP': 3.0, 'antennaHeight_AGL': 80.0, 'path': 'Land'}, {'recordNumber': 20, 'countryCode': 'ET', 'siteName': 'ASSOSA', 'programme': 'PAL', 'latitude': 10.06444444, 'longtiude': 34.57722222, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 786.0, 'channel': 60, 'maxERP': 3.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 21, 'countryCode': 'ET', 'siteName': 'DEBARK', 'programme': 'PAL', 'latitude': 13.20972222, 'longtiude': 37.97944444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 762.0, 'channel': 57, 'maxERP': 3.0, 'antennaHeight_AGL': 80.0, 'path': 'Land'}, {'recordNumber': 22, 'countryCode': 'ET', 'siteName': 'DESSIE', 'programme': 'PAL', 'latitude': 11.11972222, 'longtiude': 39.61361111, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 690.0, 'channel': 48, 'maxERP': 3.0, 'antennaHeight_AGL': 100.0, 'path': 'Land'}, {'recordNumber': 24, 'countryCode': 'ET', 'siteName': 'DILA', 'programme': 'PAL', 'latitude': 6.43694444, 'longtiude': 38.39416667, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 538.0, 'channel': 29, 'maxERP': 3.0, 'antennaHeight_AGL': 100.0, 'path': 'Land'}, {'recordNumber': 26, 'countryCode': 'ET', 'siteName': 'KEBRIDAHAR ', 'programme': 'PAL', 'latitude': 44.26805556, 'longtiude': 6.74083333, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 698.0, 'channel': 24, 'maxERP': 3.0, 'antennaHeight_AGL': 100.0, 'path': 'Land'}, {'recordNumber': 27, 'countryCode': 'ET', 'siteName': 'FICHE', 'programme': 'PAL', 'latitude': 9.77888889, 'longtiude': 38.63833333, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 706.0, 'channel': 50, 'maxERP': 3.0, 'antennaHeight_AGL': 100.0, 'path': 'Land'}, {'recordNumber': 28, 'countryCode': 'ET', 'siteName': 'FURI', 'programme': 'PAL', 'latitude': 8.88277778, 'longtiude': 38.68694444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 642.0, 'channel': 42, 'maxERP': 3.0, 'antennaHeight_AGL': 80.0, 'path': 'Land'}, {'recordNumber': 29, 'countryCode': 'ET', 'siteName': 'GORE', 'programme': 'PAL', 'latitude': 8.15166667, 'longtiude': 35.53444444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 706.0, 'channel': 50, 'maxERP': 3.0, 'antennaHeight_AGL': 100.0, 'path': 'Land'}, {'recordNumber': 30, 'countryCode': 'ET', 'siteName': 'JIJIGA', 'programme': 'PAL', 'latitude': 9.3525, 'longtiude': 42.7025, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 650.0, 'channel': 43, 'maxERP': 3.0, 'antennaHeight_AGL': 80.0, 'path': 'Land'}, {'recordNumber': 31, 'countryCode': 'ET', 'siteName': 'JIMMA', 'programme': 'PAL', 'latitude': 7.71888889, 'longtiude': 36.86694444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 666.0, 'channel': 45, 'maxERP': 3.0, 'antennaHeight_AGL': 80.0, 'path': 'Land'}, {'recordNumber': 32, 'countryCode': 'ET', 'siteName': 'JINKA', 'programme': 'PAL', 'latitude': 5.70138889, 'longtiude': 36.68444444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 674.0, 'channel': 46, 'maxERP': 3.0, 'antennaHeight_AGL': 80.0, 'path': 'Land'}, {'recordNumber': 33, 'countryCode': 'ET', 'siteName': 'KUNI', 'programme': 'PAL', 'latitude': 8.99972222, 'longtiude': 40.86555556, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 546.0, 'channel': 35, 'maxERP': 3.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 34, 'countryCode': 'ET', 'siteName': 'MAICHEW', 'programme': 'PAL', 'latitude': 12.83305556, 'longtiude': 39.56277778, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 738.0, 'channel': 54, 'maxERP': 3.0, 'antennaHeight_AGL': 100.0, 'path': 'Land'}, {'recordNumber': 35, 'countryCode': 'ET', 'siteName': 'NEFAS MEWCHA', 'programme': 'PAL', 'latitude': 11.70194444, 'longtiude': 38.39027778, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 474.0, 'channel': 21, 'maxERP': 3.0, 'antennaHeight_AGL': 100.0, 'path': 'Land'}, {'recordNumber': 36, 'countryCode': 'ET', 'siteName': 'SHEBEL ', 'programme': 'PAL', 'latitude': 8.45472222, 'longtiude': 34.58777778, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 530.0, 'channel': 28, 'maxERP': 3.0, 'antennaHeight_AGL': 80.0, 'path': 'Land'}, {'recordNumber': 37, 'countryCode': 'ET', 'siteName': 'TENDAHO', 'programme': 'PAL', 'latitude': 11.67194444, 'longtiude': 40.94166667, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 650.0, 'channel': 43, 'maxERP': 3.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 38, 'countryCode': 'ET', 'siteName': 'WELDIA', 'programme': 'PAL', 'latitude': 11.85388889, 'longtiude': 39.60944444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 506.0, 'channel': 25, 'maxERP': 3.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 39, 'countryCode': 'ET', 'siteName': 'NEKEMTE ', 'programme': 'PAL', 'latitude': 38.6325, 'longtiude': 9.11027778, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 610.0, 'channel': 38, 'maxERP': 3.0, 'antennaHeight_AGL': 100.0, 'path': 'Land'}, {'recordNumber': 40, 'countryCode': 'ET', 'siteName': 'GODE', 'programme': 'PAL', 'latitude': 6.1025, 'longtiude': 43.01444444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 530.0, 'channel': 28, 'maxERP': 3.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 41, 'countryCode': 'ET', 'siteName': 'MEKELE', 'programme': 'PAL', 'latitude': 13.55638889, 'longtiude': 39.54361111, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 738.0, 'channel': 54, 'maxERP': 3.0, 'antennaHeight_AGL': 100.0, 'path': 'Land'}, {'recordNumber': 42, 'countryCode': 'ET', 'siteName': 'AXUM', 'programme': 'PAL', 'latitude': 14.1175, 'longtiude': 38.80083333, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 714.0, 'channel': 51, 'maxERP': 3.0, 'antennaHeight_AGL': 100.0, 'path': 'Land'}, {'recordNumber': 43, 'countryCode': 'ET', 'siteName': 'DIRE DAWA', 'programme': 'PAL', 'latitude': 9.5875, 'longtiude': 41.83444444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 642.0, 'channel': 42, 'maxERP': 3.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 44, 'countryCode': 'ET', 'siteName': 'MEGA', 'programme': 'PAL', 'latitude': 4.09305556, 'longtiude': 38.32305556, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 730.0, 'channel': 53, 'maxERP': 3.0, 'antennaHeight_AGL': 100.0, 'path': 'Land'}, {'recordNumber': 45, 'countryCode': 'ET', 'siteName': 'Choke Terara', 'programme': 'PAL', 'latitude': 10.64861111, 'longtiude': 37.83972222, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 562.0, 'channel': 32, 'maxERP': 3.0, 'antennaHeight_AGL': 80.0, 'path': 'Land'}, {'recordNumber': 46, 'countryCode': 'ET', 'siteName': 'ABIY ADI', 'programme': 'PAL', 'latitude': 13.62694444, 'longtiude': 38.98972222, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 498.0, 'channel': 24, 'maxERP': 3.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 47, 'countryCode': 'ET', 'siteName': 'AMENTILA', 'programme': 'PAL', 'latitude': 39.70777778, 'longtiude': 13.36444444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 626.0, 'channel': 40, 'maxERP': 3.0, 'antennaHeight_AGL': 80.0, 'path': 'Land'}, {'recordNumber': 48, 'countryCode': 'ET', 'siteName': 'DERBA', 'programme': 'PAL', 'latitude': 37.83944444, 'longtiude': 5.8225, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 578.0, 'channel': 34, 'maxERP': 3.0, 'antennaHeight_AGL': 80.0, 'path': 'Land'}, {'recordNumber': 49, 'countryCode': 'ET', 'siteName': 'WARDER', 'programme': 'PAL', 'latitude': 45.34472222, 'longtiude': 6.96972222, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 682.0, 'channel': 47, 'maxERP': 2.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 50, 'countryCode': 'ET', 'siteName': 'FILTU', 'programme': 'PAL', 'latitude': 40.52416667, 'longtiude': 5.13666667, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 634.0, 'channel': 41, 'maxERP': 0.5, 'antennaHeight_AGL': 80.0, 'path': 'Land'}, {'recordNumber': 51, 'countryCode': 'ET', 'siteName': 'ADIGRAT', 'programme': 'PAL', 'latitude': 39.41555556, 'longtiude': 14.2475, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 714.0, 'channel': 51, 'maxERP': 3.0, 'antennaHeight_AGL': 100.0, 'path': 'Land'}, {'recordNumber': 52, 'countryCode': 'ET', 'siteName': 'GINIR', 'programme': 'PAL', 'latitude': 40.71416667, 'longtiude': 7.14944444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 666.0, 'channel': 45, 'maxERP': 3.0, 'antennaHeight_AGL': 100.0, 'path': 'Land'}, {'recordNumber': 53, 'countryCode': 'ET', 'siteName': 'DELLOMENA', 'programme': 'PAL', 'latitude': 39.84527778, 'longtiude': 6.41361111, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 626.0, 'channel': 40, 'maxERP': 2.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 54, 'countryCode': 'ET', 'siteName': 'FIK', 'programme': 'PAL', 'latitude': 42.29944444, 'longtiude': 8.13194444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 714.0, 'channel': 51, 'maxERP': 2.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 55, 'countryCode': 'ET', 'siteName': 'MAJI', 'programme': 'PAL', 'latitude': 35.59638889, 'longtiude': 6.15027778, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 594.0, 'channel': 36, 'maxERP': 2.0, 'antennaHeight_AGL': 80.0, 'path': 'Land'}, {'recordNumber': 56, 'countryCode': 'ET', 'siteName': 'GUBA', 'programme': 'PAL', 'latitude': 35.30472222, 'longtiude': 11.2525, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 490.0, 'channel': 23, 'maxERP': 3.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 57, 'countryCode': 'ET', 'siteName': 'YABELLO', 'programme': 'PAL', 'latitude': 38.08638889, 'longtiude': 4.88722222, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 706.0, 'channel': 50, 'maxERP': 1.0, 'antennaHeight_AGL': 60.0, 'path': 'Land'}, {'recordNumber': 58, 'countryCode': 'ET', 'siteName': 'SAMRE ', 'programme': 'PAL', 'latitude': 39.21472222, 'longtiude': 13.17916667, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 682.0, 'channel': 47, 'maxERP': 3.0, 'antennaHeight_AGL': 80.0, 'path': 'Land'}, {'recordNumber': 59, 'countryCode': 'ET', 'siteName': 'Bella/Ghimbi/BILLA', 'programme': 'PAL', 'latitude': 35.57722222, 'longtiude': 7.34194444, 'polarization': 'VERT', 'status': 'Operational', 'frequency': 698.0, 'channel': 24, 'maxERP': 3.0, 'antennaHeight_AGL': 80.0, 'path': 'Land'}]
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
    elif request.method == 'POST':
        pass        
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
