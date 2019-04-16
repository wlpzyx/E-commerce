$(function(){
	
	$('#login').on('click', function(){
		var ID = $('#username').val();
		var PW = $('#code').val();
		var name = $.cookie('username');
		var amima = $.cookie('password');
		var isDengLu = '1';
		if(ID === name & PW === amima){
			$.cookie('isDengLu', isDengLu, { expires: -1 , path: '/'});
			alert('登录成功！');
			$('#login').attr('href', '../index.html');
			$.cookie('isDengLu', isDengLu, { expires: 1, path: '/' });
			
		}else{
			alert('账号或密码错误！');
		}
	})
})
