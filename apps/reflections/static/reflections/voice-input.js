/**
 * 音声入力 API（Web Speech API ラッパー）
 * 各画面で script 読み込み後、init → start/stop するだけで音声→テキストが使える。
 *
 * 使い方（必要最低限）:
 *   <script src="{% static 'reflections/voice-input.js' %}"></script>
 *   <script>
 *     VoiceInput.init({ onResult: function(text) { document.getElementById('myInput').value += text; } });
 *   </script>
 *   <button onclick="VoiceInput.start()">音声入力開始</button>
 *   <button onclick="VoiceInput.stop()">音声入力停止</button>
 *   <input id="myInput" type="text">
 */
(function (global) {
  var SpeechRecognition = global.SpeechRecognition || global.webkitSpeechRecognition;
  var recognition = null;
  var opts = { lang: "ja-JP", onResult: function () {}, onError: function () {}, onStart: function () {}, onStop: function () {} };
  var listening = false;

  function isSupported() {
    return !!SpeechRecognition;
  }

  function init(options) {
    if (!SpeechRecognition) return false;
    if (recognition) return true;
    options = options || {};
    opts.lang = options.lang || "ja-JP";
    opts.onResult = typeof options.onResult === "function" ? options.onResult : opts.onResult;
    opts.onError = typeof options.onError === "function" ? options.onError : opts.onError;
    opts.onStart = typeof options.onStart === "function" ? options.onStart : opts.onStart;
    opts.onStop = typeof options.onStop === "function" ? options.onStop : opts.onStop;

    recognition = new SpeechRecognition();
    recognition.lang = opts.lang;
    recognition.continuous = true;
    recognition.interimResults = true;

    recognition.onresult = function (event) {
      for (var i = event.resultIndex; i < event.results.length; i++) {
        if (event.results[i].isFinal) opts.onResult(event.results[i][0].transcript);
      }
    };

    recognition.onerror = function (event) {
      var msg = event.error === "not-allowed" ? "マイクが許可されていません。" : (event.error || "音声認識に失敗しました。");
      opts.onError(msg);
      listening = false;
    };

    recognition.onend = function () {
      if (listening) {
        listening = false;
        opts.onStop();
      }
    };

    return true;
  }

  function start() {
    if (!recognition) return false;
    if (listening) return true;
    recognition.start();
    listening = true;
    opts.onStart();
    return true;
  }

  function stop() {
    if (!recognition || !listening) return false;
    recognition.stop();
    listening = false;
    opts.onStop();
    return true;
  }

  function isListening() {
    return !!listening;
  }

  global.VoiceInput = {
    isSupported: isSupported,
    init: init,
    start: start,
    stop: stop,
    isListening: isListening,
  };
})(typeof window !== "undefined" ? window : this);
