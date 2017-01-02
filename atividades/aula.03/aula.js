var map = function() {
	for (i = 0; i <= (this._id.length - 1); i++) {
		emit(this._id.substring(i, (i + 1)), 1);
	}
}

var reduce = function(key, values) {
	return Array.sum(values);
}
