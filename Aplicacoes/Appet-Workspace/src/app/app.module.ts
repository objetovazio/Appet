import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { MatIconModule } from '@angular/material/icon'
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { MenuPrincipalComponent } from './menu-principal/menu-principal.component';
import { RodapeComponent } from './rodape/rodape.component';
import { LoginComponent } from './login/login.component';
import { NovoUsuarioComponent } from './novo-usuario/novo-usuario.component';
import { BuscarServicoComponent } from './buscar-servico/buscar-servico.component';
import { FormsModule } from '@angular/forms' 
import { MeuPerfilComponent } from './meu-perfil/meu-perfil.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { EditarPerfilComponent } from './editar-perfil/editar-perfil.component';
import { AgendaComponent } from './agenda/agenda.component';
import { HomeComponent } from './home/home.component';

@NgModule({
  declarations: [
    AppComponent,
    MenuPrincipalComponent,
    RodapeComponent,
    LoginComponent,
    NovoUsuarioComponent,
    BuscarServicoComponent,
    MeuPerfilComponent,
    EditarPerfilComponent,
    AgendaComponent,
    HomeComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    MatIconModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
