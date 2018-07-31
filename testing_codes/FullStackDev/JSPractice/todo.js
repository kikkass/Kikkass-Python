var toDo = [];

function runToDo(){
	while (true){
		let option = prompt("Select any option:")
		if (option.toLowerCase() == 'quit'){
			break;
		} else if (option.toLowerCase() == 'add'){
			toDo.push(prompt("Create a remainder:"));
		} else if (option.toLowerCase() == 'delete') {
			let index = prompt("Please mention the index of the reminder:");
			let b = toDo.splice(index,1);
			console.log(b + ' was removed from the list');
		} else {
			console.log("*******************");
			toDo.forEach(function(action,index){
				console.log(index + ' - ' + action);
			})
			console.log("*******************");
		}
	}
}


