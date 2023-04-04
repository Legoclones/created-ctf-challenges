// imports and initializations
var express = require("express")
var assert = require('assert')
var app = express()
var bodyParser = require('body-parser');
const Browser = require("zombie");
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'))
Browser.waitDuration = '30s';

browser = new Browser({
    maxWait: 1000,
    waitDuration: 5*1000
});

// endpoint to submit links to
app.post('/report',function(req,res){
    url=req.body.url;
    browser.visit(url, function() {
        browser.setCookie({ name: 'flag', domain: 'byuctf.xyz', path:'/', value: 'byuctf{xss_1s_a_v3ry_common_m3thod_of_attack!}'});
        console.log("Visiting "+url)
        res.sendFile(__dirname+'/public/response.html')
    })
});

// main page to submit link
app.get('/',function(req,res){
    res.sendFile(__dirname+'/public/index.html')
})

// start app
app.listen(1337,()=>{
    console.log("Running on 1337");
});