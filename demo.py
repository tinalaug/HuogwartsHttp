import requests


class TestDemo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.text)
        print(r.content)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload={
            "level":1,
            "name":"tina"
        }
        r=requests.get("https://httpbin.testing-studio.com/get",params=payload)
        print(r.text)
        assert r.status_code ==200
    #模拟用户名密码
    def test_post_from(self):
        payload = {
            "level": 1,
            "name": "tina"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_header1(self):
        r = requests.get("https://httpbin.testing-studio.com/get", headers={"h":"header"})
        print(r.text)
        # print(r.content)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200

    #json请求
    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "tina"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

