Modern Portfolio Theory Statistics
##################################

:date: 2014-09-21
:tags: finance, investing, widget
:slug: modern-portfolio-theory-statistics
:author: Gouthaman Balaraman
:description: This is a small widget that lets you view the modern portfolio theory statistics for a selection of stocks
:keywords: finance


This widget shows Modern Portfolio Theory (MPT) statistics for a selected list of stocks. The calculations were made
using Quandl_ data in the WIKI_ dataset. The ETF SPY was used as a benchmark using a 5-year time horizon. If the time
series is not long enough, then an N/A is shown. You can also download the CSV_File_ containing all the metrics.


.. raw:: html

    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.25/angular.min.js"></script>
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <script>
        var myModule = angular.module('mptApp', []);
        myModule.controller('mptCtrl', ['$scope','$http', function($scope, $http){
			/* Initialization steps */
			var url = "/extra/data/mptstats/mpt_5y_latest.csv";
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
			            $scope.tickerData = $scope.data[d];  
		                return; 
		            }
            	}
            	$scope.message = "Ticker not found";
            	$scope.tickerData = null;
			};
		}]);    
    </script>
    <div ng-app="mptApp">
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
					<div class="col-md-6">
						<table class="table table-striped col-md-6">
							<tbody>
								<tr>
									<td> <span class = "pull-left key"> Ticker</span></td>
									<td> <span class = "pull-right value"> {{tickerData.Ticker}} </span></td>
								</tr>
								<tr>
									<td> <span class = "pull-left key"> Alpha (%) </span></td>
									<td> <span class = "pull-right value"> {{tickerData.Alpha}} </span></td>
								</tr>
								<tr>
									<td> <span class = "pull-left key"> Beta </span></td>
									<td> <span class = "pull-right value"> {{tickerData.Beta}} </span></td>
								</tr>
								<tr>
									<td> <span class = "pull-left key"> R-Squared </span></td>
									<td> <span class = "pull-right value"> {{tickerData.RSquared}} </span></td>
								</tr>
								<tr>
									<td> <span class = "pull-left key"> Momentum (%) </span></td>
									<td> <span class = "pull-right value"> {{tickerData.Momentum}} </span></td>
								</tr>
								<tr>
									<td> <span class = "pull-left key"> Annualized Return (%) </span></td>
									<td> <span class = "pull-right value"> {{tickerData.AnnualizedReturn}} </span></td>
								</tr>
								<tr>
									<td> <span class = "pull-left key"> Standard Deviation (%) </span></td>
									<td> <span class = "pull-right value"> {{tickerData.StandardDeviation}} </span></td>
								</tr>
							</tbody>
						</table>
					</div> <!-- column 1 div -->
					<div class="col-md-6">
						<table class="table table-striped ">
							<tbody>
								<tr>
									<td> <span class = "pull-left key"> Sharpe Ratio </span></td>
									<td> <span class = "pull-right value"> {{tickerData.SharpeRatio}} </span></td>
								</tr>
														<tr>
									<td> <span class = "pull-left key"> Sortino Ratio </span></td>
									<td> <span class = "pull-right value"> {{tickerData.SortinoRatio}} </span></td>
								</tr>
								<tr>
									<td> <span class = "pull-left key"> Information Ratio </span></td>
									<td> <span class = "pull-right value"> {{tickerData.InformationRatio}} </span></td>
								</tr>
								<tr>
									<td> <span class = "pull-left key"> Treynor Ratio </span></td>
									<td> <span class = "pull-right value"> {{tickerData.TreynorRatio}} </span></td>
								</tr>
						
								<tr>
									<td> <span class = "pull-left key"> Tracking Error (%) </span></td>
									<td> <span class = "pull-right value"> {{tickerData.TrackingError}} </span></td>
								</tr>
								<tr>
									<td> <span class = "pull-left key"> Upside Capture (%) </span></td>
									<td> <span class = "pull-right value"> {{tickerData.UpsideCapture}} </span></td>
								</tr>
								<tr>
									<td> <span class = "pull-left key"> Downside Capture (%)</span></td>
									<td> <span class = "pull-right value"> {{tickerData.DownsideCapture}} </span></td>
								</tr>
							</tbody>
						</table>
					</div> <!-- column 2 div-->
					<small><span class="key">As of date: {{tickerData.Date}}</span></small>
				</div><!-- results -->
				<div id="error" ng-if="tickerData==null">
					{{message}}
				</div>
			</div>
			
        </div> <!-- controller -->
    </div><!--app -->
    
    


.. _Quandl:  https://www.quandl.com/
.. _WIKI: https://www.quandl.com/WIKI
.. _CSV_File: /extra/data/mptstats/mpt_5y_latest.csv
