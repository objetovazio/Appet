import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {  } from '@angular/router';
import { IndexComponent } from './index/index.component';
import { LoginComponent } from './login/login.component';
import { NovoUsuarioComponent } from './novo-usuario/novo-usuario.component';
import { BuscarServicoComponent } from './buscar-servico/buscar-servico.component';
import { MeuPerfilComponent} from './meu-perfil/meu-perfil.component';
import { EditarPerfilComponent} from './editar-perfil/editar-perfil.component';
import { AgendaComponent } from './agenda/agenda.component';

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
  },
  {
    path: 'meu-perfil',
    component: MeuPerfilComponent,
    data: { title: 'Bem vindo ao Appet' }
  },
  {
    path: 'editar-perfil',
    component: EditarPerfilComponent,
    data: { title: 'Bem vindo ao Appet' }
  },
  {
    path: 'agenda',
    component: AgendaComponent,
    data: { title: 'Bem vindo ao Appet' }
  }
  

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
