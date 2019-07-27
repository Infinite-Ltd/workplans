
function addplan() {
	$(function() {
		var name1 = $("#name1")
		$('#aa').dialog({
			height:300,
			width:400,
			modal:true, //是否使用模式，为true时背景半透明不能修改的效果
			buttons:{
				"确认":function () {
					  var bValid = true;
			          if ( bValid ) {
			           alert(name1.val());
			          }

					$(this).dialog("close");
				},
				"取消":function () {
					$(this).dialog("close");
				}
			}
		});
	})
	}

