'use strict';

var express = require('express');
var app = express();
var user = require('./user/user');
var bodyParser = require("body-parser");
app.use(user);
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());
app.listen(3000);