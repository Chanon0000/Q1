import unittest

def determine_health_level(FBS, BP):
    if FBS < 100 and BP <= 120:
        return "General (สีขาว)"
    if 100 <= FBS <= 125 and 120 < BP <= 139:
        return "Risk (สีเขียว)"
    
    if 125 < FBS <= 154 and 140 <= BP <= 159:
        return "High Risk 1 (สีเหลือง)"
    
    if 154 < FBS <= 182 and 160 <= BP <= 179:
        return "High Risk 2 (สีส้ม)"
    
    if FBS >= 183 and BP > 179:
        return "High Risk 3 (สีทอง)"
    
    if FBS >= 183 and BP > 180:
        return "Critical Condition (สีดำ)"
    
    return "ข้อมูลไม่ตรงกับเกณฑ์"

class TestHealthLevel(unittest.TestCase):

    def test_general(self):
        self.assertEqual(determine_health_level(95, 110), "General (สีขาว)")

    def test_risk(self):
        self.assertEqual(determine_health_level(120, 130), "Risk (สีเขียว)")

    def test_high_risk_1(self):
        self.assertEqual(determine_health_level(130, 150), "High Risk 1 (สีเหลือง)")

    def test_high_risk_2(self):
        self.assertEqual(determine_health_level(160, 170), "High Risk 2 (สีส้ม)")

    def test_high_risk_3(self):
        self.assertEqual(determine_health_level(190, 180), "High Risk 3 (สีทอง)")

    def test_critical_condition(self):
        self.assertEqual(determine_health_level(190, 185), "Critical Condition (สีดำ)")

    def test_invalid_data(self):
        self.assertEqual(determine_health_level(100, 120), "ข้อมูลไม่ตรงกับเกณฑ์")


if __name__ == "__main__":
    unittest.main(exit=False)

    FBS = 95  # Example blood sugar level (mg/dl)
    BP = 110  # Example blood pressure (mmHg)
    
    health_level = determine_health_level(FBS, BP)
    print(f"\nระดับผู้ป่วย: {health_level}")
