import Lab2.bmi as bmi

print ("Test_bmi")

def test_bmi_normal_weight():
    inputWeight = 57
    inputHeight = 1.73
    result = bmi.calculate_bmi(inputHeight, inputWeight)
    assert(result == 0)
def test_bmi_over_weight():
    inputWeight = 110
    inputHeight = 1.73
    result = bmi.calculate_bmi(inputHeight, inputWeight)
    assert (result == 1)
def test_bmi_under_weight():
    inputWeight = 20
    inputHeight = 1.73
    result = bmi.calculate_bmi(inputHeight, inputWeight)
    assert (result == -1)