from utils.http_client import HttpClient
import sys
def test_import_works():
    c = HttpClient("https://jsonplaceholder.typicode.com")
    assert c.base_url == "https://jsonplaceholder.typicode.com"
    print("PYPATH_OK", rootdir_in_path=[p for p in sys.path if "qa-portfolio" in p])
