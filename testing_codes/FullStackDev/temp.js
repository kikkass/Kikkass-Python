function getUniqueLoc(cuisine,type){
	var locations = [];
	var regexp = new RegExp(cuisine, "i");
	for (index in contents){
		if (! locations.includes(contents[index].location) && (contents[index].location != '') && (regexp.test(contents[index].cuisine)) && (type == '' || contents[index].seating == type)){
			locations.push(contents[index].location);
		}
	}
	return locations.sort();
}

function getUniqueCuisine(location,type){
	var cuisines = [];
	for (cIndex in contents){
		obj_cuisines = contents[cIndex].cuisine.split(',');
		for(oIndex in obj_cuisines){
			if (! cuisines.includes(obj_cuisines[oIndex]) && (obj_cuisines[oIndex] != '') && (location == '' || contents[cIndex].location == location) && (type == '' || contents[cIndex].seating == type) && (contents[cIndex].location != '')){
				cuisines.push(obj_cuisines[oIndex]);
			}
		}
	}
	return cuisines.sort();
}

function getUniqueSeating(location,cuisine){
	var seating = [];
	var regexp = new RegExp(cuisine, "i");
	for (index in contents){
		if (!seating.includes(contents[index].seating) && (contents[index].seating != '') && (regexp.test(contents[index].cuisine)) && (location == '' || contents[index].location == location)){
			seating.push(contents[index].seating);
		}
	}
	return seating;
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

function filterRest(ele){
	if (ele.name == 'location'){

		var selectCuisine = document.getElementById('cuisine-search');
		var cuisine = getUniqueCuisine(ele.value,document.getElementById('type-search').value);
		var curSelection = selectCuisine.options[selectCuisine.options.selectedIndex];
		selectCuisine.options.length = 2;
		selectCuisine.options[1] = curSelection;
		selectCuisine.options.selectedIndex = 2;
		for(var i = 0; i <cuisine.length; i++){
			selectCuisine.options[selectCuisine.options.length] = new Option(cuisine[i], cuisine[i]);
		}

		var eaterieType = document.getElementById('type-search');
		var type = getUniqueSeating(ele.value,document.getElementById('cuisine-search').value);
		eaterieType.options.length = 1;
		for(var i = 0; i <type.length; i++){
			eaterieType.options[eaterieType.options.length] = new Option(type[i], type[i]);
		}
	} else if (ele.name == 'cuisine'){

		var selectLoc = document.getElementById('loc-search');
		var loc = getUniqueLoc(ele.value,document.getElementById('type-search').value);
		var curSelection = selectLoc.options[selectLoc.options.selectedIndex];
		selectLoc.options.length = 2;
		selectLoc.options[1] = curSelection;
		selectLoc.options.selectedIndex = 2;
		for(var i = 0; i <loc.length; i++){
			selectLoc.options[selectLoc.options.length] = new Option(loc[i], loc[i]);
		}

		var eaterieType = document.getElementById('type-search');
		var type = getUniqueSeating(ele.value,document.getElementById('cuisine-search').value);
		eaterieType.options.length = 1;
		for(var i = 0; i <type.length; i++){
			eaterieType.options[eaterieType.options.length] = new Option(type[i], type[i]);
		}
	}
}

var selectLoc = document.getElementById('loc-search');
var loc = getUniqueLoc(document.getElementById('cuisine-search').value,document.getElementById('type-search').value);	
for(var i = 0; i <loc.length; i++){
	selectLoc.options[selectLoc.options.length] = new Option(loc[i], loc[i]);
}

var selectCuisine = document.getElementById('cuisine-search');
var cuisine = getUniqueCuisine(document.getElementById('loc-search').value,document.getElementById('type-search').value);
for(var i = 0; i <cuisine.length; i++){
	selectCuisine.options[selectCuisine.options.length] = new Option(cuisine[i], cuisine[i]);
}

var eaterieType = document.getElementById('type-search');
var type = getUniqueSeating(document.getElementById('loc-search').value,document.getElementById('cuisine-search').value);
for(var i = 0; i <type.length; i++){
	eaterieType.options[eaterieType.options.length] = new Option(type[i], type[i]);
}
