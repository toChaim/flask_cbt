$(document).ready(function(){
	var user_id = $('#user_id').val();
	var csrf_token = $('#csrf_token').val();
	console.log(csrf_token,user_id);

	var url = `/users/${user_id}/matches`
	var promis = $.get(url).then(function(data){ return data; })
});