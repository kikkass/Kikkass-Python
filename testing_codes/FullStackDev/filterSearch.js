// var json = require('Programming_Task_DataFile.json');
// import * as json from 'Programming_Task_DataFile.json'
console.log(contents.length)

function selectFunction(ele){
	document.getElementById('txt-search').value = ele.textContent;
	document.getElementById('filter-list').innerHTML = '';
}

function get_unique_loc(){
	var locations = [];
	for (index in contents){
		if (! locations.includes(contents[index].location) && contents[index].location != ''){
			locations.push(contents[index].location);
		}
	}
	return locations.sort();
}

function get_cuisine(){
	var cuisines = [];
	for (index in contents){
		obj_cuisines = contents[index].cuisine.split(',');
		for(index in obj_cuisines){
			if (! cuisines.includes(obj_cuisines[index]) && (obj_cuisines[index] != '')){
				cuisines.push(obj_cuisines[index]);
			}
		}
	}
	return cuisines.sort();
}

function displayList(ele){
	var search = ele.value;
	if (search == ''){
		document.getElementById('filter-list').innerHTML = '';
	} else {
		var output = '';
		var pattern = '^'+search;
		var regexp = new RegExp(pattern, "i");
		loc = get_unique_loc();	
		for (var i = 0; i <loc.length; i++){
			if (regexp.test(loc[i])){
				output += '<div style="font-weight: bold; color: white;" onclick="selectFunction(this)"><p>'+loc[i]+'</p><hr></div>';
			}
		}
		document.getElementById('filter-list').innerHTML = output;
	}
}


var selectLoc = document.getElementById('loc-search');
loc = get_unique_loc();	
for(var i = 0; i <loc.length; i++){
	selectLoc.options[selectLoc.options.length] = new Option(loc[i], loc[i]);
}

var selectCuisine = document.getElementById('ciusine-search');
cuisine = get_cuisine();
for(var i = 0; i <cuisine.length; i++){
	selectCuisine.options[selectCuisine.options.length] = new Option(cuisine[i], cuisine[i]);
}
