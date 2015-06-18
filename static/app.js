function SearchCtrl($scope, $http) {
	$scope.url = '/search'; // The url of our search
		
	// The function that will be executed on button click (ng-click="search()")
	$scope.search = function() {
		// Create the http post request
		// The request is a JSON request.

		$scope.items = false;
		$scope.no_items = false;

		$http.post($scope.url, { "data" : $scope.keywords}).
		success(function(data, status) {
			$scope.status = status;
			$scope.data = data;
			$scope.result = data; // Show result from server in our <pre></pre> element

			// Determine which element to show based on if any results were returned
			if(angular.equals({}, $scope.result)) {
				$scope.no_items = true;
			} else {
				$scope.items = true;
			}
			
		})
		.
		error(function(data, status) {
			$scope.data = data || "Request failed";
			$scope.status = status;			
		});
	};



}
