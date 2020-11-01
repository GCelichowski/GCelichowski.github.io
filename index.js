var postUrl = "https://ycm1r4fi1e.execute-api.us-east-1.amazonaws.com/default/SezzleCalculator?callback=?";
var getUrl = "https://ycm1r4fi1e.execute-api.us-east-1.amazonaws.com/default/retrievecalculations?callback=?";
function postCalculation(){
    var calculation = {
        "calculation" : document.getElementById("input")
    };

    $.ajax({
        url: postUrl,
        crossDomain : true,
        contentType : "application/json",
        dataType: 'json',
        data : calculation,
        type: 'POST',
        success: function(callback) {
            console.log( 'success' );
            display(callback.data)
        }
    });
}
    function display(calculations){
        var html = "";
        calculations.array.forEach(element => {
            html += "<tr><td class='calcInfo'><div class = 'calcBox'>" + JSON.stringify(element, undefined, 2) + "</div></td>";
        });
        document.getElementById("calculations").innerHTML = html;
    }

    function getCalculations() {
        $.ajax({
            url: getUrl,
            crossDomain : true,
            contentType : "application/json",
            dataType: 'json',
            type: 'GET',
            complete: function(callback) {
                console.log( 'success' );
                display(callback.data)
            }
        });
    }