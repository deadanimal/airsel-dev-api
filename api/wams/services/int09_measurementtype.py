from zeep import Client
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
from zeep.settings import Settings

import json
import requests
import xmltodict


def get_measurementtype():

    payload = {
        "token": "tLh-KkVgm8yUgA30ulJNFA",
        "data": {
        "name": "nameFirst",
        "email": "internetEmail",
        "phone": "phoneHome",
        "_repeat": 300
        }
    };

    r = requests.post("http://167.71.199.123:8080/getMeasurementType.php", json = payload)
    return json.loads(r.content);

    # wsdl = "https://pasb-dev-uwa-iws.oracleindustry.com/ouaf/webservices/CM-MEAUSREMENTTYPE?WSDL"
    # session = Session()
    # session.auth = HTTPBasicAuth("RFID_INTEGRATION", "Rfid_1nt")

    # client = Client(wsdl, transport=Transport(session=session),
    #                 settings=Settings(strict=False, raw_response=True))

    # response = client.service.ExtractMeasurementType()
    # response_xml = response.content
    # # print(response_xml)
    # middleware_response_json = json.loads(
    #     json.dumps(xmltodict.parse(response_xml)))
    # return middleware_response_json['env:Envelope']['env:Body']['ouaf:ExtractMeasurementType']['ouaf:results']
