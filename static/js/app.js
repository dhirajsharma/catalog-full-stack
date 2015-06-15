/**
 * Created by michaael on 6/14/15.
 */

var appMain = angular.module('appMain', [], function() {

});

appMain.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{@{');
  $interpolateProvider.endSymbol('}@}');
});

