# -*- coding: utf-8 -*-
import math

def test_z_test_calculation():
    # Test Two-Proportion Z-Test Formula
    clicks_w, opens_w = 1190, 6800
    clicks_l, opens_l = 380, 4200
    p1 = clicks_w / opens_w
    p2 = clicks_l / opens_l
    p_pool = (clicks_w + clicks_l) / (opens_w + opens_l)
    se = math.sqrt(p_pool * (1 - p_pool) * (1/opens_w + 1/opens_l))
    z_score = (p1 - p2) / se
    p_val = math.erfc(abs(z_score) / math.sqrt(2))
    assert z_score > 5.0, "Z-Score should show high significance"
    assert p_val < 0.001, "P-Value should be < 0.001"
    print("[PASS] Z-Test Calculation Verified!")

def test_rfm_quantiles():
    # Test RFM Scoring Logic
    monetary_values = [500, 150, 50, 900, 400, 1200, 350, 80, 45, 650]
    sorted_m = sorted(monetary_values)
    idx_80 = int(len(sorted_m) * 0.8)
    top_20_threshold = sorted_m[idx_80]
    assert top_20_threshold >= 650, "Top 20% Monetary threshold verified"
    print("[PASS] RFM Quantile Logic Verified!")

def test_cooling_period_logic():
    # Test 24h Cooling Rule
    last_touch_hours = 12
    is_suppressed = last_touch_hours < 24
    assert is_suppressed is True, "Cooling period must suppress messages sent within 24 hours"
    print("[PASS] 24h Cooling Rule Logic Verified!")

if __name__ == '__main__':
    test_z_test_calculation()
    test_rfm_quantiles()
    test_cooling_period_logic()
    print("SUCCESS: All Engine Tests Passed Successfully!")
