// $(function(){
	// Configuration
	moment().calendar(null, {
	  sameDay: '[Today]',
	  nextDay: '[Tomorrow]',
	  nextWeek: 'dddd',
	  lastDay: '[Yesterday]',
	  lastWeek: '[Last] dddd'
	});
	
	
	// Data
	var departure;
	var now = moment();
	var dateFormat = 'dddd MMM. Do, YYYY';
	
	
	// Elements
	var form = $('#add-form');
	var inputs = $('input:not(:button, :submit), select, textarea');
	var selects = $('select');
	var checkboxes = inputs.filter('[type=checkbox]');
	var radios = inputs.filter('[type=radio]');
	var departureInput = document.getElementById('departure');
	var departureHidden = $('#departure-timestamp');
	var purposeOther = $('#purpose-other');
	var button = $('input[type=submit]');
	
	var modal = $('.modal');
	
	
	// Style state classnames
	var state = {
	  focus : 'has-focus',
	  valid : 'is-valid',
	  invalid : 'is-invalid'
	};
	
	
	// Initialization
	// initializeDeparture();
	initializeInputs();
	
	
	// Form and input event listeners
	form.submit(function(event){ 
	  save(event); 
	});
	selects.change(function(event){ 
	  selectHandler($(event.target)); 
	});
	checkboxes.change(function(event){ 
	  checkboxHandler($(event.target)); 
	});
	radios.change(function(event){ 
	  radioHandler($(event.target)); 
	});
	
	function initializeDepartureClasses(departureInputList){
		$(departureInputList).each(function(i){
			initializeDeparture(departureInputList[i]);
		})
	}


	// Departure
	function initializeDeparture(departureInput){
	  var input = $(departureInput);
	  
	  departure = {
		finder : new Pikaday({
		  field: departureInput,
		  format: dateFormat,
		  minDate: now.toDate()
		})
	  };
	  
	  input.change(function(event){
		var value = $(event.target).val();
		var stamp = departure.finder.getMoment().unix();
		departureHidden.val(stamp);
	  });
	  
	  input.val((now.format(dateFormat)));
	  departure.finder.setMoment(now);
	}
	
	
	// Inputs – Indicate set defaults
	function initializeInputs(){
	  selects.each(function(index, element){
		selectHandler($(element));
	  });
	  
	  checkboxes.each(function(index, element){
		checkboxHandler($(element));
	  });
	  
	  radioHandler();
	};
	
	
	// Checkboxes – Inicate checked option
	function checkboxHandler(element){
	  if (element.is(':checked')) {
		element.parent().addClass(state.valid);
	  } else {
		element.parent().removeClass(state.valid);
	  }
	}
	
	
	// Radio Buttons – Indicate chosen
	function radioHandler(){
	  radios.each(function(index, element){
		var element = $(element);
		var isChecked = element.is(':checked');
	  
		if (isChecked) {
		  element.parent().addClass(state.valid);
		} else {
		  element.parent().removeClass(state.valid);
		}
	  });
	}
	
	
	// Select Options – Indicated chosen
	function selectHandler(element){
	  var value = $(element).val();
	  var isSet = value !== null;
	  var isOther = value === "other";
	  
	  if (isSet) {
		element.addClass(state.valid);
	  } else {
		element.removeClass(state.valid);
	  }
	  
	  if (isOther) {
		purposeOther.show().focus();
	  } else {
		purposeOther.hide();
	  }
	}
	
	// Form Submit – Data handling (Create JSON)
	function save(event){
  
	  var data = {};
	  
	  inputs.each(function(index, element){
		var input = $(element);
		var key = input.attr('name');
		var value = input.val();
		
		data[key] = value;
	  });
	  
	  //var dataString = JSON.stringify(data);
	  //var dataJSON = JSON.parse(dataString);
	  
	  console.log(data, getTimeToTrip());
	  
	  event.preventDefault();
	}
	
	function getTimeToTrip(){
	  var leaving = departure.finder.getMoment();
	  var message = now.to(leaving, true);
	  
	  var alt = leaving.calendar(null, {
		sameDay: '[Today]',
		nextDay: '[Tomorrow]'
	  });
	  
	  if (alt === "Today" || alt === "Tomorrow") {
		message = alt;
	  }
	  
	  //return message;
	  return message;
	}
//   });