function formatNumber(value, decimal = 2) {
    // parameter value should be type number
    var seperatedValues = []
    var seperatedString = ""
    var afterDecimal =  ""

    // then convert value to string to apply string methods
    value = String(value)

    // does value have a decimal point?
    if (value.includes('.')) {
        // split by '.', then get value after the decimal 'first'.
        afterDecimal = '.' + value.split('.')[1].slice(0, decimal)
        // and then value should now = value before the decimal
        value = value.split('.')[0]
    }
    // if value has no decimal leave as is.
    else value = value

    console.log("Value: " + value)
    console.log("After Decimal: " + afterDecimal)
    
    // is the value over a thousand?, is it greater than 3 in length?
    if (value.length > 3) {
        // then turn value into array for better indexing
        value = value.split('')
        console.log("Value as list: " + value)
    
        while (value.length > 3) {
            // splice values in three's, from the 3rd last to the last value and
            // insert the values into the seperatedValues array using the unshift
            // method to retain the array index positions.
            seperatedValues.unshift(value.splice(-3, ))
        }
        console.log("seperatedValues: "+seperatedValues)

        // loop over the values in the seperatedValues array and concatenate to each order
        // removing the ',' commas inserted and assign it to seperatedString
        for (const value in seperatedValues) {
            seperatedString += seperatedValues[value].toString().replaceAll(',','') + ','
        }
        console.log("seperatedString: "+seperatedString)

        // set and return the formatted value
        value = value.toString().replaceAll(',', '')
                + ','
                + seperatedString.slice(0, seperatedString.lastIndexOf(','))
                + afterDecimal

        console.log("Value: "+value)
    }

    // if the value is less than a thousand, less than 3 in length?
    // and has a decimal point.
    else {
        console.log("Value is: " + value + afterDecimal.slice(0, decimal))
    }
}