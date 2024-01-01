// TODO: https://codepen.io/ralzohairi/pen/zYrKLWy
function testFunction(button) {
    alert("checked");
  }


//API to handle audio recording
var audioRecorder = {
  /** Start recording the audio
    * @returns {Promise} - returns a promise that resolves if audio recording successfully started
    */
  start: function () {
    if (!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia)) {
      //Feature is not supported in browser
      //return a custom error
      return Promise.reject(new Error('mediaDevices API or getUserMedia method is not supported in this browser.'));
    }
    else {
      //Feature is supported in browser
      //...
    }
  },
  /** Stop the started audio recording
    * @returns {Promise} - returns a promise that resolves to the audio as a blob file
    */
  stop: function () {
  //...
  },
  /** Cancel audio recording*/
  cancel: function () {
  //...
  }
}