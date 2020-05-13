const fs = require("fs")

const outputPath = "/Users/sanjitkumar/personal_projects/keyWordsAcronymGenerator/output.json"
const dataBuffer = fs.readFileSync(outputPath)
const jsonData = dataBuffer.toString()
const outputObj = JSON.parse(jsonData)
var json = undefined

for (var acry in outputObj){

    if (acry.length>=3){
        // console.log("Item: ",acry)
        let keywordBold = ""

        for (i=0;i<outputObj[acry].length;i++){
            for (j=0;j<outputObj[acry][i].length;j++){

                if (outputObj[acry][i][j] === outputObj[acry][i][j].toUpperCase() || j === 0){
                    keywordBold = keywordBold + "<b>" +outputObj[acry][i][j] + "</b>"
                } else{
                    keywordBold = keywordBold + outputObj[acry][i][j]
                }
            }
            var name = outputObj[acry][i]
            var itemObj = {
                name,
                displayName: keywordBold
            }
            json[acry][i] = itemObj
        }
    } 
    // else{
    //     delete outputObj.acry
    //     console.log(outputObj[acry])
    // }
}

var alteredData = JSON.stringify(outputObj)
fs.writeFileSync("outputMadeBoldJSON.json",alteredData)