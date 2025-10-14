import json
import os
import socket
import threading
import time

import pytest
import requests

from wsim.__main__ import app, load_gdata


@pytest.fixture(scope="session")
def flask_server():
    """Starts the Flask server in a background thread."""
    host = "127.0.0.1"
    port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port.bind((host, 0))
    port_num = port.getsockname()[1]
    port.close()

    server = threading.Thread(
        target=app.run, kwargs={"host": host, "port": port_num}
    )
    server.daemon = True
    server.start()
    time.sleep(1)
    yield f"http://{host}:{port_num}"


def test_get_entities(flask_server):
    """Tests the /wsim/v1/entities endpoint."""
    response = requests.get(f"{flask_server}/wsim/v1/entities")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "entities" in data
    assert "e1" in data["entities"]


def test_get_locations(flask_server):
    """Tests the /wsim/v1/locations endpoint."""
    response = requests.get(f"{flask_server}/wsim/v1/locations")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "locations" in data
    assert "l1" in data["locations"]


def test_get_zones(flask_server):
    """Tests the /wsim/v1/zones endpoint."""
    response = requests.get(f"{flask_server}/wsim/v1/zones")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "zones" in data
    assert "z1" in data["zones"]


def test_get_entityinfo(flask_server):
    """Tests the /wsim/v1/entityInfo endpoint."""
    response = requests.get(f"{flask_server}/wsim/v1/entityInfo")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "entityInfo" in data
    assert "Eastern Cottontail" in data["entityInfo"]
