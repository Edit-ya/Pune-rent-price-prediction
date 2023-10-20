function getParkingValue() {
  var uiParking = document.getElementsByName("uiParking");
  for (var i in uiParking) {
    if (uiParking[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for (var i in uiBHK) {
    if (uiBHK[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

var propertyAgeMapping = {
  '0 to 1 Year Old': 0,
  '1 to 5 Year Old': 1,
  '5 to 10 Year Old': 2,
  '10+ Year Old': 3
};

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var area = document.getElementById("uiSqft");
  var bedroom = getBHKValue();
  var parking = getParkingValue(); // Corrected function name
  var address = document.getElementById("uiLocations");
  var propertyAgeSelect = document.getElementById("uiPropertyage");
  var facing = document.getElementById("uiFacing");
  var furnishing = document.getElementById("uiFurnishing");
  var available_for = document.getElementById("uiAvailable");
  var estPrice = document.getElementById("uiEstimatedPrice");

  // Get the selected property age value
  var selectedPropertyAge = propertyAgeSelect.value;

  // Map the selected property age to its encoded value
  var encodedPropertyAge = propertyAgeMapping[selectedPropertyAge];

  //var url = "http://127.0.0.1:5000/get_estimated_rent"; //  //Use this if you are NOT using nginx
  var url = "/api/get_estimated_rent"; // Use this if  you are using nginx.

  $.post(url, {
    address: address.value,
    
    bedroom: bedroom,
    area: parseFloat(area.value),
    parking: parking,
    furnishing: furnishing.value,
    available_for: available_for.value,
    facing: facing.value,
    
    propertyage_encoded: encodedPropertyAge
      
  }, function(data, status) {
    console.log(data.estimated_price);
    estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Thousand</h2>";
    console.log(status);
  });
}

function onPageLoad() {
  console.log("document loaded");
  //var url = "http://127.0.0.1:5000/get_all_names"; //  // Use this if you are NOT using nginx 
  var url = "/api/get_all_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards    
    
  $.get(url, function(data, status) {
    console.log("got response for get_all_names request");
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uiLocations");
      $('#uiLocations').empty();
      for (var i in locations) {
        var opt = new Option(locations[i]);
        $('#uiLocations').append(opt);
      }
    }
  });
}

window.onload = onPageLoad;
