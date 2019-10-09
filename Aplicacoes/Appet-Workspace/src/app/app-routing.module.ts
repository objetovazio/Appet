import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {  } from '@angular/router';
import { IndexComponent } from './index/index.component';


const routes: Routes = [
  {
    path: 'index',
    component: IndexComponent,
    data: { title: 'Bem vindo ao Appet' }
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
