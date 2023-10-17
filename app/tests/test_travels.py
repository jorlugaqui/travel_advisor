from . import client

def test_create_item():
    response = client.post(
        "/travels/",
        json={"query": "foobar"},
    )
    assert response.status_code == 200
    assert response.json()["advise"]["query"] == "foobar"