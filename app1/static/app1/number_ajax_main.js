/*$(document).ready(function()  {
	jQuery('.ajaxform').submit( function(e) {
    alert(in ajax);
    e.preventDefault();
		var searchText = $('#number_search_text').val();
    alert(searchText);
		$var config = {
            url     : $(this).attr('action'),
            type    : $(this).attr('method'),
            data: {
        		'number_search_text' : searchText,
      		},
      		dataType: 'html',
      		success: processServerResponse
      	};
      	$.ajax(config);
     });
     var processServerResponse = function(sersverResponse_data, textStatus_ignored,
                        jqXHR_ignored)  {
      //alert("sersverResponse_data='" + sersverResponse_data + "', textStatus_ignored='" + textStatus_ignored + "', jqXHR_ignored='" + jqXHR_ignored + "'");
      $('#number_search_results').load(sersverResponse_data);
    };
 });*/


    $(document).ready(function() {
            //option A
            $('#ajaxform').submit(function(e){
              e.preventDefault();
                alert('submit intercepted');
                
            });
        });
   

		