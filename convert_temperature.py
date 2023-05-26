def convertTemperature(self, celsius):
    tempKel = celsius + 273.15
    tempFah = celsius * 1.80 + 32
    ans = [tempKel, tempFah]
    return ans