var dataMap = {
	modalTitle: 'data-one-step-delete-dlg-title',
	modalBody: 'data-one-step-delete-dlg-body',
	modalAction: 'data-one-step-delete-form',
	objDescription: 'data-obj-description'
};

(function($) {
    $.fn.oneStepDelete = function() {
        return this.each( function() {
        	$(this).on('show.bs.modal', function (event) {
        		var button = $(event.relatedTarget);
        		var dlg = $(this);
        		$.each(dataMap, function(key, value) {
        			var srcValue = button.data(key);
        			if(srcValue !== undefined) {
        				var target = dlg.find('[' + value + ']');
        				if(key == 'modalAction') target.attr('action', srcValue);
        				else target.text(srcValue);
        			}
        		});
        	});
        });
    }
}(jQuery));
