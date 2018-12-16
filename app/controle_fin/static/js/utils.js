$(document).ready(function(){
    $( document ).on( 'focus', ':input', function(){
        $( this ).attr( 'autocomplete', 'off' );
    });
});

// $('#myModal').on('shown.bs.modal', function () {
//   $('#myInput').trigger('focus')
// })

$(document).ready(function(){
	var $myForm = $('#cadastroForm');
	$myForm.submit(function(event){
		event.preventDefault();
		var $formData = $myForm.serialize();
		var $thisURL = '/cadastro-banco/' || window.loaction.href;
		$.ajax({
			method:'POST',
			url: $thisURL,
			data: $formData,
			success: handleSuccess,
			error: handleError,
		});
		function handleSuccess(data){
		    var txt;
			var cnf = confirm(data.message);
			if (cnf == true){
			    txt = 'OK'
                $myForm[0].reset()
            } else {
			    txt = 'Cancel'
            }
            console.log(txt);


		}
		function handleError(ThrowError){
			console.log(ThrowError);
		}
	});
});


function LimparTela() {
    location.reload();
}

$(document).ready(function() {
    $("#debito_credito td:contains(Debito)").css('color', 'red');
    $("#debito_credito td:contains(dito)").css('color', 'blue');
});