import statistics as st
print("This program can calculate the mean, median, mode, minimum and maximum of a given set of temperatures. \nEnter a minimum of 2 temperatures and a maximum of 100")
temperatureList=[]
isCelsius=""
while isCelsius=="":
    measurementUnit = input("Please enter C to select Celsius or F to select Fahrenheit as your unit of measurement: ").lower()
    if measurementUnit=="c":
        isCelsius=True
    elif measurementUnit=="f":
        isCelsius=False
inputtingValues=True
while inputtingValues:
    temperature=input("Temperature: ")
    if temperature=="n":
        if len(temperatureList)<2:
            print("Please enter more values (Minimum of 2)")
        else:
            inputtingValues=False
    else:
        try:
            temperatureList.append(float(temperature))
        except ValueError:
            print("Error, not a valid number")
print(temperatureList)
if isCelsius:
    celsiusMean=st.mean(temperatureList)
    fahrenheitMean=(celsiusMean*1.8)+32
    celsiusMode=st.mode(temperatureList)
    fahrenheitMode=(celsiusMode*1.8)+32
    celsiusMedian=st.median(temperatureList)
    fahrenheitMedian=(celsiusMedian*1.8)+32
else:
    fahrenheitMean=st.mean(temperatureList)
    celsiusMean=(fahrenheitMean-32)/1.8
    fahrenheitMode=st.mode(temperatureList)
    celsiusMode=(fahrenheitMode-32)/1.8
    fahrenheitMedian=st.median(temperatureList)
    celsiusMedian=(fahrenheitMedian-32)/1.8
print("Mode: {}° Celsius, {}° Fahrenheit \nMedian: {}° Celsius, {}° Fahrenheit \nMean: {}° Celsius, {}° Fahrenheit".format(celsiusMode, fahrenheitMode, celsiusMedian,fahrenheitMedian,celsiusMean,fahrenheitMean))
