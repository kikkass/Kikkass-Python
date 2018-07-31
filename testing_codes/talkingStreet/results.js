console.log(contents)

var parameters = location.search.substring(1).split("&");
var filter = {};
for (i in parameters){
	let keyVal = parameters[i].split('=');
	filter[keyVal[0]] = keyVal[1];
}

filter.cuisine = decodeURIComponent(filter.cuisine).replace(/\+/g,' ');
filter.location = filter.location.replace(/\+/g,' ');
var regexp = new RegExp(filter.cuisine, "i");

var filteredList = [];

for (i in contents){
	if ((contents[i].location == filter.location || !filter.location) && (regexp.test(contents[i].cuisine)) && (contents[i].seating == filter.seating || !filter.seating)){
		filteredList.push(contents[i])
	}
}

var output = '';
for (i in filteredList){

	var imgUrl = filteredList[i].image_url.replace('//d3501repw3v4i0.cloudfront.net','http://publish.talkingstreet.in:8080');
	if (filteredList[i].isOutlet){
		var info = ' <sup><span class="badge badge-info">OUTLET</span></sup>';
	} else {
		var info = ' <sup><span class="badge badge-secondary">BLOG</span></sup>';
	}

	output += '<div class="card text-center" style="width: 60%; margin: auto; margin-top: 2rem; align-content: center;">';
	output += '<div class="card-body">';
	output += '<h5 class="card-title">' + filteredList[i].post_title + info + '</h5>';
	output += '<div style="border: 2px solid gray; height: 40%; width: 60%; margin: auto;">';
	output += '<img class="card-img-top" src="' + imgUrl + '" alt="" style="height: 100%; width: 100%;">';
	output += '</div>';
	output += '<hr>';
	output += '<p class="card-text">' + filteredList[i].address + '</p>';
	output += filteredList[i].special_info;
	output += '<br><a href="#" class="btn btn-primary">More</a>';
	output += '</div>';
	output += '</div>';
	}

document.getElementById('results').innerHTML = output;
