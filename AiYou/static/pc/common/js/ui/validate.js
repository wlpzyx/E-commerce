!function(t){function F(t,F,e){var u=this;u.self=u,u.that=t,u.conf=F,u.valid=!1,u.checked=!0,u.requestType=e,u.init=function(){u.bindEvent()},u.init()}var e,u={rules:{},messages:{},tipsPositionClass:".J_validate",rightClassName:"correctTip",errorClassName:"tip_erorr",callback:null};F.prototype={constructor:F,bindEvent:function(){var F=this;F.that.find(":text, :password, :file, select, textarea").blur(function(){F.check(t(this))}),F.that.submit(function(u,a){return e=!0,F.valid=!1,t(this).find(":text, :password, :file, select, textarea").each(function(){F.check(t(this))}),F.that.find("."+F.conf.errorClassName).length>0?!1:(a&&(F.valid=!0,u.preventDefault()),!0)}).on("setRules.setRules",function(e,u){null==u?F.checked=!1:(t.extend(F.conf,u),F.checked=!0)})},check:function(F,e){var u=this;u.checked&&t.each(u.conf.rules,function(a,n){a==F[0].name&&t.each(n,function(t,n){if("remote"!=t||e||F.data("remote","remote"),F.data("remote"))u.methods[t](F,n,u,u.conf.messages[a][t]);else{if(!u.methods[t](F,n,u))return u.showError(F,u.conf.messages[a][t]),!1;u.hideError(F,u.conf.messages[a][t])}})})},methods:{required:function(t,F,e){return e.getLength(t.val())>0},email:function(t){var F=/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i;return F.test(t.val())},remote:function(F,e,u,a){var n={};n[t(F).attr("name")]=t(F).val(),"securitycode"==t(F).attr("name")&&(n.UserK="undefined"==typeof UserK?UserK="":UserK),t.ajax({url:e,dataType:u.requestType||"jsonp",data:n,async:!1,success:function(t){return 1==t.status?(u.hideError(F,a),F.removeData("remote"),!0):(t.msg&&(a=t.msg),u.showError(F,a),u.getLength(F.val())||(F.removeData("remote"),u.check(F,!0)),!1)},error:function(){return!1}})},maxLength:function(t,F,e){return e.getLength(t.val())<F},equalTo:function(t,F){return t.val()==F.val()},passwordT:function(t){var F=/^[0-9]{6,32}$/,e=/^[a-zA-Z]{6,32}$/,u=/[\u4E00-\u9FA5]/,a=/^[@!#\$%&'\*\+\-\/=\?\^_`{\|}\[\]<>\(\)"~,\.:;\\]{6,32}$/,n=/^[0-9a-zA-Z@!#\$%&'\*\+\-\/=\?\^_`{\|}\[\]<>\(\)"~,\.:;\\]{6,32}$/;return F.test(t.val())||e.test(t.val())||a.test(t.val())||u.test(t.val())||!n.test(t.val())?!1:!0},rangelength:function(F,e,u){var a=u.getLength(t.trim(F.val()));return a>=e[0]&&a<=e[1]},mobileEmail:function(t){var F=/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i,e=/^(13|15|18)\d{9}$/;return F.test(t.val())||e.test(t.val())},mobile:function(F){var e=/^(13|15|18|17|14)\d{9}$/;return e.test(t.trim(F.val()))},findpwd1:function(F){return"请输入您的手机号码"==t.trim(F.val())},idcard:function(F){var e=/^[\d]+$/;return e.test(t.trim(F.val()))},decimal:function(t,F){var e="^\\d{1,para1}$",u="^(\\d{1,para1})+(\\.)+(\\d{1,para2})$",a=new RegExp(e.replace("para1",F[0])),n=new RegExp(u.replace("para1",F[0]).replace("para2",F[1]));return a.test(t.val())||n.test(t.val())},number_:function(t){var F=/^\d+$/;return F.test(t.val())},im:function(t){var F=/^\d+$/;return F.test(t.val())},isAuthCode:function(F,e){return/\w{6}/.test(t.trim(e()))},postalcode:function(t){var F=/^[1-9][0-9]{5}$/;return F.test(t.val())}},showError:function(F,u){var a=this;e&&(t(window).scrollTop()>F.offset().top&&t(window).scrollTop(F.offset().top),e=!1),a.hasTipsDiv(F)?(F.parents().next(a.conf.tipsPositionClass).children().removeClass(a.conf.rightClassName).addClass(a.conf.errorClassName),F.parents().next(a.conf.tipsPositionClass).html(u)):F.parents().next(a.conf.tipsPositionClass).html('<i class="'+a.conf.errorClassName+' inline"></i>'+u).show()},hideError:function(t){var F=this,e=t.parents().next(F.conf.tipsPositionClass);F.hasTipsDiv(t)?e.html("").children().removeClass(F.conf.errorClassName).addClass(F.conf.rightClassName):e.html('<i class="'+F.conf.rightClassName+' inline"></i>')},submit:function(){},hasTipsDiv:function(t){var F=this;return t.parents().next(F.conf.tipsPositionClass+"."+F.conf.rightClassName).length>0||t.parents().next(F.conf.tipsPositionClass+"."+F.conf.errorClassName).length>0?!0:!1},getLength:function(F){return t.trim(F).length}},t.fn.validateFn=function(e,a){var n=this.data("validateFn");this.length<0||n||(e=t.extend({},u,e),this.each(function(){n=new F(t(this),e,a),t(this).data("validateFn",n)}))},t.extend(t.fn,{validSubmit:function(){return t(this).trigger("submit",[!0]),t(this).data("validateFn").valid},setRules:function(F){t(this).trigger("setRules",[F])}})}(jQuery);