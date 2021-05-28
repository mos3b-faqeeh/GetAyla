import json
from haralyzer import HarParser, HarPage
import requests


def har_parser(file):
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
                    har_headers = har["request"]["headers"]
                    for head in har_headers:
                        if head["name"].startswith(":"):
                            headers[head["name"][1:]] = head["value"]
                        else:
                            headers[head["name"]] = head["value"]
                    response = requests.get(url, headers=headers).json()
                    tmp[f"url_{count}"] = response
                    print("***********************", "\n", "*************************")
                    print("***********************", "\n", "*************************")

                    print("***********************", "\n", "*************************")

                    print("***********************", "\n", "*************************")

                    print(har["request"]["url"], "\n")

                    print(tmp)

                    results.append(tmp)
                    count += 1
                    print("\n")
                    print("\n")
                    print("\n")
                    print("\n")
                    print("\n")
                    print("\n")
                    print("\n")
                    print("\n")

            return json.dumps(results)
    except Exception as e:
        print(e)



file = "NewDataJinkstattoo.har"
print(har_parser(file))
