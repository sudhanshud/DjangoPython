
jQuery(document).ready(function() {
    
    /*
        Form
    */
    $('.release-form fieldset:first-child').fadeIn('slow');
    
    $('.release-form input[type="text"], .release-form input[type="password"], .release-form textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });


    // previous step
    $('.release-form .btn-warning').on('click', function() {
    	$(this).parents('fieldset').fadeOut(400, function() {
    		$(this).prev().fadeIn();
    	});
    });
    
    // submit
    $('.release-form').on('submit', function(e) {
    	
    	$(this).find('input[type="text"], input[type="password"], textarea').each(function() {
    		if( $(this).val() == "" ) {
    			e.preventDefault();
    			$(this).addClass('input-error');
    		}
    		else {
    			$(this).removeClass('input-error');
    		}
    	});
    	
    });
    
    
});
