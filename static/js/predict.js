document.getElementById("predict-button").addEventListener("click", function() {
    let question = document.getElementById('quest');
    let paragraph = document.getElementById('para');
    let result = document.getElementById('result-text');

    const getPrediction = async (question, paragraph) => {
       const response = await fetch('/predict', {
            method: 'POST',
            body: JSON.stringify({'question':question, 'paragraph':paragraph}),
            headers: {
                'Content-Type': 'application/json'
            }
       });
       const myJson = await response.json();
            return myJson.result;
   }

   let predtext = getPrediction(question.value, paragraph.value);
       predtext.then(function (response) {
            result.textContent = response;
   });


}, false);
