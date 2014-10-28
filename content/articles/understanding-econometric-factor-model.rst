Understanding the Econometric Factor Model
##########################################

:date: 2014-10-26
:tags: finance, investing, widget
:slug: understanding-econometric-factor-model
:author: Gouthaman Balaraman
:description: Here I explain how to make sense of the econometric factor model widget.
:keywords: finance, factor model

The post explains the `Econometric Factor Model <|filename|./widgets/econometric-factor-model.rst>`_ widget
that I have built. The factors used in the econometric factor model are: *unemployment*, 
*consumer sentiment*, *market*, *size* and *value/growth*. A brief explanation of the factors are
as follows. 

- The *unemployment* factor is a proxy for the state of economy, and exposure to this factor 
  measures the impact the economy can have on the performance of this stock.
- The *consumer sentiment* is a voice of consumers behaviour and sentiment, and this factor
  can help understand the impact of consumer confidence on the stock's performance.
- The exposure to *market* factor captures how the stock's performance is correlated with 
  that of the market.
- The *size* factor (or SML - Small Minus Large ) is a measure of the excess returns that
  the small cap has over the large cap stocks. The exposure to this factor is meant to 
  capture the impact size has on the performance of this stock. Small (large) cap stock will 
  typically have positive (negative) exposures to this factor.
- The *value/growth* (or HML - High book-to-value Minus Low) is meant to identify the
  value or growth aspect of a stock.
  
As a use case, let us try a few examples and see if it makes sense.

.. raw:: html

    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.25/angular.min.js"></script>
    <script>
        var myModule = angular.module('myApp', []);
        myModule.controller('MyCtrl', ['$scope', function($scope){
            $scope.mfData = [
                {Ticker:"X", Unemployment: -0.76, ConsumerSentiment: -0.035, Market: 1.685, Size: 0.3281, Value: 1.509},
                {Ticker:"DAL", Unemployment: -1.183, ConsumerSentiment: 0.309, Market: 0.456, Size: 1.581, Value: 0.038},
                {Ticker:"LH", Unemployment: 0.461, ConsumerSentiment: 0.02, Market: 0.606, Size: 0.081, Value: -0.185},
                {Ticker:"MCD", Unemployment: 0.951, ConsumerSentiment: -0.132, Market: 0.423, Size: -0.329, Value: -0.018},
                {Ticker:"MSFT", Unemployment: -0.248, ConsumerSentiment: -0.192, Market: 1.032, Size: -0.542, Value: -0.05}
             ];    
        }]);
    </script>
    
    <div ng-app="myApp">
        <div ng-controller="MyCtrl">
            <div class="col-md-12">
                <table class="table table-bordered col-md-12">
                    <thead>
                        <tr>
                            <th> <span class = "pull-right key">Ticker</span></td>
                            <th> <span class = "pull-right key">Unemployment</span></td>
                            <th> <span class = "pull-right key"> Consumer Sentiment</span></td>
                            <th> <span class = "pull-right key"> Market</span></td>
                            <th> <span class = "pull-right key"> Size</span></td>
                            <th> <span class = "pull-right key"> Value</span></td>
                        </tr>
                    </thead>
                    <tbody>
                        <tr ng-repeat="item in mfData">
                            <td> <span class = "pull-right value">{{item.Ticker}}</span></td>
                            <td> <span class = "pull-right value"> {{item.Unemployment}} </span></td>
                            <td> <span class = "pull-right value"> {{item.ConsumerSentiment}} </span></td>
                            <td> <span class = "pull-right value">{{item.Market}}</span></td>
                            <td> <span class = "pull-right value">{{item.Size}}</span></td>
                            <td> <span class = "pull-right value">{{item.Value}}</span></td>
                        </tr>
                    </tbody>
                </table>        
            </div>
        </div>
    </div>
    

United States Steel Corporation (X), Delta Airlines (DAL), and MicroSoft (MSFT) have negative exposure to 
unemployment, meaning increase in unemployment (or a detiorating economy) hurts the returns of this
company. Mc Donalds (MCD) has a positive exposure to unemployment, in a hurting economy MCD has a better
business.

Delta Airlines has the most significant exposure to the consumer sentiment factor. This makes
sense because travel industry benefits from a positive consumer sentiment. 

The companies on the higher end of the large cap spectrum have a negative exposure to the size factor.
The strong positive exposure of DAL to size is a little puzzling, and its history of mergers with
Northwest might explain. This is also highlights that factor models do need more than intuition sometimes to 
make sense and make correct use of.






