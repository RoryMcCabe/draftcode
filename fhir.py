# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 19:42:13 2021

@author: McCabeR
"""

import sys
sys.path.append("C:\\Users\\McCabeR\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages")

from fhir.resources.organization import Organization
from fhir.resources.address import Address

data = {
    "id": "f001",
    "active": True,
    "name": "Acme Corporation",
    "address": [{"country": "Switzerland"}]
}

print(data)
import pandas as pd
df = pd.DataFrame(data)
print(df)

df2 = pd.read_json('C:\\Users\\McCabeR\\fhir\\Aaron697_Brekke496_2fa15bc7-8866-461a-9000-f739e425860a.json')
print(df2.to_string())
df3 = pd.DataFrame(df2.entry[0])
df3.head()

org = Organization(**data)
print(org.resource_type == "Organization")
print(isinstance(org.address[0], Address))
print(org.address[0].country == "Switzerland")
print(org.dict()['active'] is True)

# from fhir.model import Patient, HumanName, Identifier, CodeableConcept, Coding, uri
# returns error: no module named fhir.model

data2={
  "resourceType": "Observation",
  "id": "ekg",
  "text": {
    "status": "generated",
    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: ekg</p><p><b>status</b>: final</p><p><b>category</b>: Procedure <span>(Details : {http://terminology.hl7.org/CodeSystem/observation-category code 'procedure' = 'Procedure', given as 'Procedure'})</span></p><p><b>code</b>: MDC_ECG_ELEC_POTL <span>(Details : {urn:oid:2.16.840.1.113883.6.24 code '131328' = '131328', given as 'MDC_ECG_ELEC_POTL'})</span></p><p><b>subject</b>: <a>P. van de Heuvel</a></p><p><b>effective</b>: 19/02/2015 9:30:35 AM</p><p><b>performer</b>: <a>A. Langeveld</a></p><p><b>device</b>: 12 lead EKG Device Metric</p><blockquote><p><b>component</b></p><p><b>code</b>: MDC_ECG_ELEC_POTL_I <span>(Details : {urn:oid:2.16.840.1.113883.6.24 code '131329' = '131329', given as 'MDC_ECG_ELEC_POTL_I'})</span></p><p><b>value</b>: Origin: (system = '[not stated]' code null = 'null'), Period: 10, Factor: 1.612, Lower: -3300, Upper: 3300, Dimensions: 1, Data: 2041 2043 2037 2047 2060 2062 2051 2023 2014 2027 2034 2033 2040 2047 2047 2053 2058 2064 2059 2063 2061 2052 2053 2038 1966 1885 1884 2009 2129 2166 2137 2102 2086 2077 2067 2067 2060 2059 2062 2062 2060 2057 2045 2047 2057 2054 2042 2029 2027 2018 2007 1995 2001 2012 2024 2039 2068 2092 2111 2125 2131 2148 2137 2138 2128 2128 2115 2099 2097 2096 2101 2101 2091 2073 2076 2077 2084 2081 2088 2092 2070 2069 2074 2077 2075 2068 2064 2060 2062 2074 2075 2074 2075 2063 2058 2058 2064 2064 2070 2074 2067 2060 2062 2063 2061 2059 2048 2052 2049 2048 2051 2059 2059 2066 2077 2073</p></blockquote><blockquote><p><b>component</b></p><p><b>code</b>: MDC_ECG_ELEC_POTL_II <span>(Details : {urn:oid:2.16.840.1.113883.6.24 code '131330' = '131330', given as 'MDC_ECG_ELEC_POTL_II'})</span></p><p><b>value</b>: Origin: (system = '[not stated]' code null = 'null'), Period: 10, Factor: 1.612, Lower: -3300, Upper: 3300, Dimensions: 1, Data: 2041 2043 2037 2047 2060 2062 2051 2023 2014 2027 2034 2033 2040 2047 2047 2053 2058 2064 2059 2063 2061 2052 2053 2038 1966 1885 1884 2009 2129 2166 2137 2102 2086 2077 2067 2067 2060 2059 2062 2062 2060 2057 2045 2047 2057 2054 2042 2029 2027 2018 2007 1995 2001 2012 2024 2039 2068 2092 2111 2125 2131 2148 2137 2138 2128 2128 2115 2099 2097 2096 2101 2101 2091 2073 2076 2077 2084 2081 2088 2092 2070 2069 2074 2077 2075 2068 2064 2060 2062 2074 2075 2074 2075 2063 2058 2058 2064 2064 2070 2074 2067 2060 2062 2063 2061 2059 2048 2052 2049 2048 2051 2059 2059 2066 2077 2073</p></blockquote><blockquote><p><b>component</b></p><p><b>code</b>: MDC_ECG_ELEC_POTL_III <span>(Details : {urn:oid:2.16.840.1.113883.6.24 code '131389' = '131389', given as 'MDC_ECG_ELEC_POTL_III'})</span></p><p><b>value</b>: Origin: (system = '[not stated]' code null = 'null'), Period: 10, Factor: 1.612, Lower: -3300, Upper: 3300, Dimensions: 1, Data: 2041 2043 2037 2047 2060 2062 2051 2023 2014 2027 2034 2033 2040 2047 2047 2053 2058 2064 2059 2063 2061 2052 2053 2038 1966 1885 1884 2009 2129 2166 2137 2102 2086 2077 2067 2067 2060 2059 2062 2062 2060 2057 2045 2047 2057 2054 2042 2029 2027 2018 2007 1995 2001 2012 2024 2039 2068 2092 2111 2125 2131 2148 2137 2138 2128 2128 2115 2099 2097 2096 2101 2101 2091 2073 2076 2077 2084 2081 2088 2092 2070 2069 2074 2077 2075 2068 2064 2060 2062 2074 2075 2074 2075 2063 2058 2058 2064 2064 2070 2074 2067 2060 2062 2063 2061 2059 2048 2052 2049 2048 2051 2059 2059 2066 2077 2073</p></blockquote></div>"
  },
  "status": "final",
  "category": [
    {
      "coding": [
        {
          "system": "http://terminology.hl7.org/CodeSystem/observation-category",
          "code": "procedure",
          "display": "Procedure"
        }
      ]
    }
  ],
  "code": {
    "coding": [
      {
        "system": "urn:oid:2.16.840.1.113883.6.24",
        "code": "131328",
        "display": "MDC_ECG_ELEC_POTL"
      }
    ]
  },
  "subject": {
    "reference": "Patient/f001",
    "display": "P. van de Heuvel"
  },
  "effectiveDateTime": "2015-02-19T09:30:35+01:00",
  "performer": [
    {
      "reference": "Practitioner/f005",
      "display": "A. Langeveld"
    }
  ],
  "device": {
    "display": "12 lead EKG Device Metric"
  },
  "component": [
    {
      "code": {
        "coding": [
          {
            "system": "urn:oid:2.16.840.1.113883.6.24",
            "code": "131329",
            "display": "MDC_ECG_ELEC_POTL_I"
          }
        ]
      },
      "valueSampledData": {
        "origin": {
          "value": 2048
        },
        "period": 10,
        "factor": 1.612,
        "lowerLimit": -3300,
        "upperLimit": 3300,
        "dimensions": 1,
        "data": "2041 2043 2037 2047 2060 2062 2051 2023 2014 2027 2034 2033 2040 2047 2047 2053 2058 2064 2059 2063 2061 2052 2053 2038 1966 1885 1884 2009 2129 2166 2137 2102 2086 2077 2067 2067 2060 2059 2062 2062 2060 2057 2045 2047 2057 2054 2042 2029 2027 2018 2007 1995 2001 2012 2024 2039 2068 2092 2111 2125 2131 2148 2137 2138 2128 2128 2115 2099 2097 2096 2101 2101 2091 2073 2076 2077 2084 2081 2088 2092 2070 2069 2074 2077 2075 2068 2064 2060 2062 2074 2075 2074 2075 2063 2058 2058 2064 2064 2070 2074 2067 2060 2062 2063 2061 2059 2048 2052 2049 2048 2051 2059 2059 2066 2077 2073"
      }
    },
    {
      "code": {
        "coding": [
          {
            "system": "urn:oid:2.16.840.1.113883.6.24",
            "code": "131330",
            "display": "MDC_ECG_ELEC_POTL_II"
          }
        ]
      },
      "valueSampledData": {
        "origin": {
          "value": 2048
        },
        "period": 10,
        "factor": 1.612,
        "lowerLimit": -3300,
        "upperLimit": 3300,
        "dimensions": 1,
        "data": "2041 2043 2037 2047 2060 2062 2051 2023 2014 2027 2034 2033 2040 2047 2047 2053 2058 2064 2059 2063 2061 2052 2053 2038 1966 1885 1884 2009 2129 2166 2137 2102 2086 2077 2067 2067 2060 2059 2062 2062 2060 2057 2045 2047 2057 2054 2042 2029 2027 2018 2007 1995 2001 2012 2024 2039 2068 2092 2111 2125 2131 2148 2137 2138 2128 2128 2115 2099 2097 2096 2101 2101 2091 2073 2076 2077 2084 2081 2088 2092 2070 2069 2074 2077 2075 2068 2064 2060 2062 2074 2075 2074 2075 2063 2058 2058 2064 2064 2070 2074 2067 2060 2062 2063 2061 2059 2048 2052 2049 2048 2051 2059 2059 2066 2077 2073"
      }
    },
    {
      "code": {
        "coding": [
          {
            "system": "urn:oid:2.16.840.1.113883.6.24",
            "code": "131389",
            "display": "MDC_ECG_ELEC_POTL_III"
          }
        ]
      },
      "valueSampledData": {
        "origin": {
          "value": 2048
        },
        "period": 10,
        "factor": 1.612,
        "lowerLimit": -3300,
        "upperLimit": 3300,
        "dimensions": 1,
        "data": "2041 2043 2037 2047 2060 2062 2051 2023 2014 2027 2034 2033 2040 2047 2047 2053 2058 2064 2059 2063 2061 2052 2053 2038 1966 1885 1884 2009 2129 2166 2137 2102 2086 2077 2067 2067 2060 2059 2062 2062 2060 2057 2045 2047 2057 2054 2042 2029 2027 2018 2007 1995 2001 2012 2024 2039 2068 2092 2111 2125 2131 2148 2137 2138 2128 2128 2115 2099 2097 2096 2101 2101 2091 2073 2076 2077 2084 2081 2088 2092 2070 2069 2074 2077 2075 2068 2064 2060 2062 2074 2075 2074 2075 2063 2058 2058 2064 2064 2070 2074 2067 2060 2062 2063 2061 2059 2048 2052 2049 2048 2051 2059 2059 2066 2077 2073"
      }
    }
  ]
}

from fhir.resources.observation import Observation

obs = Observation(**data2)
print(obs.resource_type == "Observation")
print(obs.status == "final")
print(obs.dict()['id'] == "ekg")

####

import fhiry
# ok
import fhiry.parallel as fp
# returns error: no module ... not a package
df = fp.process('c:/users/mccaber/fhir')
print(df.info())

fhiry.Fhiry.process_list('c:/users/mccaber/fhir','Aaron697_Brekke496_2fa15bc7-8866-461a-9000-f739e425860a.json')
# returns []

df = fp.ndjson('c:/users/mccaber/fhir')
print(df.info())
print(df.columns)

####

dir(fhiry)
from inspect import getmembers, isfunction
print(getmembers(fhiry.__builtins__, isfunction))
# []
#fhiry.Fhiry.process_list()
#fhiry.Fhirndjson.process_list()

####

import json

import fhirclient.models.patient as p
with open('C:\\Users\\McCabeR\\fhir\\Aaron697_Brekke496_2fa15bc7-8866-461a-9000-f739e425860a.json', 'r') as h:
     pjs = json.load(h)
patient = p.Patient(pjs)
# error resource type bundle
patient.name[0].given

import fhirclient.models.bundle as b
with open('C:\\Users\\McCabeR\\fhir\\Aaron697_Brekke496_2fa15bc7-8866-461a-9000-f739e425860a.json', 'r') as h:
    js = json.load(h)
bundle = b.Bundle(js)
# error FHIRValidationError
bundle.entry
for entry in bundle.entry:
    print(entry.resource)

resources = []
if bundle.entry is not None:
    for entry in bundle.entry:
        resources.append(entry.resource)
        
from fhirclient import client
settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://fhir-open-api-dstu2.smarthealthit.org'
}
smart = client.FHIRClient(settings=settings)

#import fhirclient.models.patient as p
patient = p.Patient.read('hca-pat-1', smart.server)
# error failed to establish conn +- vpn

#patient.birthDate.isostring
#smart.human_name(patient.name[0])

smart = client.FHIRClient(settings=settings)
import fhirclient.models.procedure as pr
search = pr.Procedure.where(struct={'subject': 'hca-pat-1', 'status': 'completed'})
procedures = search.perform_resources(smart.server)
# error failed to establish conn +- vpn

#for procedure in procedures: procedure.as_json()
#bundle = search.perform(smart.server)

"""

Summary

- restful API calls not possible in my PC work environment
- Fhir manages to read in records
- Fhiry has installation issues
- Fhirclient gives errors

Also looked at fhir-parser / client-py from smart-on-fhir
and fhir table export (FTE)
and fhirExtinguisher

Spark Bunsen seems promising if I had more time

"""