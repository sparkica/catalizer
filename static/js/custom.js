$(document).ready(function(){
	$('input[id^="slider_"]').on('change', function() {
		var output = '#'+this.name + '_output';
		$(output).val(this.value);
	})
})