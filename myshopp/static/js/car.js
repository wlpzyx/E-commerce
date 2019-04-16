$(function(){
	//--------------登录分辨----------
	var isDenglu = $.cookie('isDengLu');
	var name = $.cookie('username');
	var amima = $.cookie('password');
	if(isDenglu == 1){
		$('.head-left>span').eq(0).text('您好！' + name +'，欢迎来到米米乐商城！');
		$('.head-left>span').eq(1).text('');
		$('.head-left>span').eq(2).append('<a href="javascript:;">退出</a>');
	};
	$('.head-left>.tuichu').on('click', 'a', function(){
		$.cookie('isDengLu', 1, { expires: -1 , path: '/'});
		$(this).attr('href', 'car.html');
	})
	//----------------------顶部下拉-------------------
	$('.head-nav').hover(function(){
		$(this).children('dd').stop(true, false).slideDown(100);
	},
	function(){
		$(this).children('dd').stop(true, false).slideUp(100);
		
	})
	
	
	
})


