function validateDate() {
  var dateInput = document.getElementById('dateInput');
  var selectedDate = new Date(dateInput.value);
  var currentDate = new Date();

  if (selectedDate > currentDate) {
    alert('Please select a past date');
    dateInput.value = ''; // Clear the input value
  }
}
    window.onload = function () {
      var chart = new CanvasJS.Chart("Barchart",
      {
        title:{
          text: "Accidents Assements"
        },
        data: [
        {
          type: "bar",
          dataPoints: [
          { y: 788, label: "Male"},
          { y: 201, label: "Female"},
          { y: 202, label: "20-30"},
          { y: 236, label: "30-40"},
          { y: 395, label: "40-50"},
          { y: 127, label: "Infants"}
          ]
        },
        {
          type: "bar",
          dataPoints: [
          { y: 776, label: "Male"},
          { y: 144, label: "Female"},
          { y: 223, label: "20-30"},
          { y: 272, label: "30-40"},
          { y: 319, label: "40-50"},
          { y: 200, label: "Infants"}
          ]
        },
        {
          type: "bar",
          dataPoints: [
          { y: 600, label: "Male"},
          { y: 128, label: "Female"},
          { y: 246, label: "20-30"},
          { y: 272, label: "30-40"},
          { y: 296, label: "40-50"},
          { y: 200, label: "Infants"}
          ]
        }
        ]
      });
      chart.backgroundColor = 'rgba(0, 0, 0, 0)';
    chart.render();
  }
  
  /*
      // Chart.js configuration
      var chartCanvas = document.getElementById('chartCanvas');
      var chartCtx = chartCanvas.getContext('2d');
      var chartData = {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: 'Sample Dataset',
      data: [12, 19, 3, 5, 2, 3],
      backgroundColor: ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(255, 206, 86, 0.6)',
                        'rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)', 'rgba(255, 159, 64, 0.6)'],
      borderColor: 'rgba(255, 99, 132, 1)',
      borderWidth: 1,
  
    }]
  };
      var chartOptions = {
        responsive: true,
        maintainAspectRatio: false
      };
      var chart = new Chart(chartCtx, {
        type: 'doughnut',
        data: chartData,
        options: chartOptions
      });
  */
      //2D Bar Graph
     
const toggleTheme = (isChecked) => {
  const theme = isChecked ? "dark" : "light";

  document.documentElement.dataset.mdbTheme = theme;
}
// add listener to toggle theme with Shift + D
document.addEventListener("keydown", (e) => {
  if (e.shiftKey && e.key === "D") {
    themeStitcher.checked = !themeStitcher.checked;
    toggleTheme(themeStitcher.checked);
  }
});

var currentStage = 1;
    var modal = document.getElementById('modal');
    var stages = document.getElementsByClassName('modal-stage');

    function openModal() {
      modal.style.display = 'block';
      showStage(currentStage);
    }

    function closeModal() {
      modal.style.display = 'none';
    }

    function showStage(stage) {
      for (var i = 0; i < stages.length; i++) {
        stages[i].classList.remove('active');
      }

      stages[stage - 1].classList.add('active');
    }

    function nextStage() {
      if (currentStage < stages.length) {
        currentStage++;
        showStage(currentStage);
      }
    }

    function prevStage() {
      if (currentStage > 1) {
        currentStage--;
        showStage(currentStage);
      }
    }

    function submitForm() {
      // Handle form submission logic here
      alert('Form submitted successfully!');
      closeModal();
    }

    var modal = document.getElementById("modal");
    var closeBtn = document.getElementsByClassName("close")[0];
    
    closeBtn.addEventListener("click", function() {
      modal.style.display = "none";
    });
    const severityInput = document.getElementById("severity-input");
    const severityValues = document.querySelectorAll(".severity-value");
    
    severityInput.addEventListener("input", () => {
      const value = severityInput.value;
      severityValues.forEach((el, i) => {
        if (i < value) {
          el.classList.add("active");
        } else {
          el.classList.remove("active");
        }
      });
    });