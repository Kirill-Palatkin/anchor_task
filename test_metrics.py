
import math
from metrics import compute_metrics

def test_valid_values():
    res = compute_metrics(1000, 50, 25)  # CTR=0.05, CPC=0.5
    assert res["status"] == "ok"
    assert res["ctr"] is not None and math.isclose(res["ctr"], 0.05, rel_tol=1e-12, abs_tol=0.0)
    assert res["cpc"] is not None and math.isclose(res["cpc"], 0.5, rel_tol=1e-12, abs_tol=0.0)

def test_zeros_all():
    res = compute_metrics(0, 0, 0)  # деление на ноль для CPC, impressions=0 для CTR
    assert res["status"] == "no_answer"
    assert res["ctr"] is None
    assert res["cpc"] is None

def test_negative_or_garbage():
    res = compute_metrics(-10, 5, 20)
    assert res["status"] == "no_answer"
    assert res["ctr"] is None and res["cpc"] is None
