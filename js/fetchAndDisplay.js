function appendData(data) {
    var mainContainer = document.getElementById("myData");
    var keyWordCount = 1

    for (var acry in data) {

        if (acry.length >=3){
            console.log("Item: ",acry)

            var div = document.createElement("div");
            let keywordBold = ""

            for (i=0;i<data[acry].length;i++){
                for (j=0;j<data[acry][i].length;j++){
                    if (data[acry][i][j] === data[acry][i][j].toUpperCase() || j === 0){
                        keywordBold = keywordBold + "<b>" +data[acry][i][j] + "</b>"
                    } else{
                        keywordBold = keywordBold + data[acry][i][j]
                    }
                }

                var rowContainer = document.createElement("tr");

                var rowHead = document.createElement("th")
                rowHead.setAttribute("scope","row")
                rowHead.textContent = keyWordCount
                keyWordCount+=1

                var rowData1 = document.createElement("td")
                var rowData2 = document.createElement("td")
                rowData1.innerHTML = acry
                rowData2.innerHTML = keywordBold

                rowContainer.appendChild(rowHead)
                rowContainer.appendChild(rowData1)
                rowContainer.appendChild(rowData2)

                
                mainContainer.appendChild(rowContainer);
            }
        }
    }
}


    fetch('output.json').then(function (response) {

        return response.json();

    }) .then(function (data) {

        appendData(data);

    }) .catch(function (err) {

        console.log(err);

    });


