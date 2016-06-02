var app = angular.module('rfSwitchApp', []);
app.controller('SwitchController',function($scope,$http){
	$scope.sendForm = {}
	$http.get("/api/switches").then(function(response) {
		$scope.switches=response.data;
	});
	$scope.turnOn = function(switchId) {
		$http.post("/api/switches/"+switchId+"/on");	
	};
	$scope.turnOff = function(switchId) {
		$http.post("/api/switches/"+switchId+"/off");	
	};
	$scope.submitForm = function() {
		$http.post("/api/send",$scope.sendForm)
	};
});
