const fs = require("fs")

const outputPath = "/Users/sanjitkumar/personal_projects/keyWordsAcronymGenerator/output.json"
const dataBuffer = fs.readFileSync(outputPath)
const jsonData = dataBuffer.toString()
const inputObj = JSON.parse(jsonData)
var json = undefined

for (var acry in inputObj){

    if (acry.length>=3){
        // console.log("Item: ",acry)

        for (i=0;i<inputObj[acry].length;i++){
            let keywordBold = ""
            for (j=0;j<inputObj[acry][i].length;j++){

                if (inputObj[acry][i][j] === inputObj[acry][i][j].toUpperCase() || j === 0){
                    keywordBold = keywordBold + "<b>" +inputObj[acry][i][j] + "</b>"
                } else{
                    keywordBold = keywordBold + inputObj[acry][i][j]
                }
            }
            var outpuObj = inputObj[acry][i]
            var outpuObj = {
                name,
                displayName: keywordBold
            }
            json[acry][i] = outpuObj
        }
    } 
}

var alteredData = JSON.stringify(outpuObj)
fs.writeFileSync("outputMadeBoldJSON.json",alteredData)