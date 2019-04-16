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
		$(this).attr('href', 'goodsdata.html');
	})
	//---------------全部商品下拉菜单
	$('.nav-down1').hover(
		function(){
			$(this).children('.banner-nav').css('display','block');
			
		},
		function(){
			$('.banner-nav').css('display','none')
		}
	);
	//---------------顶部下拉菜单
	$('.head-nav').hover(function(){
		$(this).children('dd').stop(true, false).slideDown(100);
	},
	function(){
		$(this).children('dd').stop(true, false).slideUp(100);
	});
	
	//----------------侧边栏特效----------------------
	$('.siderbar-hover').hover(
		function(){
			var aa = $(this).children('.siderbar-show').outerWidth();
			var $oThis = $(this);
			$(this).children('.siderbar-show').css('display','block').stop(true,false)
			$(this).children('.siderbar-show').animate({opacity: '1', left: -aa}, 500);
		},
		function(){
			var $oThis = $(this);
			$(this).children('.siderbar-show').animate({opacity: '0', left: 0}, 500,function(){
				$oThis.children('.siderbar-show').css('display','none')
			});
		}
	);
	$('.siderbar-click').on('click', function(){
		var aa = $(this).children('.siderbar-show').outerWidth();
		$(this).children('.siderbar-show').css('display','block').stop(true,false).animate({opacity: '1', left: -aa}, 500);
	});
	$('.car-show-tit>p').on('click', function(event){
		event.stopPropagation();
		var $oThis = $(this);
		$(this).parents('.car-show').animate({opacity: '0', left: 0}, 500,function(){
				$oThis.parents('.car-show').css('display','none');
		})
	})
	$('.topshow').on('click', function(){
		$(window).scrollTop(0);
	});
	//---------------------放大--------
	$('.goodsdata-top-left').hover(function(){
		$('.goodsdata-btn>a').css('display','block');
	},function(){
		$('.goodsdata-btn>a').css('display','none');
	})
	var aa = 0;
	$('.goodsdata-smallpic>li').hover(function(){
		var n = $(this).index();
		aa = n;
		var m = $('.goodsdata-bigpic>li:visible').index();
		
		if(n == m){
		}else if(n!=m){
			$('.goodsdata-smallpic>li').css('borderColor','white');
			$('.goodsdata-bigpic>li').stop(true,false).fadeOut(400);
			$('.goodsdata-smallpic>li').eq(n).css('borderColor','red');
			$('.goodsdata-bigpic>li').eq(n).stop(true,false).fadeIn(400);
		}
	})
	
	$('.goodsdata-btn-next').on('click', function(){
		aa++;
		if(aa>3){
			aa=0;
		}
		$('.goodsdata-smallpic>li').css('borderColor','white');
		$('.goodsdata-bigpic>li').stop(true,false).fadeOut(400);  
		$('.goodsdata-smallpic>li').eq(aa).css('borderColor','red');
		$('.goodsdata-bigpic>li').eq(aa).stop(true,false).fadeIn(400);
	})
	$('.goodsdata-btn-prev').on('click', function(){
		aa--;
		if(aa<0){
			aa=3;
		}
		$('.goodsdata-smallpic>li').css('borderColor','white');
		$('.goodsdata-bigpic>li').stop(true,false).fadeOut(400);  
		$('.goodsdata-smallpic>li').eq(aa).css('borderColor','red');
		$('.goodsdata-bigpic>li').eq(aa).stop(true,false).fadeIn(400);
	})
	
	$('.zhezhu').on('click', function(){
		$('.goodsdata-btn-close').css({'display':'block', 'left': 1200});
		$('.goodsdata-btn-next').css({'left': 1200});
		$('.goodsdata-bigpic').stop(true,false).animate({'width':1200, 'height': 500},500);
		$('.goodsdata-bigpic>li').stop(true,false).animate({'width':1200, 'height': 450},500);
		$('.goodsdata-bigpic>li>img').stop(true,false).animate({'width':450, 'height': 450},500);
		$(this).css('display', 'none')
	})
	$('.goodsdata-btn-close').on('click', function(){
		$('.goodsdata-bigpic>li>img').animate({'marginTop': 0}, 100,function(){
			$('.goodsdata-btn-next').css({'left': 300});
			$('.goodsdata-bigpic').stop(true,false).animate({'width':360, 'height': 360},500);
			$('.goodsdata-bigpic>li').stop(true,false).animate({'width':360, 'height': 360},500);
			$('.goodsdata-bigpic>li>img').stop(true,false).animate({'width':360, 'height': 360},500);
			$('.goodsdata-btn-close').css({'display':'none'});
			$('.zhezhu').css('display', 'block');
		});
	})
	$('.goodsdata-bigpic>li>img').on('click', function(){
		$('.goodsdata-bigpic>li>img').stop(true,false).animate({'width':1200, 'height': 1200}, 500);
		$('.goodsdata-bigpic>li>img').css('cursor', 'move');
	})
	
	
	
