function getColor(){
  let r = Math.floor(Math.random() * (256));
  let g = Math.floor(Math.random() * (256));
  let b = Math.floor(Math.random() * (256));

  return 'rgb(' + r + ', ' + g + ', ' + b + ')';
}

function fillColor(){
  for (var i = 0; i < squares.length; i++){
    squares[i].style.backgroundColor = colorPicked;
  }
}

var colors = [getColor(),getColor(),getColor(),getColor(),getColor(),getColor()];
var colorPicked = colors[Math.floor(Math.random() * (6))];
var squares = document.querySelectorAll(".square");
var rgbDisplay = document.querySelector("#rgbValue");

rgbDisplay.textContent = colorPicked;

for (var i = 0; i < squares.length; i++){
  // Add initial colors to squares
  squares[i].style.backgroundColor = colors[i];

  // Add click event listener to each of the squares
  squares[i].addEventListener("click", function(){
    // Grab the color of clicked square
    var colorClicked = this.style.backgroundColor;
    if(colorClicked === colorPicked){
      fillColor();
    } else {
      this.style.backgroundColor = '#222222';
    }
  });
}
