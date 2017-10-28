<?php

//function for the pomodoro main time
function firstIteration(){
  usleep(1200000000);
}

//function for the pomodoro 5 minute break
function secondIteration(){
  usleep(300000000)
}

function postMethod($message){
  $c = curl_init(SLACK_WEBHOOK);
  curl_setopt($c, CURLOPT_SSL_VERIFYPEER, false);
  curl_setopt($c, CURLOPT_POST, true);
  curl_setopt($c, CURLOPT_POSTFIELDS, $message);
  curl_exec($c);
  curl_close($c);
}

define('SLACK_WEBHOOK','https://hooks.slack.com/services/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');
$command = $_POST['command'];
$channel = $_POST['channel_id'];
$user_name = $post['user_name'];

$stop = False;
while($stop == False){

$start_text = "<@".$user_id."|".$user_name."> : Starting Tomato Cycle!";
postMethod($start_text);
firstIteration();

$break_text = "<@".$user_id."|".$user_name."> : Take a Break!";
postMethod($break_text);
secondIteration();
//Cycle Through While
}

 ?>
