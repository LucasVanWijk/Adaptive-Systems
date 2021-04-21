f_rain = lambda cloudy, rain : 0.1*(0 + cloudy) + 0.9*(-2 + rain)
f_cloudy = lambda sunny, cloudy, rain : 0.3*(3+sunny) + 0.5*(0 + cloudy) + 0.2*(-2 + rain)
f_sunny = lambda sunny, cloudy, meteor : 0.6*(3+sunny) + 0.3*(0 + cloudy) + 0.1*(-10 + meteor)
meteor = 0

rain = f_rain(0, 0)
cloudy = f_cloudy(0,0,0)
sunny = f_sunny(0,0,0)
for i in range(2):
    print(i)
    print(f"rain = {rain}")
    print(f"cloudy = {cloudy}")
    print(f"sunny = {sunny}")

    rain = f_rain(cloudy, rain)
    cloudy = f_cloudy(sunny,cloudy,rain)
    sunny = f_sunny(sunny,cloudy,0)

