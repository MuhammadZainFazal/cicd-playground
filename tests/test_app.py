import pytest

from app.main import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
    assert "Hello" in res.get_json()["message"]


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}


def test_calc_add(client):
    res = client.get("/calc/add?a=2&b=3")
    assert res.get_json()["result"] == 5


def test_calc_divide_by_zero(client):
    assert client.get("/calc/divide?a=1&b=0").status_code == 400


def test_calc_bad_input(client):
    assert client.get("/calc/add?a=x&b=1").status_code == 400


def test_calc_unknown_op(client):
    assert client.get("/calc/power?a=1&b=2").status_code == 404
