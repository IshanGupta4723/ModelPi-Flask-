var drive_mode = 'Normal';
var last_key = 'w';
var adaptive_cruise_status = 'Disengaged';
var cruise_status = 'Disengaged';
var parking_brake = 'Engaged';
var current_gear = 'N'
//movement functions
function gas(direction) {
  $.ajax({
    url:'',
    type:'get',
    data: {
      movement:direction
    }
  })
}
function stop() {
  $.ajax({
    url:'',
    type:'get',
    data: {
      movement:"stop"
    }
  })
}
function go_left() {
  $.ajax({
    url:'',
    type:'get',
    data: {
      movement:"left"
    }
  })
}
function go_right() {
  $.ajax({
    url:'',
    type:'get',
    data: {
      movement:"right"
    }
  })
}

//thread management
function start_thread() {
  $.ajax({
      url:'',
      type:'get',
      data: {
        thread:"start"
      }
    })
}

function kill_thread() {
  $.ajax({
    url:'',
    type:'get',
    data:{
      thread:'kill'
    }
  })
}
//APPLY BRAKES WHEN KEY IS RELEASED

//SENDING AJAX QUERY
function idle() {
  $.ajax({
    url:'',
    tyoe:'get',
    data:{
      movement:'idle'
    }
  })
}

//EVENT LISTENER FOR KEY RELEASE
document.addEventListener('keyup',function(event) {
    idle()
    console.log(event.key)
  }
) 

function change_drive_mode(mode) {
  $.ajax({
    url:'',
    tyoe:'get',
    data:{
      drive_mode:mode
    }
  })
}

function change_gear(gear){
  $.ajax({
    url:'',
    tyoe:'get',
    data:{
      transmission:gear
    }
  })
}

function park(status) {
  $.ajax({
    url:'',
    tyoe:'get',
    data:{
      park:status
    }
  })
}

function cruise(status){
  $.ajax({
    url:'',
    tyoe:'get',
    data:{
      cruise:status
    }
  })
}
//MOVING ON KEYPRESS
//Key press listener

document.addEventListener('keypress', function(event) {
  const key = event.key; // "a", "1", "Shift", etc.
  if (key===last_key) {
    //do nothing
  }
  else if (key==='w'){
    if(current_gear==='D'){
      gas("front");
    }
    else if(current_gear==='R'){
      gas("back");
    }
    last_key = 'w';
  }
  else if (key==='s'){
    stop();
    last_key = 's';
  }
  else if (key==='a'){
    go_left()
    last_key = 'a';
  }
  else if (key==='d'){
    go_right()
    last_key = 'd';
  }
})
//CHECKING IF SCRIPT HAS LOADED
$(document).ready(function(){
  console.log("script.js has been loaded!");
})

//CHANGE DRIVE MODE ON BUTTON CLICK
$('.Sport').click(function(){
  console.log("Sport drivemode activated!");
  drive_mode = 'Sport';
  $('.Sport').css("border","solid 3px red");
  $('.Sport').css("color","red");
  $('.Eco').css("border","none");
  $('.Eco').css("color","#0d7d29");
  $('.Normal').css("border","none");
  $('.Normal').css("color","#094a7b");
  change_drive_mode("Sport")
})
$('.Normal').click(function(){
  console.log("City drivemode activated!");
  drive_mode = 'Normal';
  $('.Sport').css("border","none");
  $('.Sport').css("color","#7b0909");
  $('.Eco').css("border","none");
  $('.Eco').css("color","#0d7d29");
  $('.Normal').css("border","solid 3px cyan");
  $('.Normal').css("color","cyan");
  change_drive_mode("City")
})

$('.Eco').click(function(){
  console.log("Economy drivemode activated!")
  drive_mode = 'Economy';
  $('.Sport').css("border","none");
  $('.Sport').css("color","#7b0909");
  $('.Normal').css("border","none");
  $('.Normal').css("color","#094a7b");
  $('.Eco').css("border","solid 3px lime");
  $('.Eco').css("color","lime");
  change_drive_mode("Eco")
})

$('.cruise').click(function(){
  if (adaptive_cruise_status=='Disengaged') {
    console.log("Adaptive cruise control has been engaged!");
    start_thread();
    adaptive_cruise_status = 'Engaged';
    $('.cruise').css("color","#00ff00");
    $('.cruise').css("border-color","#00ff00");
    
  }
  else if (adaptive_cruise_status=='Engaged') {
    console.log("Adaptive cruise control has been disengaged!");
    kill_thread();
    adaptive_cruise_status = 'Disengaged';
    $('.cruise').css("color","#888a0f");
    $('.cruise').css("border-color","#888a0f");
  }
})

$('.auto').click(function(){
  if (cruise_status=='Disengaged') {
    console.log("cruise control has been engaged!");
    cruise_status = 'Engaged';
    $('.auto').css("color","#00ff00");
    cruise("Engaged");
    
  }
  else if (cruise_status=='Engaged') {
    console.log("cruise control has been disengaged!");
    cruise_status = 'Disengaged';
    $('.auto').css("color","#888a0f");
    cruise("Disengaged");
  }
})

$('.park_hold').click(function(){
  if (parking_brake=='Disengaged') {
    console.log("Adaptive cruise control has been engaged!");
    parking_brake = 'Engaged';
    $('.park_hold').css("color","#ff0000");
    park("Engaged");
    
  }
  else if (parking_brake=='Engaged') {
    console.log("Adaptive cruise control has been disengaged!");
    parking_brake = 'Disengaged';
    $('.park_hold').css("color","#7b0f0f");
    park("Disengaged");
  }
})

$('.N').click(function(){
  console.log("Adaptive cruise control has been engaged!");
  current_gear = 'N';
  $('.N').css("color","#ff9500");
  $('.R').css("color","#ffffff");
  $('.D').css("color","#ffffff");
  change_gear('N');
})

$('.D').click(function(){
  console.log("Adaptive cruise control has been engaged!");
  current_gear = 'D';
  $('.D').css("color","#ff9500");
  $('.N').css("color","#ffffff");
  $('.R').css("color","#ffffff");
  change_gear('D');
})

$('.R').click(function(){
  console.log("Adaptive cruise control has been engaged!");
  current_gear = 'R';
  $('.R').css("color","#ff9500");
  $('.N').css("color","#ffffff");
  $('.D').css("color","#ffffff");
  change_gear('R');
})



