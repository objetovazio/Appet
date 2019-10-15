import { Component, OnInit, ContentChildDecorator } from '@angular/core';
import { NgForm } from '@angular/forms';

import { Login } from '../model/Login';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  login:Login;

  constructor() { }

  ngOnInit() {
    this.login = new Login();
  }

  onSubmit(form: NgForm){
    console.log(form.value)
  }

}
