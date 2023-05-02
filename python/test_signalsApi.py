from fastapi.testclient import TestClient
from signalsApi import app



client = TestClient(app)

def test_read_rout():
    response = client.get("/signals/Ac_lNpon_TtuxVXFCGq")
    assert response.status_code == 200
    assert response.json() == {"node_id":"Ac_lNpon_TtuxVXFCGq", "sampling_interval_ms": 500, "deadband_value": 0, "deadband_type": "", "active": 1, "keywords": "PS"}



 