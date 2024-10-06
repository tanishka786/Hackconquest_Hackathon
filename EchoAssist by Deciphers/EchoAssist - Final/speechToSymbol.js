function convertStringToASL(textString) {
    let charArray = Array.from(textString.toUpperCase());
    let charCodeHTML = '';
    let part1 = "<img class='ASL-letter' src='https://www.dcode.fr/tools/sign-language-american/images/char(";
    let part2 = ").png' alt='";
    let part3 = "' title='";
    let part4 = "'>";
    charArray.forEach((char) => {
        let charCode = char.charCodeAt(0);
        if (charCode === 32) {
            charCodeHTML += "&nbsp;&nbsp;&nbsp;";
        } else {
            charCodeHTML += part1 + charCode + part2 + char + part3 + char + part4;
        }
    });
    return charCodeHTML;
}

document.addEventListener('DOMContentLoaded', () => {
    const startRecordingButton = document.querySelector('#startSpeechToSymbol');
    const stopRecordingButton = document.querySelector('#stopSpeechToSymbol');

    const textResultDiv = document.querySelector('#resultText');
    const totalTextResultDiv = document.querySelector('#resultTextTot');
    const transResultDiv = document.querySelector('#resultTextTrans');
    const totalTransResultDiv = document.querySelector('#resultTextTransTot');
    const symbolResultDiv = document.querySelector('#resultSymbol');
    const totalSymbolResultDiv = document.querySelector('#resultSymbolTot');
    const instructions = document.querySelector('#instructions');

    let recognition;

    stopRecordingButton.disabled = true;

    if ('webkitSpeechRecognition' in window) {
        recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;
        recognition.lang = 'en-US';

        let totalTranscript = '';
        let totalSymbolScript = '';

        recognition.onstart = () => {
            stopRecordingButton.disabled = false;
            instructions.textContent = "Voice Recognition is On!";
            totalTranscript = '';
            totalSymbolScript = '';
        };

        recognition.onresult = (event) => {
            let interimTranscript = '';
            let finalTranscript = '';

            for (let i = event.resultIndex; i < event.results.length; i++) {
                const transcript = event.results[i][0].transcript;

                if (event.results[i].isFinal) {
                    finalTranscript += transcript + ' ';
                } else {
                    interimTranscript += transcript;
                }
            }

            let intText = finalTranscript || interimTranscript;
            textResultDiv.textContent = intText;
            let intTextSymbol = convertStringToASL(finalTranscript || interimTranscript);
            symbolResultDiv.innerHTML = intTextSymbol;

            let langInput = document.querySelector('#translatedLang').value;
            let intTextEncoded = encodeURI(intText);
            let api_URL = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=" + langInput + "&dt=t&q=" + intTextEncoded;

            fetch(api_URL)
                .then(response => response.json())
                .then(data => {
                    let translatedText = data[0][0][0];
                    transResultDiv.textContent = translatedText;
                });

            totalTranscript += finalTranscript;
            totalTextResultDiv.textContent = totalTranscript;
            totalSymbolScript += intTextSymbol;
            totalSymbolResultDiv.innerHTML = totalSymbolScript;
        };

        recognition.onerror = (event) => {
            instructions.textContent = 'Error occurred in recognition: ' + event.error;
        };

        recognition.onend = () => {
            stopRecordingButton.disabled = true;
            instructions.textContent = 'Voice Recognition has been turned off.';
        };
    } else {
        instructions.textContent = 'Your browser does not support Speech Recognition.';
    }

    startRecordingButton.addEventListener('click', () => {
        recognition.start();
        instructions.textContent = 'Voice Recognition started.';
        startRecordingButton.disabled = true;
        stopRecordingButton.disabled = false;
    });

    stopRecordingButton.addEventListener('click', () => {
        recognition.stop();
        startRecordingButton.disabled = false;
        stopRecordingButton.disabled = true;
        instructions.textContent = 'Voice Recognition stopped.';
    });
});