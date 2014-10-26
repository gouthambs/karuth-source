Econometric Factor Model
########################

:date: 2014-10-20
:tags: finance, investing, widget
:slug: econometric-factor-model
:author: Gouthaman Balaraman
:description: An econometric factor model to explain factor exposures and exposures
:keywords: finance, factor model


    
.. raw:: html

    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.25/angular.min.js"></script>
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <script>
        var myModule = angular.module('myApp', []);
            myModule
            .directive( 'barChart', function(){
                var directive = {
                    restrict : 'E',
                    replace : true,
                    scope : { 
                        dataset: '=' // bidirectional data binding
                        },
                    template :  '<svg ng-attr-width="{{graph.width}}" ng-attr-height="{{graph.height}}"></svg>',
                    link : function(scope, element, attrs){
                        scope.graph = {height: 200, width: 400};
                        scope.width = function(){
                            dataPoints = scope.dataset.length;
                            return scope.graph / dataPoints;
                         };
                         scope.height = function(data) {
                            max = Math.max.apply(null, scope.dataset);
                            return data / max * scope.graph.height;
                         };
                         scope.x = function(index) {
                            index * scope.width();
                         };
                         scope.y = function(index){
                            scope.graph.height - scope.height(data);
                         };
                    }
                };
                return directive;
        });
        
        myModule.controller('mptCtrl', ['$scope','$http', function($scope, $http){
			/* Initialization steps */
			var url = "/extra/data/factormodels/fm_5y_latest.csv";
            $scope.factorItems = ["Alpha","Unemployment","ConsumerSentiment","Market","Size","ValueGrowth"];
            $scope.riskItems = ["TotalRisk","DiversifiableRisk","NonDiversifiableRisk"];
            $scope.myData = [10,20,30,40,60, 80, 20, 50];
			$http.get(url).success(function(respData, status, headers, config){
				var data = d3.csv.parse( respData ); 			
				$scope.data = data;
                $scope.ticker = 'AAPL';
                $scope.fetchTickerData($scope.ticker);
			});
			$scope.fetchTickerData = function(ticker){
				$scope.message = "";
				ticker = ticker.toUpperCase();
				for (var d = 0, len = $scope.data.length; d < len; d += 1) {
		            if ($scope.data[d].Ticker == ticker) {
			            var data = $scope.data[d];  
                        var factors = ["Alpha","Unemployment","ConsumerSentiment","Market","Size","ValueGrowth"];
                        var datalist = {};
                        for(var i = 0; i < factors.length; i+=1){
                            datalist[factors[i]] = {exposure: data[factors[i]], std:data[factors[i]+"Std"]};
                        }
                        datalist.Ticker = data.Ticker;
                        datalist.Date = data.Date;
                        datalist.TotalRisk = data.TotalRisk;
                        datalist.DiversifiableRisk = data.DiversifiableRisk;
                        datalist.NonDiversifiableRisk = data.NonDiversifiableRisk;
                        $scope.tickerData = datalist;
                        return;
		            }
            	}
            	$scope.message = "Ticker not found";
            	$scope.tickerData = null;
			};
		}]);    
    </script>
    <div ng-app="myApp">
        <div ng-controller="mptCtrl">
            <form class="form-inline" ng-submit="fetchTickerData(ticker)">
				<fieldset>
					<!-- Form Name -->
					<!-- Text input-->
					<div class="form-group col-md-2 ">
					  <div class="">
					  	<input id="ticker" name="ticker" type="text" placeholder="TICKER" class="form-control input-md" ng-model="ticker">
					  </div>
					</div>

					<!-- Button -->
					<div class="form-group col-md-2 col-md-offset-2">
					  <div class="">
						<button id="submit" name="submit" class="btn btn-primary">Submit</button>
					  </div>
					</div>
				</fieldset>
			</form>
			<hr/>
            
			<div style="height:800px; ">
				<div id="results" ng-show="tickerData !=null">
					<div class="col-md-12">
                        <strong>Factor Exposures - {{tickerData.Ticker}}</strong>
                        <br/>
						<table class="table table-bordered col-md-12">
                            <thead>
								<tr>
									<th> <span class = "pull-left value">Factor</span></td>
									<th> <span class = "pull-right value"> Exposure </span></td>
                                    <th> <span class = "pull-right value"> Standard Deviation </span></td>
								</tr>
							</thead>
							<tbody>
								<tr ng-repeat="item in factorItems">
									<td> <span class = "pull-left key">{{item}}</span></td>
									<td> <span class = "pull-right value"> {{tickerData[item].exposure}} </span></td>
                                    <td> <span class = "pull-right value"> {{tickerData[item].std}} </span></td>
								</tr>
								
							</tbody>
						</table>
                        <strong>Risk - {{tickerData.Ticker}}</strong>
                        <br/>
						<table class="table table-bordered col-md-12">
                            <thead>
								<tr>
									<th> <span class = "pull-right value">Total Risk (%)</span></td>
									<th> <span class = "pull-right value">Diversifiable Risk (%)</span></td>
                                    <th> <span class = "pull-right value"> Non-Diversifiable Risk (%)</span></td>
								</tr>
							</thead>
							<tbody>
								<tr>
									<td> <span class = "pull-right key">{{tickerData.TotalRisk}}</span></td>
									<td> <span class = "pull-right value"> {{tickerData.DiversifiableRisk}} </span></td>
                                    <td> <span class = "pull-right value"> {{tickerData.NonDiversifiableRisk}} </span></td>
								</tr>
							</tbody>
						</table>
					</div> <!-- column 1 div -->
					<small>
                        <span class="key">As of date: {{tickerData.Date}}</span>
                    </small>
				</div><!-- results -->
				<div id="error" ng-if="tickerData==null">
					{{message}}
				</div>
			</div>
			
        </div> <!-- controller -->
    </div><!--app -->
    