#Temperature Classifier: Freezing, Very Cold, Cold, Moderate, Hot, Very Hot

temperature = int(input("input temperature number:"))

if temperature < 0:
    print('Very Cold')
elif temperature < 10:
    print('Cold')
elif temperature < 20:
    print('Moderate')
elif temperature < 30:
    print('Hot')
else:
    print('Very Hot')