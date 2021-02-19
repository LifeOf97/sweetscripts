// Author: Kelvin Mayowa Ayeni (KMA).
// Github: d-kma.
// Twitter: @DBlackerMan.
// Date: February 19, 2021.
// formula: https://www.techspot.com/news/68482-quickly-convert-between-storage-size-units-kb-mb.html
// Credits: https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size

function humanize(value, decimal=2, memory=1024.0, spc=false) {
    // funtion to convert any size to human readable memory size format
    /*
    value:
    the value to convert, this should be type int or float.

    decimal:
    The number of decimal places the converted size should be returned in.
    default is 2 decimal place.

    memory:
    default memory size to use. Gigabyte: 1000.0 or Gibibyte: 1024.0.
    default is Gibibyte: 1024.0 look up "formula" url @ top comments.

    spc:
    should there be spacing between the converted size and its unit
    when outputting the converted size?. True/False.
    default is False: no spacing.
    */
   const units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];

   for (let unit = 0; unit < units.length; unit++) {
       if (value < memory) {
           if (spc) return value.toString().slice(0, value.toString().indexOf('.')+3) + " " + units[unit];
           else return value.toString().slice(0, value.toString().indexOf('.')+3) + units[unit];
       }
       // divide again if value is still greater than memory.
       else value /= memory;
   }
}

console.log(humanize(67_003_324_746))