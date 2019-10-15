import { NgForm } from '@angular/forms';
import { Component, OnInit } from '@angular/core';

import { BuscaServico } from '../model/BuscaServico';

@Component({
  selector: 'app-buscar-servico',
  templateUrl: './buscar-servico.component.html',
  styleUrls: ['./buscar-servico.component.scss']
})
export class BuscarServicoComponent implements OnInit {

  buscaservico:BuscaServico;
  constructor() { }

  ngOnInit() {
    this.buscaservico = new BuscaServico();
  }

  onSubmit(form: NgForm){
    console.log(form.value)
  }
}
