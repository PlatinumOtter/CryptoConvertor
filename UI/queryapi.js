function getamount() {
    var coin1 = document.getElementById("coin1");
    var coin1rate = 1;
    var coin2 = document.getElementById("coin2");
    var coin2rate = 1;
    var exchange = document.getElementById("exchange");
    var starting = document.getElementById("amount");

    $.ajax({
        url: "localhost:5000/api/v1.0/" + exchange + "?coin=" + coin1,
        success: function(data) {
            var obj = JSON.parse(data)
            coin1rate = obj.rate
        }
    })
    $.ajax({
        url: "localhost:5000/api/v1.0/" + exchange + "?coin=" + coin2,
        success: function(data) {
            var obj = JSON.parse(data)
            coin2rate = obj.rate
        }
    })

    var result = starting * coin1rate / coin2rate

    document.getElementById("result").innerHTML = result
}