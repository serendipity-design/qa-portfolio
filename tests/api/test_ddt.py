import yaml,pytest
case = yaml.safe_load(open("data/api_cases.yaml",encoding="utf-8"))

@pytest.mark.parametrize("case",case,ids=[i["name"] for i in case])
def test_from_yaml(case,http_client):
    r = http_client.request(case["method"], case["path"],
                        json=case.get("body"), params=case.get("params"))

    assert r.status_code == case["expected_status"]