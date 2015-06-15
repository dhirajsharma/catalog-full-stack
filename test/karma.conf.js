module.export = function(config){
  config.set({
    basePath: '../',

    files: [
      'static/components/angular/angular.js',
      'static/components/angular-route/angular-route.js',
      'static/components/angular-resource/angular-resource.js',
      'static/components/angular-animate/angular-animate.js',
      'static/components/angular-mocks/angular-mocks.js',
      'static/js/**/*.js',
      'test/unit/**/*.js'
    ],

    autoWatch: true,

    frameworks: ['jasmine'],
    browsers: ['Chrome'],
    plugins: [
            'karma-chrome-launcher',
            'karma-firefox-launcher',
            'karma-jasmine'
            ],

    junitReporter : {
      outputFile: 'test_out/unit.xml',
      suite: 'unit'
    }
  });
};