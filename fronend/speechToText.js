// status fields and start button in UI
var phraseDiv;
var startRecognizeOnceAsyncButton;

// subscription key and region for speech services.
var subscriptionKey, serviceRegion;
var authorizationToken;
var SpeechSDK;
var recognizer;
// wss://eastus.stt.speech.microsoft.com/speech/recognition/interactive/cognitiveservices/v1?language=en-US&format=simple&Ocp-Apim-Subscription-Key=5ddec480deda4a3ea442cdd812bf429a&X-ConnectionId=34BAA660F48F46A793BF6F9F6A10BF8B
// https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/274b0beb-01bd-4fb0-b8c8-4d63d5cbeba1?staging=true&verbose=true&timezoneOffset=-360&subscription-key=5ddec480deda4a3ea442cdd812bf429a&q=fetch 
document.addEventListener("DOMContentLoaded", function () {
  startRecognizeOnceAsyncButton = document.getElementById("startRecognizeOnceAsyncButton");
  subscriptionKey = "7d20015ea7c94687883a3e49d3cfdbf1";
  serviceRegion = "westus";
  phraseDiv = document.getElementById("phraseDiv");

  startRecognizeOnceAsyncButton.addEventListener("click", function () {
    startRecognizeOnceAsyncButton.disabled = true;
    phraseDiv.innerHTML = "";

    // if we got an authorization token, use the token. Otherwise use the provided subscription key
    var speechConfig;
    speechConfig = SpeechSDK.SpeechConfig.fromSubscription(subscriptionKey, serviceRegion);
    

    speechConfig.speechRecognitionLanguage = "en-US";
    var audioConfig  = SpeechSDK.AudioConfig.fromDefaultMicrophoneInput();
    recognizer = new SpeechSDK.SpeechRecognizer(speechConfig, audioConfig);

    recognizer.recognizeOnceAsync(
      function (result) {
        startRecognizeOnceAsyncButton.disabled = false;
        phraseDiv.innerHTML += result.text;
        $.getJSON( "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/274b0beb-01bd-4fb0-b8c8-4d63d5cbeba1?staging=true&verbose=true&timezoneOffset=-360&subscription-key=5ddec480deda4a3ea442cdd812bf429a&q=" + result.text, function( data ) {
          var items = [];

        });
        

        recognizer.close();
        recognizer = undefined;
      },
      function (err) {
        startRecognizeOnceAsyncButton.disabled = false;
        phraseDiv.innerHTML += err;
        window.console.log(err);

        recognizer.close();
        recognizer = undefined;
      });
  });

  if (!window.SpeechSDK) {
    SpeechSDK = window.SpeechSDK;
    startRecognizeOnceAsyncButton.disabled = false;


    // in case we have a function for getting an authorization token, call it.
    if (typeof RequestAuthorizationToken === "function") {
        RequestAuthorizationToken();
    }
  }
});