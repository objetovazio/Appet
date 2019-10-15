import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';

import { Usuario } from '../model/Usuario';

@Component({
  selector: 'app-novo-usuario',
  templateUrl: './novo-usuario.component.html',
  styleUrls: ['./novo-usuario.component.scss']
})
export class NovoUsuarioComponent implements OnInit {

  usuario:Usuario;

  constructor() { }

  ngOnInit() {
    this.usuario = new Usuario();
  }

  onSubmit(form: NgForm){
    console.log(form.value)
  }

}
