  $(document).ready(function(){
    $('select').formSelect();
  });

  $(document).ready(function(){
    $('.datepicker').datepicker();
    var inputs = document.querySelectorAll('.datepicker');
    var datepickers = M.Datepicker.init(inputs);
    datepickers[0].open();
    });

  $(document).ready(function(){
    $('.timepicker').timepicker().defaultTime();
  });