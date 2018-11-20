# <p align=center>Temperature-Recording-Tool</p>
### <p align=center>Part of my unit 4 Assignment. Code can take between 2 and 100 temperatures in either celsius or fahrenheit and calculate the mean, median, minimum and maximum</p>

## <p align=center>Flowchart</p>
<img align=center src="https://github.com/olaramoni/Temperature-Recording-Tool/blob/master/Flowchart.jpg"></img>
## <p align=center>Pseudocode</p>

<p>OUTPUT Introductory message</p>
<p>SET temperatureList TO []</p>
<p>SET isCelsius TO ""</p>
<p>WHILE isCelsius EQUALS "" DO</p>
<p>    SET measurementUnit to INPUT</p>
<p>        IF measurementUnit EQUALS "C":</p>
<p>            SET isCelsius TO True</p>
<p>        IF measurementUnit EQUALS "F":</p>
<p>            SET isCelsius to False</p>
SET inputtingValues TO Temperature
WHILE inputtingValues EQUALS True DO:
    SET temperature TO input
    IF temperature EQUALS "n" THEN
        IF length(temperatureList) IS LESS THAN 2 THEN:
            OUTPUT "Please enter more values"
        ELSE
            SET inputtingValues TO false
        ENDIF
    ELSE
        APPEND temperature TO temperatureList
IF isCelsius EQUALS True THEN:
    SET celsiusMax TO max(temperatureList)
    SET fahrenheitMax TO convert celsiusMax to fahrenheit
    SET celsiusMin TO min(temperatureList)
    SET fahrenheitMin TO convert celsiusMin to fahrenheit
    SET celsiusMean TO mean(temperatureList)
    SET fahrenheitMean TO convert celsiusMean to fahrenheit
    SET celsiusMode TO mode(temperatureList)
    SET fahrenheitMode TO convert celsiusMode to fahrenheit
    SET celsiusMedian TO median(temperatureList)
    SET fahrenheitMedian TO convert celsiusMedian to fahrenheit
ELSE:
    SET fahrenheitMax TO max(temperatureList)
    SET celsiusMax TO convert fahrenheitMax to celsius
    SET fahrenheitMin TO min(temperatureList)
    SET celsiusMin TO convert fahrenheitMin to celsius
    SET fahrenheitMean TO mean(temperatureList)
    SET celsiusMean TO convert fahrenheitMean to celsius
    SET fahrenheitMode TO mode(temperatureList)
    SET celsiusMode TO convert fahrenheitMode to celcius
    SET fahrenheitMedian TO median(temperatureList)
    SET celsiusMedian TO convert fahrenheitMedian to celsius
OUTPUT fahrenheitMax
OUTPUT fahrenheitMin
OUTPUT fahrenheitMean
OUTPUT fahrenheitMedian
OUTPUT fahrenheitMode
OUTPUT celsiusMax
OUTPUT celsiusMin
OUTPUT celsiusMean
OUTPUT celsiusMedian
OUTPUT celsiusMode
</p>
