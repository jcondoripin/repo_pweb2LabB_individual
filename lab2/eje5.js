document.getElementById('table-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var numValues = parseInt(document.getElementById('numValues').value);
    
    var tableContainer = document.getElementById('table-container');
    tableContainer.innerHTML = '';
    
    var table = document.createElement('table');
    var tableRow = document.createElement('tr');
    
    for (var i = 1; i <= numValues; i++) {
      var tableData = document.createElement('td');
      var input = document.createElement('input');
      input.type = 'number';
      input.name = 'value-' + i;
      input.required = true;
      tableData.appendChild(input);
      tableRow.appendChild(tableData);
    }
    
    table.appendChild(tableRow);
    tableContainer.appendChild(table);
    
    var calculateBtn = document.getElementById('calculate-btn');
    calculateBtn.disabled = false;
});
  
document.getElementById('calculate-btn').addEventListener('click', function() {
    var inputs = document.querySelectorAll('input[name^="value-"]');
    var sum = 0;
    
    for (var i = 0; i < inputs.length; i++) {
      sum += parseInt(inputs[i].value);
    }
    
    alert('La suma de los valores es: ' + sum);
});