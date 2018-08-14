'use strict';

var express = require('express');
var router = express.Router();
// import {User} from "./Model/User"
var User = require('./Model/User');
router.get('/hello', function (req, res) {
    res.send("Helloo fucked up world World!");
});
router.post('/signup', function (req, res) {
    //get data from the api
    var user = new User();
    user.name = req.body.name;
    user.email = req.body.email;
    user.password = req.body.password;
    console.log(user);
});
module.exports = router;