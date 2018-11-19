#Statistics library to calculate the 3 averages easily
import statistics as st
#Introductory message, explains function of program
print("This program can calculate the mean, median, mode, minimum and maximum of a given set of temperatures. \nEnter a minimum of 2 temperatures and a maximum of 100")
#Initialises an empty list that temperatures will later be appended to
temperatureList=[]
#Initialises a variable to an empty string, I will use this to create a while loop which will later set it to either True or False
#depending on whether the user is inputting temperatures in celsius or fahrenheit
isCelsius=""
#Beginning of while loop using iscelsius variable
while isCelsius=="":
    #User inputs C to select celsius and F to select fahrenheit, whatever letter they input is converted to lowercase to make
    #If statements easier to implement
    measurementUnit = input("Please enter C to select Celsius or F to select Fahrenheit as your unit of measurement: ").lower()
    #If statement determines whether user entered C to select celsius
    if measurementUnit=="c":
        #If the user entered C, the variable isCelsius is set to True and the while loop breaks
        isCelsius=True
    #If statement determines whether user entered F to select fahrenheit
    elif measurementUnit=="f":
        #If the user entered F, the isCelsius variable is set to False and the while loop breaks
        isCelsius=False
#A boolean variable is created and set to True, indicating that the user is still inputting values and allowing a while loop to continue
inputtingValues=True
#While loop will continue as long as the userInputting is True
while inputtingValues:
    #User can input temperatures as integer or float values or enter n to stop inputting values
    temperature=input("Temperature: ")
    #If statement to determine whether the user wants to stop inputting values or not
    if temperature=="n":
        #The program requires a minimum of 2 temperatures so the length of the temperatureList must be greater than 2 or the user
        #must enter more values
        if len(temperatureList)<2:
            #Error prompts user to enter more values
            print("Please enter more values (Minimum of 2)")
        #Else occurs when the user has entered a valid number of values and wants to stop inputting

        else:
            #inputtingValues is set to false, indicating that the user is no longer inputting values
            #and ending the while loop
            inputtingValues=False
    #Else occurs when user enters something other than n ie a number value that will be interpreted as a temperature or an invalid character
    else:
        #I am trying to convert the user input to a float but if it is not a number, an error will occur so exception handling
        #Will prevent the program from crashing
        try:
            #The value inputted by the user is converted to a float value and appended to the list of temperatures
            temperatureList.append(float(temperature))
        #Excepting a value error for when the data type is incorrect
        except ValueError:
            #User is told their input is invalid while loop repeats
            print("Error, not a valid number")
        #Program must be able to recieve a maximum of 100 temperatures
        if len(temperatureList)==100:
                #Prompts user that the maximum number of values has been reached and calculations will be made
                print("You have entered the maximum number of values")
                inputtingValues=False
#Outputting all values inputted by the user
print(temperatureList)
#Conversions for if user selected celsius as their unit of measurement
if isCelsius:
    #Using statistics module to calculate mean, rounds it to 1 decimal place
    celsiusMean=round(st.mean(temperatureList),1)
    #Once I have the mean in celsius, I can use the formula to convert it to fahrenheit, rounds it to 1 decimal place
    fahrenheitMean=round((celsiusMean*1.8)+32,1)
    #Using statistics module to calculate mode, rounds it to 1 decimal place
    celsiusMode=round(st.mode(temperatureList),1)
    #Once I have the mode in celsius, I can use the formula to convert it to fahrenheit, rounds it to 1 decimal place
    fahrenheitMode=round((celsiusMode*1.8)+32,1)
    #Using statistics module to calculate median, rounds it to 1 decimal place
    celsiusMedian=round(st.median(temperatureList),1)
    #Once I have the median in celsius, I can use the formula to convert it to fahrenheit, rounds it to 1 decimal place
    fahrenheitMedian=round((celsiusMedian*1.8)+32,1)
    #Calculating the maximum value in celsius, rounds it to 1 decimal place
    celsiusMax=round(max(temperatureList),1)
    #Using maximum in celsius to calculate fahrenheit value, rounds it to 1 decimal place
    fahrenheitMax=round((celsiusMax*1.8)+32,1)
    #Calculating minimum value in celsius, rounds it to 1 decimal place
    celsiusMin=round(min(temperatureList),1)
    #Using minimum value in celsius to calculate fahrenheit value, rounds to 1 decimal place
    fahrenheitMin=round((celsiusMin*1.8)+32,1)
else:
    #Using statistics module to calculate mean, rounds it to 1 decimal place
    fahrenheitMean=round(st.mean(temperatureList),1)
    #Once I have the mean in fahrenheit, I can use the formula to convert it to celsius, rounds it to 1 decimal place
    celsiusMean=round((fahrenheitMean-32)/1.8,1)
    #Using statistics module to calculate mode
    fahrenheitMode=round(st.mode(temperatureList),1)
    #Once I have the mode in fahrenheit, I can use the formula to convert it to celsius, rounds it to 1 decimal place
    celsiusMode=round((fahrenheitMode-32)/1.8,1)
    #Using statistics module to calculate median, rounds it to 1 decimal place
    fahrenheitMedian=round(st.median(temperatureList),1)
    #Once I have the median in fahrenheit, I can use the formula to convert it to celsius, rounds it to 1 decimal place
    celsiusMedian=round((fahrenheitMedian-32)/1.8,1)
    #Calclating maximum value in fahrenheit, rounds it to 1 decimal place
    fahrenheitMax=round(max(temperatureList),1)
    #Using max in fahrenheit to calculate celsius value, rounds to 1 decimal place
    celsiusMax=round((fahrenheitMax-32)/1.8,1)
    #Calculating minimum value in fahrenheit, rounds it to 1 decimal place
    fahrenheitMin=round(min(temperatureList))
    #Using minimum in fahrenheit to calculate value in celsius, rounds it to 1 decimal place
    celsiusMin=round((fahrenheitMin-32)/1.8,1)
#Outputting all values calculated in a table style format
#Underscores are the top of the table, separating the outputs from the rest of the program
print("You have entered {} temperatures".format(len(temperatureList)))
print("_"*53)
#Outputs the row of the table regarding the modal values
print("   |  Mode   |  {}° Celsius| {}° Fahrenheit  |".format(celsiusMode, fahrenheitMode))
#Outputs the row of the table regarding median values
print("   |  Median |  {}° Celsius| {}° Fahrenheit  |".format(celsiusMedian, fahrenheitMedian))
#Outputs the row of the table regarding mean values
print("   |  Mean   |  {}° Celsius| {}° Fahrenheit  |".format(celsiusMean, fahrenheitMean))
#Outputs row of the table regarding maximum values
print("   |  Max    |  {}° Celsius| {}° Fahrenheit  |".format(celsiusMax, fahrenheitMax))
#Outputs row of the table regarding minimum values
print("   |  Min    |  {}° Celsius| {}° Fahrenheit  |".format(celsiusMin, fahrenheitMin))
