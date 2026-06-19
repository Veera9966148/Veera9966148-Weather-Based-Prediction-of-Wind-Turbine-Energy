function showToast(message){

const toast =
document.getElementById(
"toast"
);

toast.innerText = message;
toast.style.display = "block";

setTimeout(() => {

toast.style.display = "none";

},3000);

}

const form =
document.getElementById(
"predictionForm"
);

if(form){

form.addEventListener(
"submit",
async (e)=>{

e.preventDefault();

const city =
document.getElementById(
"city"
).value;

const power =
document.getElementById(
"power"
).value;

const wind =
document.getElementById(
"wind"
).value;

if(power<=0 || wind<=0){

showToast(
"Invalid values"
);

return;
}

document
.getElementById(
"loading"
)
.classList
.remove(
"hidden"
);

try{

const response =
await fetch(
"/predict",
{
method:"POST",
headers:{
"Content-Type":
"application/json"
},
body:
JSON.stringify({
city,
theoretical_power:
power,
wind_speed:
wind
})
}
);

const data =
await response.json();

document
.getElementById(
"loading"
)
.classList
.add(
"hidden"
);

if(data.success){

document
.getElementById(
"resultCard"
)
.classList
.remove(
"hidden"
);

document
.getElementById(
"predictionValue"
)
.innerText =
data.prediction;

showToast(
"Prediction Successful"
);

}
else{

showToast(
data.message
);

}

}
catch{

showToast(
"Server Error"
);

}

});
}

const historyChart =
document.getElementById(
"historyChart"
);

if(historyChart){

new Chart(
historyChart,
{
type:"line",
data:{
labels:[
"Mon",
"Tue",
"Wed",
"Thu",
"Fri"
],
datasets:[
{
label:
"Power",
data:[
500,
900,
700,
1200,
1000
]
}
]
}
}
);

}

const windChart =
document.getElementById(
"windChart"
);

if(windChart){

new Chart(
windChart,
{
type:"bar",
data:{
labels:[
"5",
"6",
"7",
"8",
"9"
],
datasets:[
{
label:
"Wind",
data:[
500,
650,
900,
1200,
1500
]
}
]
}
}
);

}
