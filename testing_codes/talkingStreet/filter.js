function fillLocOptions(){

	// Following variables fetch and store current selections
	var curLocation = document.getElementById('loc-search').value;
	var curCusine = document.getElementById('cuisine-search').value;
	var curType = document.getElementById('type-search').value;

	var locations = [];
	var regexp = new RegExp(curCusine, "i");

	for (i in contents){
		if(!(locations.includes(contents[i].location)) && (contents[i].location != '' && contents[i].location != curLocation) && (regexp.test(contents[i].cuisine)) && (curType == '' || contents[i].seating == curType)){
			locations.push(contents[i].location);
		}
	}

	locations.sort();
	if (!curLocation){
		document.getElementById('loc-search').options.length = 1;
		for (i in locations){
			document.getElementById('loc-search').options[document.getElementById('loc-search').options.length] = new Option(locations[i], locations[i]);
		}
	} else {
		document.getElementById('loc-search').options[1] = document.getElementById('loc-search').options[document.getElementById('loc-search').options.selectedIndex];
		document.getElementById('loc-search').options.length = 2;
		for (i in locations){
			document.getElementById('loc-search').options[document.getElementById('loc-search').options.length] = new Option(locations[i], locations[i]);
		}
		document.getElementById('loc-search').options.selectedIndex = 1;
	}
}

function fillCuisineOptions(){

	// Following variables fetch and store current selections
	var curLocation = document.getElementById('loc-search').value;
	var curCusine = document.getElementById('cuisine-search').value;
	var curType = document.getElementById('type-search').value;

	var cuisines = [];

	for (i in contents){
		objectCuisines = contents[i].cuisine.split(',');
		for (j in objectCuisines){
			if (!(cuisines.includes(objectCuisines[j])) && (objectCuisines[j] != '' && objectCuisines[j] != curCusine) && (curLocation == '' || contents[i].location == curLocation) && (curType == '' || contents[i].seating == curType) && (contents[i].location != '')){
				cuisines.push(objectCuisines[j]);
			}
		}
	}

	cuisines.sort();
	if (!curCusine){
		document.getElementById('cuisine-search').options.length = 1;
		for (i in cuisines){
			document.getElementById('cuisine-search').options[document.getElementById('cuisine-search').options.length] = new Option(cuisines[i], cuisines[i]);
		}
	} else {
		document.getElementById('cuisine-search').options[1] = document.getElementById('cuisine-search').options[document.getElementById('cuisine-search').options.selectedIndex];
		document.getElementById('cuisine-search').options.length = 2;
		for (i in cuisines){
			document.getElementById('cuisine-search').options[document.getElementById('cuisine-search').options.length] = new Option(cuisines[i], cuisines[i]);
		}
		document.getElementById('cuisine-search').options.selectedIndex = 1;
	}

}

function fillTypeOptions(){

	// Following variables fetch and store current selections
	var curLocation = document.getElementById('loc-search').value;
	var curCusine = document.getElementById('cuisine-search').value;
	var curType = document.getElementById('type-search').value;

	var seatings = [];
	var regexp = new RegExp(curCusine, "i");

	for (i in contents){
		if(!(seatings.includes(contents[i].seating)) && (contents[i].seating != '' && contents[i].seating != curType) && (regexp.test(contents[i].cuisine)) && (curLocation == '' || contents[i].location == curLocation)){
			seatings.push(contents[i].seating);
		}
	}

	seatings.sort()
	if (!curType){
		document.getElementById('type-search').options.length = 1;
		for (i in seatings){
			document.getElementById('type-search').options[document.getElementById('type-search').options.length] = new Option(seatings[i], seatings[i]);
		}
	} else {
		document.getElementById('type-search').options[1] = document.getElementById('type-search').options[document.getElementById('type-search').options.selectedIndex];
		document.getElementById('type-search').options.length = 2;
		for (i in seatings){
			document.getElementById('type-search').options[document.getElementById('type-search').options.length] = new Option(seatings[i], seatings[i]);
		}
		document.getElementById('type-search').options.selectedIndex = 1;
	}


}

function resetFilterOptions(){

	console.log('Activated');

	//Following variables store filtering elements
	document.getElementById('loc-search').options.length = 1;
	document.getElementById('cuisine-search').options.length = 1;
	document.getElementById('type-search').options.length = 1;

	//Following function calls will fill indivisual filter lists
	fillLocOptions();
	fillCuisineOptions();
	fillTypeOptions();
}

function selectFunction(ele){
	document.getElementById('txt-search').value = ele.textContent;
	document.getElementById('filter-list').innerHTML = '';
}

function displayList(ele){
	var search = ele.value;
	if (search == ''){
		document.getElementById('filter-list').innerHTML = '';
	} else {
		var output = '';
		var pattern = '^'+search;
		var regexp = new RegExp(pattern, "i");
		city = ['Ahmedabad','Bengaluru','Bhopal','Chennai','Chandigar','Amritsar','Deharadun','New Delhi','Lucknow','Jaipur','Patna','Kolkata','Gowhati','Shimla','Darjeeling','Raipur','Allahabad','Agra','Pune','Mumbai','Nagpur','Hyderabad','Bhuvaneshwar','Vishakapattanam','Mysore','Kochi','Tiruvanatapuram','Panjim'].sort(); // A dummy list of cities	
		for (var i = 0; i <city.length; i++){
			if (regexp.test(city[i])){
				output += '<div style="font-weight: bold; color: white;" onclick="selectFunction(this)"><p>'+city[i]+'</p><hr></div>';
			}
		}
		document.getElementById('filter-list').innerHTML = output;
	}
}

function filterChange(ele){
	if (ele.name == 'location'){
		fillCuisineOptions();
		fillTypeOptions();
	} else if (ele.name == 'cuisine'){
		fillLocOptions();
		fillTypeOptions();
	} else {
		fillLocOptions();
		fillCuisineOptions();
	}
}