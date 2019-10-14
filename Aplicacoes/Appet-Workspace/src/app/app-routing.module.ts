import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {  } from '@angular/router';
import { IndexComponent } from './index/index.component';
import { LoginComponent } from './login/login.component';
import { NovoUsuarioComponent } from './novo-usuario/novo-usuario.component';
import { BuscarServicoComponent } from './buscar-servico/buscar-servico.component';

const routes: Routes = [
  {
    path: '',
    component: IndexComponent,
    data: { title: 'Bem vindo ao Appet' }
  },
  {
    path: 'login',
    component: LoginComponent,
    data: { title: 'Bem vindo ao Appet' }
  },
  {
    path: 'novo-usuario',
    component: NovoUsuarioComponent,
    data: { title: 'Bem vindo ao Appet' }
  },
  {
    path: 'buscar-servico',
    component: BuscarServicoComponent,
    data: { title: 'Bem vindo ao Appet' }
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
