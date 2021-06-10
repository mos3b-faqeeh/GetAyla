import json
from haralyzer import HarParser, HarPage
import requests




def har_parser_response(file):
    with open(file, 'r') as f:
        har_parser = HarParser(json.loads(f.read()))
    results = []
    try:
        if har_parser:
            count = 0
            for har in har_parser.har_data['entries']:
                tmp = {}
                url = har["request"]["url"]
                headers = {}
                if "https://www.instagram.com/graphql/query/" in url:
                    response = har["response"]["content"]["text"]
                    tmp[f"url_{count}"] = json.loads(response)
                    results.append(tmp)
                    count += 1
            return json.dumps(results)
    except Exception as e:
        print(e)


file = "NewDataJinkstattoo.har"
print(har_parser_response(file))