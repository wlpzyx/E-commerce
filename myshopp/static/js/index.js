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
		$(this).attr('href', 'index.html');
	})
	//----------------侧边栏特效----------------------
	$('.siderbar-hover').hover(
		function(){
			var aa = $(this).children('.siderbar-show').outerWidth();
			var $oThis = $(this);
			$(this).children('.siderbar-show').css('display','block').stop(true,false);
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
	//--------------------------楼层定位------------
	
	$(window).on('scroll', function(event){
		if($(window).scrollTop() > 1330){
			$('#floorsider').stop(true, false).animate({left : 0},100, function(){
				$('.tofirst').on('click', function(){
					$(window).scrollTop(1525);
				})
				if($(window).scrollTop() < 1425||$(window).scrollTop() > 1900){
					$('.tofirst').animate({marginLeft : -30},100);
				}else{
					$('.tofirst').animate({marginLeft : 0},100);
				}
				//-------------2F------------
				$('.tosecond').on('click', function(){
					$(window).scrollTop(2179);
				})
				if($(window).scrollTop() < 1900||$(window).scrollTop() > 2500){
					
					$('.tosecond').animate({marginLeft : -30},100);
				}else{
					$('.tosecond').animate({marginLeft : 0},100);
				}
				//-------------3F--------------
				$('.tothird').on('click', function(){
					$(window).scrollTop(2833);
				})
				if($(window).scrollTop() < 2500||$(window).scrollTop() > 3000){
					$('.tothird').animate({marginLeft : -30},100);
				}else{
					$('.tothird').animate({marginLeft : 0},100);
				}
				//-------------4F--------------
				$('.tofouth').on('click', function(){
					$(window).scrollTop(3487);
				})
				if($(window).scrollTop() < 3000||$(window).scrollTop() > 3900){
					$('.tofouth').animate({marginLeft : -30},100);
				}else{
					$('.tofouth').animate({marginLeft : 0},100);
				}
			});
		}else{
			$('#floorsider').animate({left : -80},500);
		}
	})
	//----------------------顶部下拉-------------------
	$('.head-nav').hover(function(){
		$(this).children('dd').stop(true, false).slideDown(100);
	},
	function(){
		$(this).children('dd').stop(true, false).slideUp(100);
		
	})
	//------------------banner轮播--------------------
	jQuery(".slideBox").slide({mainCell:".bd ul",effect:"fold",autoPlay:true,delayTime:700});
	//------------------楼层中左右轮播-------------
	jQuery(".slideBox1").slide({mainCell:".bd ul",effect:"leftLoop",autoPlay:true,delayTime:700});
	//------------------楼层中上下轮播-------------
	 jQuery(".picScroll-top").slide({titCell:".hd ul",mainCell:".bd ul",autoPage:true,effect:"topLoop",autoPlay:true,vis:4});
	//------------------楼层选项卡---------------
	$('.floor1-nav > li').hover(function(){
		var aa = $(this).index();
		$('.floor1-nav > li').children('a').css({background:'white', color: '#666'});
		$(this).children('a').css({background:'#4595c6', color: 'white'});
		$('.firstfloor-tab').css('display', 'none');
		$('.firstfloor-tab').eq(aa).css('display', 'block');
	},
	function(){
	});
	//-----------2F----------
	$('.floor2-nav > li').hover(function(){
		var aa = $(this).index();
		$('.floor2-nav > li').children('a').css({background:'white', color: '#666'});
		$(this).children('a').css({background:'#27ae61', color: 'white'});
		$('.secondfloor-tab').css('display', 'none');
		$('.secondfloor-tab').eq(aa).css('display', 'block');
	},
	function(){
	});
	//-----------3F-------------
	$('.floor3-nav > li').hover(function(){
		var aa = $(this).index();
		$('.floor3-nav > li').children('a').css({background:'white', color: '#666'});
		$(this).children('a').css({background:'#2b3282', color: 'white'});
		$('.thirdfloor-tab').css('display', 'none');
		$('.thirdfloor-tab').eq(aa).css('display', 'block');
	},
	function(){
	});
	//-----------4F-------------
	$('.floor4-nav > li').hover(function(){
		var aa = $(this).index();
		$('.floor4-nav > li').children('a').css({background:'white', color: '#666'});
		$(this).children('a').css({background:'#f7994a', color: 'white'});
		$('.fourthfloor-tab').css('display', 'none');
		$('.fourthfloor-tab').eq(aa).css('display', 'block');
	},
	function(){
	});
	//-----------所有图片上浮效果-----------
	$('.firstfloor-right-down>li').hover(function(){
		$(this).children('dl').children('dt').children('img').stop(true,false).animate({top: 0},200);
	},
	function(){
		$(this).children('dl').children('dt').children('img').stop(true,false).animate({top: 15},200);
	})
	$('.firstfloor-tab2>li').hover(function(){
		console.log(1);
		$(this).children('dl').children('dt').children('a').children('img').stop(true,false).animate({top: -15},200);
	},
	function(){
		$(this).children('dl').children('dt').children('a').children('img').stop(true,false).animate({top: 0},200);
	})
	//-----------手风琴------------
	//------------1f------------
	var $firstOli = $('.first-accordion>li');
	for(var i = 0; i < $firstOli.length; i++){
		if(i === 0){
			$firstOli.eq(i).css({top: 0});
		}else{
			$firstOli.eq(i).css({top: 110+39*i})
		}
	}
	$firstOli.hover(function(event){
		event.stopPropagation();
		for(var j = 0; j<$firstOli.length; j++){
			if($firstOli.eq(j).index()<=$(this).index()){
				$firstOli.eq(j).stop(true,false).animate({top : 39*j}, 200);
			}else{
				$firstOli.eq(j).stop(true,false).animate({top : 110+39*j}, 200);
			}
		}
	})
	//------------2f--------------------
	var $oLi = $('.second-accordion>li');
	for(var i = 0; i < $oLi.length; i++){
		if(i === 0){
			$oLi.eq(i).css({top: 0});
		}else{
			$oLi.eq(i).css({top: 110+39*i})
		}
	}
	$oLi.hover(function(event){
		event.stopPropagation();
		for(var j = 0; j<$oLi.length; j++){
			if($oLi.eq(j).index()<=$(this).index()){
				$oLi.eq(j).stop(true,false).animate({top : 39*j}, 200);
			}else{
				$oLi.eq(j).stop(true,false).animate({top : 110+39*j}, 200);
			}
		}
	})
	//-----------3f--------------
	var $thirdLi = $('.third-accordion>li');
	for(var i = 0; i < $thirdLi.length; i++){
		if(i === 0){
			$thirdLi.eq(i).css({top: 0});
		}else{
			$thirdLi.eq(i).css({top: 110+39*i})
		}
	}
	$thirdLi.hover(function(event){
		event.stopPropagation();
		for(var j = 0; j<$thirdLi.length; j++){
			if($thirdLi.eq(j).index()<=$(this).index()){
				$thirdLi.eq(j).stop(true,false).animate({top : 39*j}, 200);
			}else{
				$thirdLi.eq(j).stop(true,false).animate({top : 110+39*j}, 200);
			}
		}
	})
	//-----------4f------------
	var $fourthLi = $('.fourth-accordion>li');
	for(var i = 0; i < $fourthLi.length; i++){
		if(i === 0){
			$fourthLi.eq(i).css({top: 0});
		}else{
			$fourthLi.eq(i).css({top: 110+39*i})
		}
	}
	$fourthLi.hover(function(event){
		event.stopPropagation();
		for(var j = 0; j<$fourthLi.length; j++){
			if($fourthLi.eq(j).index()<=$(this).index()){
				$fourthLi.eq(j).stop(true,false).animate({top : 39*j}, 200);
			}else{
				$fourthLi.eq(j).stop(true,false).animate({top : 110+39*j}, 200);
			}
		}
	})
	//--------------左侧图标上下运动-------------
	$('.banner-serve>li').hover(function(){
		var $oThis = $(this);
		$(this).children('a').children('img').animate({top: 0,opacity: 0},200,function(){
			$oThis.children('a').children('img').css({top: 17,opacity: 100});
			$oThis.children('a').children('img').animate({top: 15},100);
			
		});
	},
	function(){
		
	})
	//-------------底部回顶---------
	$('.huiding').on('click', function(){
		$(window).scrollTop(0);
	})
	//----------------搜索框跨域
	
	
})




