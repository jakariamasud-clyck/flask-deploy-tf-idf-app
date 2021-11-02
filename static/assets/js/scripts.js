/* ************* SOME FUNTION INIT INDEX ******************

1.STICKY NAVBER FUNTION
2.SOME LITTLE PLUGIN ACTIVE FUNTION

--------------------
->DOCUMENT READY ALL FUNCTION  CALL

************************************* */

(function ($) {
	'use strict';


	/* ------ GLOBAL VARIABLE  ------- */

	/*============  1.ADVANCE OPTION SHOW / Hide FUNTION ===========*/
	function advance_option_show_hide() {
		$(".triggerAdvance-btn").on('click', function () {
			var thatBtn = $(this);
			thatBtn.add('.mda-filterAdvance').toggleClass('active');

			setTimeout(function () {
				if (thatBtn.hasClass('active')) {
					$("#mda_advo").val('active');
				} else {
					$("#mda_advo").val('deactive');
				}
			}, 300);
		});

	}

	/*============  2.SUM Same Key Val  FUNTION ===========*/
	function data_table() {
		$('#tableOfValues table, #sentenceScores table').DataTable();

	}

	/*============  2.DEVICE OPTION SELECTION FUNTION ===========*/
	function device_option_selection() {
		var devices = $('.mda-device-field .mda-sf-item i');
		devices.on('click', function () {
			var thatDvi = $(this);
			devices.removeClass('active')
			thatDvi.addClass('active');
			$('#mda_device').val(thatDvi.data('device'));
		});

	}

	/*============= xxxxxxxxxxxxxxxxxxxxxxxxx ===========*/

	/*============= DOCUMENT READY ALL FUNCTION  CALL ===========*/
	$(function () {
		if (typeof advance_option_show_hide == 'function') {
			advance_option_show_hide();
		}
		if (typeof device_option_selection == 'function') {
			device_option_selection();
		}
		if (typeof data_table == 'function') {
			data_table();
		}
	});


	/*============= WINDOW LOAD RESIZE FUNTION CALL ===========*/
	//$(window).on("load  resize",function(){});


})(jQuery);