$(function(){
	//--------------登录分辨----------
	var isDenglu = $.cookie('isDengLu');
	var name = $.cookie('username');
	var amima = $.cookie('password');
	if(isDenglu == 1){
		$('.head-left>span').eq(0).text('您好！' + name +'，欢迎来到米米乐商城！');
		$('.head-left>span').eq(1).text('');
		$('.head-left>span').eq(2).append('<a href="javascript:;">退出</a>');
		$('.banner-right-tit').text('');
		$('.banner-right-tit').append('<h4>'+ name + '<br/>欢迎您！</h4>');
	};
	$('.head-left>.tuichu').on('click', 'a', function(){
		$.cookie('isDengLu', 1, { expires: -1 , path: '/'});
		$(this).attr('href', 'searchlist.html');
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
	//--------------所在地选择
	$('.search-goods-location').hover(function(){
		$(this).children('.search-goods-location-list').css({'display':'block', 'zIndex': 100, 'background': 'white'});
	},function(){
		$('.search-goods-location-list').css({'display':'none'});
	})
	//搜索结果显示
	$('.goods-pic-out').hover(function(){
		$(this).css('overflow', 'visible');
		$(this).children('.goods-pic-in').css('zIndex','100');
		$(this).children('.goods-pic-in').children('.goods-pic-in-bottom').stop(true, false).animate({'top':183},500)
	},function(){
		$(this).children('.goods-pic-in').children('.goods-pic-in-bottom').stop(true, false).animate({'top':226},500)
		$(this).css('overflow', 'hidden');
		$(this).children('.goods-pic-in').css('zIndex','0');
	})
	//------吸顶
	$(window).on('scroll', function(event){
		if($(window).scrollTop()>400){
			$('.search-xiding-wrap').css({'display': 'block', 'zIndex': '200'});
			$('.search-xiding-wrap').stop(true, false).animate({'top': 0},200);
		}else{
			$('.search-xiding-wrap').stop(true, false).animate({'top': -50},200, function(){
				$('.search-xiding-wrap').css('display', 'none');
			});
			
		}
	})
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
	})
})
