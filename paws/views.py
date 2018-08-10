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
    height = float(request.GET['h'])
    latitude = float(request.GET['lat'])
    longitude = float(request.GET['long'])
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
                        "latitude": -latitude,
                        "longitude": longitude
                    }
                }
            },
            "antennaHeight_AGL": height,
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
            "incumbentDataset":[{"recordNumber": 1, "countryCode": "ET", "siteName": "FURI", "programme": "PAL", "latitude": 8.8827, "longitude": 14.6869, "polarization": "HOR", "status": "Operational", "frequency": 178.0, "channel": 5, "maxERP": 5.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 2, "countryCode": "ET", "siteName": "FURI", "programme": "PAL", "latitude": 8.8827, "longitude": 14.6869, "polarization": "HOR", "status": "Operational", "frequency": 192.0, "channel": 7, "maxERP": 5.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 3, "countryCode": "ET", "siteName": "HARAR", "programme": "PAL", "latitude": 42.1244, "longitude": 9.2886, "polarization": "HOR", "status": "Operational", "frequency": 192.0, "channel": 7, "maxERP": 1.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 4, "countryCode": "ET", "siteName": "DIREDAWA", "programme": "PAL", "latitude": 9.5875, "longitude": 41.8344, "polarization": "HOR", "status": "Operational", "frequency": 178.0, "channel": 5, "maxERP": 0.25, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 5, "countryCode": "ET", "siteName": "JIJIGA", "programme": "PAL", "latitude": 9.3524, "longitude": 42.7025, "polarization": "HOR", "status": "Operational", "frequency": 192.0, "channel": 11, "maxERP": 0.2, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 6, "countryCode": "ET", "siteName": "NAZIRETH", "programme": "PAL", "latitude": 39.2333, "longitude": 8.5522, "polarization": "HOR", "status": "Operational", "frequency": 178.0, "channel": 11, "maxERP": 1.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 7, "countryCode": "ET", "siteName": "DESSIE", "programme": "PAL", "latitude": 11.1197, "longitude": 39.6136, "polarization": "HOR", "status": "Operational", "frequency": 220.0, "channel": 9, "maxERP": 1.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 8, "countryCode": "ET", "siteName": "JIMMA", "programme": "PAL", "latitude": 7.7188, "longitude": 36.8669, "polarization": "HOR", "status": "Operational", "frequency": 220.0, "channel": 5, "maxERP": 0.5, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 9, "countryCode": "ET", "siteName": "NEKEMTE", "programme": "PAL", "latitude": 36.6325, "longitude": 9.1102, "polarization": "HOR", "status": "Operational", "frequency": 206.0, "channel": 9, "maxERP": 0.5, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 10, "countryCode": "ET", "siteName": "SHASHEMENE", "programme": "PAL", "latitude": 38.6216, "longitude": 7.1266, "polarization": "HOR", "status": "Operational", "frequency": 206.0, "channel": 5, "maxERP": 1.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 11, "countryCode": "ET", "siteName": "DILA", "programme": "PAL", "latitude": 6.4369, "longitude": 38.3941, "polarization": "HOR", "status": "Operational", "frequency": 178.0, "channel": 11, "maxERP": 0.5, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 12, "countryCode": "ET", "siteName": "GONDAR", "programme": "PAL", "latitude": 37.4677, "longitude": 12.6302, "polarization": "HOR", "status": "Operational", "frequency": 178.0, "channel": 7, "maxERP": 0.5, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 13, "countryCode": "ET", "siteName": "BAHIRDAR", "programme": "PAL", "latitude": 37.3586, "longitude": 11.5941, "polarization": "HOR", "status": "Operational", "frequency": 192.0, "channel": 5, "maxERP": 0.4, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 14, "countryCode": "ET", "siteName": "MEKELE", "programme": "PAL", "latitude": 13.5563, "longitude": 39.5436, "polarization": "HOR", "status": "Operational", "frequency": 185.0, "channel": 7, "maxERP": 1.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 15, "countryCode": "ET", "siteName": "AXUM", "programme": "PAL", "latitude": 14.1175, "longitude": 38.8008, "polarization": "HOR", "status": "Operational", "frequency": 206.0, "channel": 9, "maxERP": 1.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 16, "countryCode": "ET", "siteName": "ASSOSA", "programme": "PAL", "latitude": 10.0644, "longitude": 34.5772, "polarization": "HOR", "status": "Operational", "frequency": 220.0, "channel": 11, "maxERP": 1.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 17, "countryCode": "ET", "siteName": "GODE", "programme": "PAL", "latitude": 6.1025, "longitude": 43.0144, "polarization": "HOR", "status": "Operational", "frequency": 206.0, "channel": 9, "maxERP": 1.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 18, "countryCode": "ET", "siteName": "ADIREMEST", "programme": "PAL", "latitude": 13.7416, "longitude": 37.3225, "polarization": "HOR", "status": "Operational", "frequency": 586.0, "channel": 35, "maxERP": 3.0, "antennaHeight_AGL": 100.0, "path": "Land"}, {"recordNumber": 19, "countryCode": "ET", "siteName": "ANKOBER", "programme": "PAL", "latitude": 9.688, "longitude": 39.7341, "polarization": "HOR", "status": "Operational", "frequency": 578.0, "channel": 34, "maxERP": 3.0, "antennaHeight_AGL": 80.0, "path": "Land"}, {"recordNumber": 20, "countryCode": "ET", "siteName": "ASSOSA", "programme": "PAL", "latitude": 10.0644, "longitude": 34.5772, "polarization": "HOR", "status": "Operational", "frequency": 786.0, "channel": 60, "maxERP": 3.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 21, "countryCode": "ET", "siteName": "DEBARK", "programme": "PAL", "latitude": 13.2097, "longitude": 37.9794, "polarization": "HOR", "status": "Operational", "frequency": 762.0, "channel": 57, "maxERP": 3.0, "antennaHeight_AGL": 80.0, "path": "Land"}, {"recordNumber": 22, "countryCode": "ET", "siteName": "DESSIE", "programme": "PAL", "latitude": 11.1197, "longitude": 39.6136, "polarization": "HOR", "status": "Operational", "frequency": 690.0, "channel": 48, "maxERP": 3.0, "antennaHeight_AGL": 100.0, "path": "Land"}, {"recordNumber": 24, "countryCode": "ET", "siteName": "DILA", "programme": "PAL", "latitude": 6.4369, "longitude": 38.3941, "polarization": "HOR", "status": "Operational", "frequency": 538.0, "channel": 29, "maxERP": 3.0, "antennaHeight_AGL": 100.0, "path": "Land"}, {"recordNumber": 26, "countryCode": "ET", "siteName": "KEBRIDAHAR", "programme": "PAL", "latitude": 44.268, "longitude": 6.7408, "polarization": "HOR", "status": "Operational", "frequency": 698.0, "channel": 24, "maxERP": 3.0, "antennaHeight_AGL": 100.0, "path": "Land"}, {"recordNumber": 27, "countryCode": "ET", "siteName": "FICHE", "programme": "PAL", "latitude": 9.7788, "longitude": 38.6383, "polarization": "HOR", "status": "Operational", "frequency": 706.0, "channel": 50, "maxERP": 3.0, "antennaHeight_AGL": 100.0, "path": "Land"}, {"recordNumber": 28, "countryCode": "ET", "siteName": "FURI", "programme": "PAL", "latitude": 8.8827, "longitude": 38.6869, "polarization": "HOR", "status": "Operational", "frequency": 642.0, "channel": 42, "maxERP": 3.0, "antennaHeight_AGL": 80.0, "path": "Land"}, {"recordNumber": 29, "countryCode": "ET", "siteName": "GORE", "programme": "PAL", "latitude": 8.1516, "longitude": 35.5344, "polarization": "HOR", "status": "Operational", "frequency": 706.0, "channel": 50, "maxERP": 3.0, "antennaHeight_AGL": 100.0, "path": "Land"}, {"recordNumber": 30, "countryCode": "ET", "siteName": "JIJIGA", "programme": "PAL", "latitude": 9.3524, "longitude": 42.7025, "polarization": "HOR", "status": "Operational", "frequency": 650.0, "channel": 43, "maxERP": 3.0, "antennaHeight_AGL": 80.0, "path": "Land"}, {"recordNumber": 31, "countryCode": "ET", "siteName": "JIMMA", "programme": "PAL", "latitude": 7.7188, "longitude": 36.8669, "polarization": "HOR", "status": "Operational", "frequency": 666.0, "channel": 45, "maxERP": 3.0, "antennaHeight_AGL": 80.0, "path": "Land"}, {"recordNumber": 32, "countryCode": "ET", "siteName": "JINKA", "programme": "PAL", "latitude": 5.7013, "longitude": 36.6844, "polarization": "HOR", "status": "Operational", "frequency": 674.0, "channel": 46, "maxERP": 3.0, "antennaHeight_AGL": 80.0, "path": "Land"}, {"recordNumber": 33, "countryCode": "ET", "siteName": "KUNI", "programme": "PAL", "latitude": 8.9997, "longitude": 40.8655, "polarization": "HOR", "status": "Operational", "frequency": 546.0, "channel": 35, "maxERP": 3.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 34, "countryCode": "ET", "siteName": "MAICHEW", "programme": "PAL", "latitude": 12.833, "longitude": 39.5627, "polarization": "HOR", "status": "Operational", "frequency": 738.0, "channel": 54, "maxERP": 3.0, "antennaHeight_AGL": 100.0, "path": "Land"}, {"recordNumber": 35, "countryCode": "ET", "siteName": "NEFASMEWCHA", "programme": "PAL", "latitude": 11.7019, "longitude": 38.3902, "polarization": "HOR", "status": "Operational", "frequency": 474.0, "channel": 21, "maxERP": 3.0, "antennaHeight_AGL": 100.0, "path": "Land"}, {"recordNumber": 36, "countryCode": "ET", "siteName": "SHEBEL", "programme": "PAL", "latitude": 8.4547, "longitude": 34.5877, "polarization": "HOR", "status": "Operational", "frequency": 530.0, "channel": 28, "maxERP": 3.0, "antennaHeight_AGL": 80.0, "path": "Land"}, {"recordNumber": 37, "countryCode": "ET", "siteName": "TENDAHO", "programme": "PAL", "latitude": 11.6719, "longitude": 40.9416, "polarization": "HOR", "status": "Operational", "frequency": 650.0, "channel": 43, "maxERP": 3.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 38, "countryCode": "ET", "siteName": "WELDIA", "programme": "PAL", "latitude": 11.8538, "longitude": 39.6094, "polarization": "HOR", "status": "Operational", "frequency": 506.0, "channel": 25, "maxERP": 3.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 39, "countryCode": "ET", "siteName": "NEKEMTE", "programme": "PAL", "latitude": 38.6325, "longitude": 9.1102, "polarization": "HOR", "status": "Operational", "frequency": 610.0, "channel": 38, "maxERP": 3.0, "antennaHeight_AGL": 100.0, "path": "Land"}, {"recordNumber": 40, "countryCode": "ET", "siteName": "GODE", "programme": "PAL", "latitude": 6.1025, "longitude": 43.0144, "polarization": "HOR", "status": "Operational", "frequency": 530.0, "channel": 28, "maxERP": 3.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 41, "countryCode": "ET", "siteName": "MEKELE", "programme": "PAL", "latitude": 13.5563, "longitude": 39.5436, "polarization": "HOR", "status": "Operational", "frequency": 738.0, "channel": 54, "maxERP": 3.0, "antennaHeight_AGL": 100.0, "path": "Land"}, {"recordNumber": 42, "countryCode": "ET", "siteName": "AXUM", "programme": "PAL", "latitude": 14.1175, "longitude": 38.8008, "polarization": "HOR", "status": "Operational", "frequency": 714.0, "channel": 51, "maxERP": 3.0, "antennaHeight_AGL": 100.0, "path": "Land"}, {"recordNumber": 43, "countryCode": "ET", "siteName": "DIREDAWA", "programme": "PAL", "latitude": 9.5875, "longitude": 41.8344, "polarization": "HOR", "status": "Operational", "frequency": 642.0, "channel": 42, "maxERP": 3.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 44, "countryCode": "ET", "siteName": "MEGA", "programme": "PAL", "latitude": 4.093, "longitude": 38.323, "polarization": "HOR", "status": "Operational", "frequency": 730.0, "channel": 53, "maxERP": 3.0, "antennaHeight_AGL": 100.0, "path": "Land"}, {"recordNumber": 45, "countryCode": "ET", "siteName": "ChokeTerara", "programme": "PAL", "latitude": 10.6486, "longitude": 37.8397, "polarization": "HOR", "status": "Operational", "frequency": 562.0, "channel": 32, "maxERP": 3.0, "antennaHeight_AGL": 80.0, "path": "Land"}, {"recordNumber": 46, "countryCode": "ET", "siteName": "ABIYADI", "programme": "PAL", "latitude": 13.6269, "longitude": 38.9897, "polarization": "HOR", "status": "Operational", "frequency": 498.0, "channel": 24, "maxERP": 3.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 47, "countryCode": "ET", "siteName": "AMENTILA", "programme": "PAL", "latitude": 39.7077, "longitude": 13.3644, "polarization": "HOR", "status": "Operational", "frequency": 626.0, "channel": 40, "maxERP": 3.0, "antennaHeight_AGL": 80.0, "path": "Land"}, {"recordNumber": 48, "countryCode": "ET", "siteName": "DERBA", "programme": "PAL", "latitude": 37.8394, "longitude": 5.8225, "polarization": "HOR", "status": "Operational", "frequency": 578.0, "channel": 34, "maxERP": 3.0, "antennaHeight_AGL": 80.0, "path": "Land"}, {"recordNumber": 49, "countryCode": "ET", "siteName": "WARDER", "programme": "PAL", "latitude": 45.3447, "longitude": 6.9697, "polarization": "HOR", "status": "Operational", "frequency": 682.0, "channel": 47, "maxERP": 2.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 50, "countryCode": "ET", "siteName": "FILTU", "programme": "PAL", "latitude": 40.5241, "longitude": 5.1366, "polarization": "HOR", "status": "Operational", "frequency": 634.0, "channel": 41, "maxERP": 0.5, "antennaHeight_AGL": 80.0, "path": "Land"}, {"recordNumber": 51, "countryCode": "ET", "siteName": "ADIGRAT", "programme": "PAL", "latitude": 39.4155, "longitude": 14.2475, "polarization": "HOR", "status": "Operational", "frequency": 714.0, "channel": 51, "maxERP": 3.0, "antennaHeight_AGL": 100.0, "path": "Land"}, {"recordNumber": 52, "countryCode": "ET", "siteName": "GINIR", "programme": "PAL", "latitude": 40.7141, "longitude": 7.1494, "polarization": "HOR", "status": "Operational", "frequency": 666.0, "channel": 45, "maxERP": 3.0, "antennaHeight_AGL": 100.0, "path": "Land"}, {"recordNumber": 53, "countryCode": "ET", "siteName": "DELLOMENA", "programme": "PAL", "latitude": 39.8452, "longitude": 6.4136, "polarization": "HOR", "status": "Operational", "frequency": 626.0, "channel": 40, "maxERP": 2.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 54, "countryCode": "ET", "siteName": "FIK", "programme": "PAL", "latitude": 42.2994, "longitude": 8.1319, "polarization": "HOR", "status": "Operational", "frequency": 714.0, "channel": 51, "maxERP": 2.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 55, "countryCode": "ET", "siteName": "MAJI", "programme": "PAL", "latitude": 35.5963, "longitude": 6.1502, "polarization": "HOR", "status": "Operational", "frequency": 594.0, "channel": 36, "maxERP": 2.0, "antennaHeight_AGL": 80.0, "path": "Land"}, {"recordNumber": 56, "countryCode": "ET", "siteName": "GUBA", "programme": "PAL", "latitude": 35.3047, "longitude": 11.2525, "polarization": "HOR", "status": "Operational", "frequency": 490.0, "channel": 23, "maxERP": 3.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 57, "countryCode": "ET", "siteName": "YABELLO", "programme": "PAL", "latitude": 38.0863, "longitude": 4.8872, "polarization": "HOR", "status": "Operational", "frequency": 706.0, "channel": 50, "maxERP": 1.0, "antennaHeight_AGL": 60.0, "path": "Land"}, {"recordNumber": 58, "countryCode": "ET", "siteName": "SAMRE", "programme": "PAL", "latitude": 39.2147, "longitude": 13.1791, "polarization": "HOR", "status": "Operational", "frequency": 682.0, "channel": 47, "maxERP": 3.0, "antennaHeight_AGL": 80.0, "path": "Land"}, {"recordNumber": 59, "countryCode": "ET", "siteName": "BellaGhimbiBILLA", "programme": "PAL", "latitude": 35.5772, "longitude": 7.3419, "polarization": "HOR", "status": "Operational", "frequency": 698.0, "channel": 24, "maxERP": 3.0, "antennaHeight_AGL": 80.0, "path": "Land"}]
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
    height = str(request.GET['h'])
    latitude = str(request.GET['lat'])
    longitude = str(request.GET['long'])
    serial = str(request.GET['ser'])
    model = str(request.GET['mod'])
    regulator = str(request.GET['reg'])
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
                "height": height
            },
            "location": {
                "point": {
                    "center": {
                        "latitude": latitude,
                        "longitude": longtiude
                    }
                }
            },
            "deviceDesc": {
                "serialNumber": serial,
                "modelId": model,
                "regulatorId": regulator
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
